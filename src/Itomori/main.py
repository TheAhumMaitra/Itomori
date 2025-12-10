# SPDX-FileCopyrightText: 2025-present Ahum Maitra theahummaitra@gmail.com
#
# SPDX-License-Identifier: 	GPL-3.0-or-later


"""
Main python file to run Itomori
"""

# for cli interface
import argparse #to declare main interface
import subprocess  # for update with cli

# for generate ids
import uuid

# import all necessary type annotations
from typing import Any

# for saving the notes with time
import arrow

# to tell user a joke
import pyjokes

# to do the logging
from loguru import logger

# for interact with user
from textual import on

# Textual necessary imports
from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, Input, Label

# import containers for textual app
from textual.containers import Container, ScrollableContainer


# for saving and accessing notes (simple database)
from tinydb import TinyDB

# import all necessary components for Itomori

<<<<<<< HEAD
# About Screen
from Itomori.components.AboutScreen import AboutScreen

#Note input box
from Itomori.components.AddNoteInputBox import UserNoteInputBox

# Where 'notes.json' saved Warning
from Itomori.components.InfoWhereSaved import WhereSavedWarn

#for pushing the license texts in License screen
from Itomori.components.LicenseText import license_text

# For rendering the ASCII logo of Itomori
from Itomori.components.LogoText import LogoRender

#Showing user notes components
from Itomori.components.ViewNotes import ViewNotes

#Welcome text
=======
#import my 'Your Name' textual theme
from Itomori.themes.YourNameTheme import your_name

# All components
>>>>>>> 66a56de1db2cc0677a5c1c97c3b4c48d0e296b7a
from Itomori.components.WelcomeTextRender import WelcomeText
from Itomori import __version__

# main app class
class Itomori(App):
    """
    This is the main class of our app. This is required to run Textual app.

    :param app - inhertence from the Textual app class
    """

    logger.add(".logs/app.log", rotation="10 MB")

    # css style path
    CSS_PATH: str = "./style.tcss"

    # keyboard bindings for user
    BINDINGS = [
        ("^q", "quit", "Quit the app"),
        ("v", "show_ver", "Show About info"),
        ("n", "show_row_notes", "View All Notes"),
    ]

    # main method
    def compose(self) -> ComposeResult:
        """
        This is the main method. This method is to compose Itomori
        """
        #Loading the joke
        self.joke_label: Label = Label("Loading joke...", id="joke")

        yield Header(show_clock=True)  # show the Header with a little clock

        # scrollable container to show all components
        yield ScrollableContainer(
            LogoRender, WelcomeText, WhereSavedWarn, UserNoteInputBox
        )

        yield self.joke_label

        yield Footer()  # show footer

    # if any input submitted
    @on(Input.Submitted, "#NoteInputBox")  # anything submitted via note input field
    def handle_tasks(self) -> None:
        """
        This function helps us to receive user's typed input and store them in a json file (notes.json). This json file can keep append every time.
        """
        #main database
        db: TinyDB = TinyDB("notes.json")

        #get user's note
        user_typed_input: Any = self.query_one("#NoteInputBox")  # get user input

        #get the Note and strip it
        self.user_note: str = (
            user_typed_input.value.strip()
        )  # get the real value form 'user_typed_input'

        note: str = self.user_note  # make the note available for all scopes

        # get a beautiful date and time to store in the json file
        date_and_time: str = arrow.now().format("dddd, DD MMMM YYYY - hh:mm A (ZZZ)")

        # id for our note
        id: str = str(uuid.uuid4())

        # insert the note (with id, time and date)
        db.insert({"ID": id, "Note": note, "Time": date_and_time})

    #show version if the `v` key pressed
    def action_show_ver(self) -> None:
        """
        This method help us, if user pressed 'v' key in their keyboard then it help us to show the Version component (screen).
        """
        logger.info("User requested for exit the Version modal screen")

        self.push_screen(AboutScreen())  # push the modal screen

    # View note class for show the notes
    class ViewNote:
        Container(ViewNotes())

    #if user requested to close the app
    def action_quit(self) -> None:
        logger.info("User requested to exit the app!") #add a log
        self.app.exit() #exit the app

    #if user requested to show notes
    def action_show_row_notes(self) -> None:
        """
        This method help us, if user pressed 'n' key in their keyboard then it help us to show the all saved notes, raw json file.
        """
        logger.info("User requested for exit the Raw notes screen")
        self.push_screen(ViewNotes())  # push the screen

    #update the joke after 5 seconds
    def update_joke(self) -> None:
        joke: str = pyjokes.get_joke()
        self.joke_label.update(f"[b grey]{joke}[/b grey]")

    #ready these when the app loaded
    def on_mount(self) -> None:
        """
        This method helps us to when the app run successfully it quickly run these settings or tweaks
        """
        logger.info("Applied quick changes and theme changed")
        # Set the Itomori's default theme
        self.theme = "catppuccin-mocha"

<<<<<<< HEAD
    #ready before app loaded
=======
        # Register the `Your Name` theme
        self.register_theme(your_name)

>>>>>>> 66a56de1db2cc0677a5c1c97c3b4c48d0e296b7a
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
        return "\n\nUpdated Itomori successfully"

    if args.about:
        subprocess.run(["clear"])
        print(
            "Hello, This is Itomori, v1.0.0! A quick note taking TUI for you! License : GNU General Public License V3"
        )
        return

    if args.license:
        subprocess.run(["clear"])

        return """Itomori  Copyright (C) 2025  Ahum Maitra
    This program comes with ABSOLUTELY NO WARRANTY; for details type `--fullLicense'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `--fullLicense' for details."""

    if args.fullLicense:
        subprocess.run(["clear"])

        print(f"{license_text}")
        return

    if args.uninstall:
        subprocess.run(["clear"])

        print(
            "\n\nUninstalling Itomori, Sorry to say goodbye! I tried to make for you! I tried very hard to make Itomori for you, contact me for any feedback or if you faced an issue! Go to the GIthub repo and issues section and create a new issue! I hope it's help ! Press Ctrl + C to cancel!\n\n"
        )

        sure : str = input("Are you sure , you want to uninstall Itomori? (Y/n)")
        try :
            if sure == "Y" or sure == "y":
                subprocess.run(["uv", "tool", "uninstall", "Itomori"])
                return "I'm sad but Itomori is uninstalled from your computer or device"

            elif sure =="N" or sure == "n":
                return "Itomori uninstallation canceled!"
        except ValueError as error:
            return "Invalid value, please input correct option. Itomori uninstallation canceled!"

    logger.info("User requested to run the Itomori")
    app: Itomori = Itomori()
    app.run()


# if the file run directly
if __name__ == "__main__":
    app: Itomori = Itomori()  # app is 'Itomori' class [main class]
    try:
        app.run()  # try to run the app

    # if any critical error stops us to run the app or anything wrong
    except Exception as Error:
        raise Exception(
            f"Sorry! Something went wrong, it is too critical. Raw error - {Error}"  # give user a friendly message and also give user user what goes wrong
        )
