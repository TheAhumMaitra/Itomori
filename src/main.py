"""
Main python file to render Itomori
"""

# import all necessary libraries or modules
from tinydb import TinyDB
import fire  # to give user a goood CLI UX
from loguru import logger  # for save and write the logs

# Textual necessary imports
from textual.app import App, ComposeResult

# import necessary textual widgets
from textual.widgets import Header, Footer, Input, Label

# import containers for textual app
from textual.containers import ScrollableContainer


# import pyjoke to tell user a joke
import pyjokes

# import other modules or libraries
import uuid  # to generate id

import arrow  # to get current time and date
from textual import on  # to interact with user

# All components
from components.WelcomeTextRender import WelcomeText
from components.AddNoteInputBox import UserNoteInputBox
from components.InfoWhereSaved import WhereSavedWarn
from components.LogoText import LogoRender
from components.VersionScreen import VersionScreen
from components.ViewRawNotes import RawNotes

from tinydb.storages import JSONStorage
from tinydb.middlewares import CachingMiddleware


# main app class
class Itomori(App):
    """
    This is the main class of our app. This is required to run Textual app.

    :param app - inhertence from the Textual app class
    """

    logger.add(".logs/app.log", rotation="10 MB")

    # css style path
    CSS_PATH = "./style.tcss"

    # keyboard bindings for user
    BINDINGS = [
        ("^q", "quit", "Quit the app"),
        ("v", "show_ver", "Show version and info"),
        ("n", "show_row_notes", "View All Notes"),
    ]

    # main method
    def compose(self) -> ComposeResult:
        """
        This is the main method. This method is to compose Itomori
        """

        joke = pyjokes.get_joke()  # tell user a joke

        yield Header(show_clock=True)  # show the Header with a little clock

        # scrollable container to show all components
        yield ScrollableContainer(
            LogoRender, WelcomeText, WhereSavedWarn, UserNoteInputBox
        )

        yield Label(f"[b grey]{joke}[/b grey]", id="joke")

        yield Footer()  # show footer

    # if any input submitted
    @on(Input.Submitted, "#NoteInputBox")  # anything submitted via note input field
    def handle_tasks(self) -> None:
        """
        This function helps us to receive user's typed input and store them in a json file (notes.json). This json file can keep append every time.
        """

        db = TinyDB("notes.json")
        user_typed_input = self.query_one("#NoteInputBox")  # get user input
        self.user_note = (
            user_typed_input.value.strip()
        )  # get the real value form 'user_typed_input'

        note = self.user_note  # make the note available all over the class

        # get a beautiful date and time to store in the json file
        date_and_time = arrow.now().format("dddd, DD MMMM YYYY - hh:mm A (ZZZ)")

        # id for our note
        id = str(uuid.uuid4())

        # insert the note (with id, time and date)
        db.insert({"ID": id, "Note": note, "Time": date_and_time})

    def action_show_ver(self) -> None:
        """
        This method help us, if user pressed 'v' key in their keyboard then it help us to show the Version component (screen).
        """
        logger.info("User requested for exit the Version modal screen")

        self.push_screen(VersionScreen())  # push the modal screen

    def action_show_row_notes(self) -> None:
        """
        This method help us, if user pressed 'n' key in their keyboard then it help us to show the all saved notes, raw json file.
        """
        logger.info("User requested for exit the Raw notes screen")
        self.push_screen(RawNotes())  # push the screen

    def on_mount(self) -> None:
        """
        This method helps us to when the app run successfully it quickly run these settings or tweaks
        """
        logger.info("Applied quick changes and theme changed")
        # Set the Itomori's default theme
        self.theme: theme = "catppuccin-mocha"


# if the file run directly
if __name__ == "__main__":
    app = Itomori()  # app is 'Itomori' class [main class]
    try:
        logger.info("User requested to run the Itomori")
        app.run()  # try to run the app

    # if any critical error stops us to run the app or anything wrong
    except Exception as Error:
        raise Exception(
            f"Sorry! Something went wrong, it is too critical. Raw error - {Error}"  # give user a friendly messege and also give user user what goes wrong
        )
