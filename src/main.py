from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Input
from textual.containers import ScrollableContainer
import uuid  # to genrate id
import json
from datetime import datetime

# All components
from components.WelcomeTextRender import WelcomeText
from components.AddNoteInputBox import UserNoteInputBox
from textual import on
from datetime import datetime as time
from components.InfoWhereSaved import WhereSavedWarn
from components.LogoText import LogoRender
from components.VersionScreen import VersionScreen
from components.ViewRawNotes import RawNotes


class Itomori(App):
    CSS_PATH = "./style.tcss"
    BINDINGS = [
        ("^q", "quit", "Quit the app"),
        ("v", "show_ver", "Show version and info"),
        ("n", "show_row_notes", "View All Notes"),
    ]

    @on(Input.Submitted, "#NoteInputBox")
    def handle_tasks(self) -> None:
        user_typed_input = self.query_one("#NoteInputBox")
        self.user_note = user_typed_input.value.strip()
        note = self.user_note
        notes = {
            "ID": str(uuid.uuid4()),
            "Time": datetime.now().isoformat(),
            "Task Text": note,
        }

        # Write note to file
        with open("notes.json", "a") as notesfile:
            notesfile.write(json.dumps(notes) + "\n")

    def compose(self) -> ComposeResult:
        yield Header()

        yield ScrollableContainer(
            LogoRender, WelcomeText, WhereSavedWarn, UserNoteInputBox
        )

        yield Footer()

    def action_show_ver(self) -> None:
        self.push_screen(VersionScreen())

    def action_show_row_notes(self) -> None:
        self.push_screen(RawNotes())


if __name__ == "__main__":
    app = Itomori()
    app.run()
