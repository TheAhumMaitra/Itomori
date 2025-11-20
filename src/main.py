"""
Main python file to render Itomori
"""

# import all nesseary libaries or modules

# Textual nesseary imports
from textual.app import App, ComposeResult

# import nesseary textual widgets
from textual.widgets import Header, Footer, Input

# import containers for textual app
from textual.containers import ScrollableContainer

# import other modules or libaries
import uuid  # to genrate id
import json  # to add notes and view notes
from datetime import datetime  # to get current time and date
from textual import on  # to intereact with user

# All components
from components.WelcomeTextRender import WelcomeText
from components.AddNoteInputBox import UserNoteInputBox
from components.InfoWhereSaved import WhereSavedWarn
from components.LogoText import LogoRender
from components.VersionScreen import VersionScreen
from components.ViewRawNotes import RawNotes


# main app class
class Itomori(App):
    """
    This is the main class of our app. This is required to run Textual app.

    :param app - inhertence from the Textual app class
    """

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
        yield Header(show_clock=True)  # show the Header with a liitle clcok

        # scrollable container to show all components
        yield ScrollableContainer(
            LogoRender, WelcomeText, WhereSavedWarn, UserNoteInputBox
        )

        yield Footer()  # show footer

    # if any input submiited
    @on(Input.Submitted, "#NoteInputBox")  # anything sumbitted via note input
    def handle_tasks(self) -> None:
        """
        This function helps us to recive user's typed input and store them in a json file (notes.json). This json file can keep append every time.
        """
        user_typed_input = self.query_one("#NoteInputBox")  # get user input
        self.user_note = (
            user_typed_input.value.strip()
        )  # get the real value form 'user_typed_input'

        note = self.user_note  # make the note avaliable all over the class

        # get a beautiful date and time to store in the json file
        date_and_time = (
            datetime.now().astimezone().strftime("%A, %d %B %Y - %I:%M %p (%Z)")
        )

        # notes dictionary to store and orgainze random note id, note and time and date for that
        notes = {
            "ID": str(uuid.uuid4()),
            "Time": date_and_time,
            "Task Text": note,
        }

        # Write the user's note to file
        with open("notes.json", "a") as notesfile:
            notesfile.write(json.dumps(notes) + "\n")

    def action_show_ver(self) -> None:
        """
        This method help us, if user pressed 'v' key in thir keyboard then it help us to show the Version component (screen).
        """
        self.push_screen(VersionScreen())  # psuh the modal screen

    def action_show_row_notes(self) -> None:
        """
        This method help us, if user pressed 'n' key in thir keyboard then it help us to show the all saved notes, raw json file.
        """
        self.push_screen(RawNotes())  # psuh the screen

    def on_mount(self) -> None:
        """
        This method helps us to when the app run succesfully it quicly run these settings or tweaks
        """
        # Set the Itomori's default theme
        self.theme: theme = "catppuccin-mocha"


# if the file run directly
if __name__ == "__main__":
    app = Itomori()  # app is 'Itomori' class [main class]
    try:
        app.run()  # try to run the app
    # if any critical error stops us to run the app or anything wrong
    except Exception as Error:
        raise Exception(
            f"Sorry! Something went wrong, it is too critical. Raw error - {Error}"
        )
