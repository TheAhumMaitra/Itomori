# Necessary Textual components and widgets
import time
from textual.screen import ModalScreen
from textual.app import ComposeResult
from textual.widgets import Label
from textual.containers import Container
from tinydb import TinyDB
from tabulate import tabulate


class RawNotes(ModalScreen[None]):
    """
    This widget helps users to see all raw json file notes.
    """

    # keyboard bindings for the modal screen
    BINDINGS = [("escape", "pop_screen")]

    def compose(self) -> ComposeResult:
        """
        Main method for this widget
        """

        # read the json file
        with Container(id="ViewRawNotesScreen"):
            try:
                Database = TinyDB("./notes.json")
                all_notes = tabulate(Database.all(), headers="keys", tablefmt="grid")

            except FileNotFoundError as FileError:
                yield Label(
                    f"[b red]File not found, ERROR={FileError}! The app will close in 5 seconds[/b red]"
                )
                time.sleep(5)
                raise FileNotFoundError("THe 'notes.json' file is not here!")

            except Exception as UnexpectedError:
                yield Label(
                    f"[b red]Unexpected error - {UnexpectedError}! The app will close in 5 seconds[/b red]"
                )
                time.sleep(5)
                raise Exception(
                    f"Something is wrong! Unexpected error - {UnexpectedError}"
                )

            # all labels
            yield Label("[b yellow]Press ESC to exit this screen[/b yellow]\n\n\n\n")
            yield Label("[b yellow underline]ALL NOTES : [/b yellow underline]\n\n\n\n")

            # check notes are empty or not
            if (notes := len(Database)) == 0:
                yield Label("[b blue]Nothing in here![/b blue]")
            else:
                yield Label(f"[b pink]{all_notes}[/b pink]")

    def action_pop_screen(self):
        """
        method helps to dismiss the modal screen
        """
        self.dismiss()
