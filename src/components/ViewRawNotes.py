# Necessary Textual components and widgets
from textual.screen import ModalScreen
from textual.app import ComposeResult
from textual.widgets import Label
from textual.containers import Container

class RawNotes(ModalScreen[None]):

    """
    This widget helps users to see all raw json file notes.
    """

    #keyboard bindings for the modal screen
    BINDINGS = [("escape", "pop_screen")]

    def compose(self) -> ComposeResult:
        """
        Main method for this widget
        """

        #read the json file
        with Container(id="ViewRawNotesScreen"):
            with open("./notes.json", "r") as notes:
                all_notes = notes.read()

            #all labels
            yield Label("[b yellow]Press ESC to exit this screen[/b yellow]\n\n\n\n")
            yield Label("[b yellow underline]ALL NOTES : [/b yellow underline]\n\n\n\n")

            # check notes are empty or not
            if (notes := str(all_notes)) == "":
                yield Label("[b blue]Nothing in here![/b blue]")
            else:
                yield Label(f"[b pink]{notes}[/b pink]")

    def action_pop_screen(self):
        """
        method helps to dismiss the modal screen
        """
        self.dismiss()
