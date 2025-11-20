from textual.screen import ModalScreen
from textual.app import ComposeResult
from textual.widgets import Label
from textual.containers import Container


class RawNotes(ModalScreen[None]):
    BINDINGS = [("escape", "pop_screen")]

    def compose(self) -> ComposeResult:
        with Container(id="ViewRawNotesScreen"):
            with open("./notes.json", "r") as notes:
                all_notes = notes.read()

            yield Label("[b yellow]Press ESC to exit this screen[/b yellow]\n\n\n\n")
            yield Label("[b yellow underline]ALL NOTES : [/b yellow underline]\n\n\n\n")
            yield Label(f"[b green]{all_notes}[/b green]")

    def action_pop_screen(self):
        self.dismiss()
