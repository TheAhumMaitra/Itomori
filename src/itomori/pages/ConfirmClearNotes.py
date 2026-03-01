import subprocess

from textual.app import ComposeResult
from textual.containers import Grid
from textual.screen import ModalScreen
from textual.widgets import Button, Label
from loguru import logger

class ConfirmClearNotes(ModalScreen[bool]):
    """A confirmation dialog for clearing notes"""
    
    BINDINGS = [("escape", "cancel", "Escape the confirmation screen")]

    def compose(self) -> ComposeResult:
        yield Grid(
            Label("Are you sure you want to clear all notes?", id="question"),
            Button("Yes", variant="error", id="yes"),
            Button("No", variant="primary", id="no"),
            id="dialog",
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "yes":
            subprocess.run(["Itomori", "--clearnotes"])
            self.dismiss(True)
        elif event.button.id == "no":
            logger.info("User requested to cancel the note clearing")
            self.dismiss(False)

    def action_cancel(self) -> None:
        self.dismiss(False)
