# all necessary Textual widgets, screens, containers
from textual.screen import ModalScreen
from textual.app import ComposeResult
from textual.widgets import Label
from textual.containers import Container

"""
This file is a component, which is just helps to render the version screen.
"""


class VersionScreen(ModalScreen[None]):
    """
    This class render the 'VersionSceen' Modal Screen.

    :param ModalScreen[None] - it inherit from the Textual Modal Screen
    """

    # keyboard bindings for this modal screen
    BINDINGS: list[tuple(str)] = [("escape", "pop_screen")]

    # css link
    CSS_PATH: str = "../style.tcss"

    def compose(self) -> ComposeResult:
        """
        Main Textaul compose function to render the Version MOdal Screen
        """
        with Container(id="VersionScreen"):
            """
            Main container for the Version Modal Screen
            """
            # All labels
            yield Label("[b]Itomori v1.0.0[/b]")  # Itmori current version
            yield Label(
                "[italic bold]Author : Ahum Maitra[italic bold]"
            )  # My name as author

            # Github link label to show the github link
            yield Label(
                "[yellow bold]Github link : [underline]https://github.com/TheAhumMaitra/Itomori[/underline][yellow bold]"
            )

            # An info, how to exit this modal screen
            yield Label("Press [b]ESC[/b] to exit this screen.")

    def action_pop_screen(self) -> None:
        """
        This Textual action method helps to exit the modal screen by pressing 'ESC'
        """
        self.dismiss()  # if the action triggered then dismiss the screen
