from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Input
from textual.containers import ScrollableContainer
import uuid
# All components
from WelcomeTextRender import WelcomeText
from AddNoteInputBox import UserNoteInputBox
from textual import on
from datetime import datetime as time
from InfoWhereSaved import WhereSavedWarn
from LogoText import LogoRender
from VersionScreen import VersionScreen
from ViewRawNotes import RawNotes

class Itomori(App):
    CSS_PATH = "./style.tcss"
    BINDINGS = [("^q", "quit", "Quit the app"), ("v", "show_ver", "Show version and info"), ("n", "show_row_notes", "View All Notes")]

    @on(Input.Submitted, "#NoteInputBox")
    def handle_tasks(self) -> None:
        user_typed_input = self.query_one("#NoteInputBox")
        self.user_note = user_typed_input.value.strip()

        # Write note to file
        with open("notes.txt", "a") as notes:
            notes.write("\n\n" + f"ID : {uuid.uuid4()}" + "Task Text : \n\n" + self.user_note + f"\tTime:{time.now()}\n")



    def compose(self) -> ComposeResult:
        yield Header()

        yield ScrollableContainer(
            LogoRender,
            WelcomeText,
            WhereSavedWarn,
            UserNoteInputBox
        )

        yield Footer()

    def action_show_ver(self) -> None:
        self.push_screen(VersionScreen())

    def action_show_row_notes(self) -> None:
        self.push_screen(RawNotes())

if __name__ == "__main__":
    app = Itomori()
    app.run()
