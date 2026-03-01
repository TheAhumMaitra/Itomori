from textual.app import ComposeResult
from textual.containers import Grid
from textual.screen import ModalScreen
from textual.widgets import Button, Label, Input
from itomori import DB_PATH
from tinydb import TinyDB, Query

class EditNote(ModalScreen[str | None]):
    """A modal screen for editing a note's text."""

    BINDINGS = [("escape", "cancel", "Cancel editing")]

    def __init__(self, note_text: str, note_id: str):
        super().__init__()
        self.note_text = note_text
        self.note_id = note_id

    def compose(self) -> ComposeResult:
        yield Grid(
            Label("Edit Note:", id="edit_label"),
            Input(value=self.note_text, id="edit_input"),
            Button("Save", variant="primary", id="save_btn"),
            Button("Cancel", variant="error", id="cancel_btn"),
            id="edit_dialog",
        )

    def on_mount(self) -> None:
        self.query_one("#edit_input", Input).focus()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "save_btn":
            new_text = self.query_one("#edit_input", Input).value
            if new_text and new_text != self.note_text:
                self.save_note(new_text)
                self.dismiss(new_text)
            else:
                self.dismiss(None)
        elif event.button.id == "cancel_btn":
            self.dismiss(None)

    def on_input_submitted(self, event: Input.Submitted) -> None:
        new_text = event.value
        if new_text and new_text != self.note_text:
            self.save_note(new_text)
            self.dismiss(new_text)
        else:
            self.dismiss(None)

    def save_note(self, new_text: str) -> None:
        # extract tags (starting with #) from the note
        tags = [word.lstrip("#") for word in new_text.split() if word.startswith("#")]
        db = TinyDB(DB_PATH)
        db.update({"Note": new_text, "Tags": tags}, Query().ID == self.note_id)

    def action_cancel(self) -> None:
        self.dismiss(None)
