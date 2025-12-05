#   Copyright (C) 2025  Ahum Maitra

#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.

#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.

#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>


"""
Main python file to render Itomori
"""

import argparse  # for cli commands
import subprocess  # for update with cli

# to genarate new joke every 5 sec after
# import other modules or libraries
import uuid  # to generate id
from typing import Any, Tuple

import arrow  # to get current time and date

# import pyjoke to tell user a joke
import pyjokes
from loguru import logger  # for save and write the logs
from textual import on  # to interact with user

# Textual necessary imports
from textual.app import App, ComposeResult

# import containers for textual app
from textual.containers import Container, ScrollableContainer

# import necessary textual widgets
from textual.widgets import Footer, Header, Input, Label

# import all necessary libraries or modules
from tinydb import TinyDB

from Itomori.components.AboutScreen import AboutScreen
from Itomori.components.AddNoteInputBox import UserNoteInputBox
from Itomori.components.InfoWhereSaved import WhereSavedWarn
from Itomori.components.LicenseText import license_text
from Itomori.components.LogoText import LogoRender
from Itomori.components.ViewRawNotes import RawNotes

# All components
from Itomori.components.WelcomeTextRender import WelcomeText


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

        db: TinyDB = TinyDB("notes.json")
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
        db.insert({"ID": id, "Note": note, "Time": date_and_time})

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
        joke: str = pyjokes.get_joke()
        self.joke_label.update(f"[b grey]{joke}[/b grey]")

    def on_mount(self) -> None:
        """
        This method helps us to when the app run successfully it quickly run these settings or tweaks
        """
        logger.info("Applied quick changes and theme changed")
        # Set the Itomori's default theme
        self.theme = "catppuccin-mocha"

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
        print("You are using Itomori v1.0.0")
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

        return"""Itomori  Copyright (C) 2025  Ahum Maitra
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
        subprocess.run(["uv", "tool", "uninstall", "Itomori"])
        return "I'm sad but Itomori is uninstalled from your computer or device"

    app: Itomori = Itomori()
    app.run()


# if the file run directly
if __name__ == "__main__":
    app: Itomori = Itomori()  # app is 'Itomori' class [main class]
    try:
        app.run()  # try to run the app
        logger.info("User requested to run the Itomori")

    # if any critical error stops us to run the app or anything wrong
    except Exception as Error:
        raise Exception(
            f"Sorry! Something went wrong, it is too critical. Raw error - {Error}"  # give user a friendly messege and also give user user what goes wrong
        )
