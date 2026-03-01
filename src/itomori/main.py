# SPDX-FileCopyrightText: 2025-present Ahum Maitra theahummaitra@gmail.com
#
# SPDX-License-Identifier: 	GPL-3.0-or-later


"""
Main python file to render Itomori
"""

import argparse  # for cli commands
import subprocess  # for update with cli

# to generate new joke every 5 sec after
# import other modules or libraries
import uuid  # to generate id
from typing import Any, Tuple

import arrow  # to get current time and date
import random

from pathlib import Path

# import pyjoke to tell user a joke
import pyjokes
from loguru import logger  # for save and write the logs
from textual import on  # to interact with user

# Textual necessary imports
from textual.app import App, ComposeResult
from textual.containers import Container, ScrollableContainer
from textual.widgets import Footer, Header, Input, Label, ListView
from itomori.pages.ConfirmClearLogs import ConfirmClearLogs
from itomori.pages.ConfirmClearNotes import ConfirmClearNotes
from itomori.components.JohnWickQuotes import JOHN_WICK_QUOTES

# import all necessary libraries or modules
from tinydb import TinyDB

from itomori.pages.AboutScreen import AboutScreen
from itomori.components.AddNoteInputBox import UserNoteInputBox
from itomori.components.InfoWhereSaved import WhereSavedWarn
from itomori.components.LicenseText import license_text
from itomori.components.LogoText import LogoRender
from itomori.components.ViewRawNotes import RawNotes
from itomori.components.RecentNotes import get_recent_notes, recent_notes_text

#import my 'Your Name' textual theme
from itomori.themes.YourNameTheme import your_name

# All components
from itomori.components.WelcomeTextRender import WelcomeText
from itomori import __version__, LOG_PATH, DB_PATH, load_settings
from itomori.pages.Settings import Settings

# Load settings, confirm logger
settings = load_settings()
if settings.get("logs", True):
    logger.add(LOG_PATH, rotation="10 MB")
else:
    logger.disable("itomori")

# main app class
class Itomori(App):
    """
    This is the main class of our app. This is required to run Textual app.

    :param app - inherence from the Textual app class
    """

    # css style path
    CSS_PATH: str = "style.tcss"

    # keyboard bindings for user
    BINDINGS = [
        ("^q", "quit", "Quit the app"),
        ("v", "show_ver", "Show About info"),
        ("n", "show_row_notes", "View All Notes"),
        ("s", "render_settings", "Open Settings")
    ]

    # main method
    def compose(self) -> ComposeResult:
        """
        This is the main method. This method is to compose Itomori
        """
        self.joke_label: Label = Label("Loading joke...", id="joke")

        yield Header(show_clock=True)  # show the Header with a little clock

        # scrollable container to show all components
        yield ScrollableContainer(
            LogoRender, WelcomeText, WhereSavedWarn, UserNoteInputBox, recent_notes_text,
            ListView(*get_recent_notes(), id="notes_list")
        )


        yield self.joke_label

        yield Footer()  # show footer

    # if any input submitted
    @on(Input.Submitted, "#NoteInputBox")  # anything submitted via note input field
    def handle_tasks(self) -> None:
        """
        This function helps us to receive user's typed input and store them in a json file (notes.json). This json file can keep append every time.
        """

        db: TinyDB = TinyDB(DB_PATH)
        user_typed_input: Any = self.query_one("#NoteInputBox")  # get user input

        self.user_note: str = (
            user_typed_input.value.strip()
        )  # get the real value form 'user_typed_input'

        note: str = self.user_note  # make the note available all over the class

        # get a beautiful date and time to store in the json file
        date_and_time: str = arrow.now().format("dddd, DD MMMM YYYY - hh:mm A (ZZZ)")

        # id for our note
        id: str = str(uuid.uuid4())

        # insert the note (with id, time and date)
        # extract tags (starting with #) from the note
        tags = [word.lstrip("#") for word in self.user_note.split() if word.startswith("#")]
        
        db.insert({
            "ID": id, 
            "Note": note, 
            "Time": date_and_time,
            "Pinned": False,
            "Tags": tags
        })

        # Clear input box
        user_typed_input.value = ""

        # Update recent notes list
        notes_list = self.query_one("#notes_list", ListView)
        notes_list.clear()
        for item in get_recent_notes():
            notes_list.append(item)

    def action_render_settings(self) -> None:
        self.push_screen(Settings())

    def action_show_ver(self) -> None:
        """
        This method help us, if user pressed 'v' key in their keyboard then it help us to show the Version component (screen).
        """
        logger.info("User requested for exit the Version modal screen")

        self.push_screen(AboutScreen())  # push the modal screen

    class ViewNote:
        Container(RawNotes())

    def action_quit(self) -> None:
        logger.info("User requested to exit the app!")
        self.app.exit()

    def action_show_row_notes(self) -> None:
        """
        This method help us, if user pressed 'n' key in their keyboard then it help us to show the all saved notes, raw json file.
        """
        logger.info("User requested for exit the Raw notes screen")
        self.push_screen(RawNotes())  # push the screen

    def update_joke(self) -> None:
        settings = load_settings()
        startup_option = settings.get("startup_text", "jokes")
        
        if startup_option == "jokes":
            joke: str = pyjokes.get_joke()
            self.joke_label.update(f"[b grey]{joke}[/b grey]")
            self.joke_label.display = True
        elif startup_option == "quotes":
            quote: str = random.choice(JOHN_WICK_QUOTES)
            self.joke_label.update(f"[b grey]\"{quote}\" - John Wick[/b grey]")
            self.joke_label.display = True
        else:
            self.joke_label.display = False

    def on_mount(self) -> None:
        """
        This method helps us to when the app run successfully it quickly run these settings or tweaks
        """
        logger.info("Applied quick changes and theme changed")

        # Load theme from settings
        settings = load_settings()
        theme_name = settings.get("theme", "catppuccin-mocha")

        # Register the `Your Name` theme
        self.register_theme(your_name)

        # Set the theme
        self.theme = theme_name

    def on_ready(self) -> None:
        self.update_joke()

        # update every 10 seconds automatically
        self.set_interval(10, self.update_joke)


