# SPDX-FileCopyrightText: 2025-present Ahum Maitra theahummaitra@gmail.com
#
# SPDX-License-Identifier: 	GPL-3.0-or-later


# all necessary Textual widgets, screens, containers
from textual.screen import ModalScreen
from textual.app import ComposeResult
from textual.widgets import Label
from textual.containers import Container
from Itomori.components.LicenseScreen import LicenseScreen
from Itomori import __version__

"""
This file is a component, which is just helps to render the version screen.
"""


class AboutScreen(ModalScreen[None]):
    """
    This class render the About Modal Screen.

    :param ModalScreen[None] - it inherit from the Textual Modal Screen
    """

    # keyboard bindings for this modal screen
    BINDINGS = [("escape", "pop_screen"), ("l", "show_license", "Show License info")]

    # css link
    CSS_PATH: str = "../style.tcss"

    def compose(self) -> ComposeResult:
        """
        Main Textaul compose function to render the About Modal Screen
        """
        with Container(id="AboutScreen"):
            """
            Main container for the Version Modal Screen
            """
            # All labels
            yield Label(f"[b]Itomori v{__version__}[/b]")  # Itmori current version
            yield Label(
                "[italic bold]Author : Ahum Maitra[italic bold]"
            )  # My name as author

            # Github link label to show the github link
            yield Label(
                "[yellow bold]Github link : [underline]https://github.com/TheAhumMaitra/Itomori[/underline][yellow bold]"
            )

            # An info, how to exit this modal screen
            yield Label("Press [b]ESC[/b] to exit this screen.")
            yield Label("[b underline green]Press `L` to view License info[/b underline green]")

    def action_pop_screen(self) -> None:
        """
        This Textual action method helps to exit the modal screen by pressing 'ESC'
        """
        self.dismiss()  # if the action triggered then dismiss the screen

    def action_show_license(self):
        self.app.push_screen(LicenseScreen())