# main function for cli integration
def main():
    """
    This main function help us to run cli command to run Itomori (like : `Itomori`)
    """

    parser = argparse.ArgumentParser(
        prog="Itomori", description="A beautiful quick note taking tui app"
    )

    parser.add_argument(
        "--version",
        action="store_true",
        help="Shows the current Itomori version you are using",
    )

    parser.add_argument(
        "--update", action="store_true", help="To update Itomori automatically"
    )

    parser.add_argument(
        "--clearlogs", action="store_true", help="Clear all logs of Itomori"
    )

    parser.add_argument(
        "--clearnotes", action="store_true", help="Clear all notes of Itomori"
    )

    parser.add_argument("--about", action="store_true", help="Show Itomori's info")

    parser.add_argument("--license", action="store_true", help="Show Itomori's license")
    parser.add_argument(
        "--fullLicense",
        action="store_true",
        help="Show full LIcense text, conditions, policies, license details!",
    )

    parser.add_argument("--uninstall", action="store_true", help="Uninstall Itomori")
    args = parser.parse_args()

    if args.version:
        subprocess.run(["clear"])
        print(f"You are using Itomori {__version__}")
        return

    if args.clearlogs:
        print("Clearing the logs....")
        LOG_PATH.write_text("")
        print("Logs cleared successfully")
        return

    if args.clearnotes:
        print("Clearing the notes....")
        DB_PATH.write_text("")
        print("Notes cleared successfully")
        return

    if args.update:
        subprocess.run(["clear"])
        print("Updating Itomori....")
        subprocess.run(
            [
                "uv",
                "tool",
                "install",
                "git+https://github.com/TheAhumMaitra/Itomori.git",
            ]
        )
        print("Updated Itomori successfully")
        return

    if args.about:
        subprocess.run(["clear"])
        print(
            f"Hello, This is Itomori, v{__version__}! A quick note taking TUI for you! License : GNU General Public License V3"
        )
        return

    if args.license:
        subprocess.run(["clear"])

        print("""Itomori  Copyright (C) 2025  Ahum Maitra
    This program comes with ABSOLUTELY NO WARRANTY; for details type `--fullLicense'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `--fullLicense' for details.""")
        return

    if args.fullLicense:
        subprocess.run(["clear"])

        print(f"{license_text}")
        return

    if args.uninstall:
        subprocess.run(["clear"])

        print(
            "\n\nUninstalling Itomori, Sorry to say goodbye! I tried to make for you! I tried very hard to make Itomori for you, contact me for any feedback or if you faced an issue! Go to the GIthub repo and issues section and create a new issue! I hope it's help ! Press Ctrl + C to cancel!\n\n"
        )
        subprocess.run(["uv", "tool", "uninstall", "Itomori"])
        print("I'm sad but Itomori is uninstalled from your computer or device")
        return

    app: Itomori = Itomori()
    logger.info("Starting Itomori app...")
    app.run()
    logger.info("Itomori app exited normally.")


# if the file run directly
if __name__ == "__main__":
    app: Itomori = Itomori()  # app is 'Itomori' class [main class]
    try:
        logger.info("Starting Itomori app...")
        app.run()  #run the app
        logger.info("Itomori app exited normally.")

    # if any critical error stops us to run the app or anything wrong
    except Exception as Error:
        logger.error(f"Critical error: {Error}")
        raise Exception(
            f"Sorry! Something went wrong, it is too critical. Raw error - {Error}"  # give user a friendly messege and also give user user what goes wrong
        )
