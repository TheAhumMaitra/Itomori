# SPDX-FileCopyrightText: 2025-present Ahum Maitra theahummaitra@gmail.com
#
# SPDX-License-Identifier: 	GPL-3.0-or-later

# all necessary Textual subpackage, widgets, screens, containers
from textual.screen import ModalScreen
from textual.app import ComposeResult
from textual.widgets import Label, Footer, Header
from textual.containers import Container

#import License modal screen component
from itomori.pages.LincenseScreen import LicenseScreen

# import current Itomori version
from itomori import __version__

"""
About Page
"""

#About modal screen
class AboutScreen(ModalScreen[None]):
    """
    This class render the About Modal Screen.

    :param ModalScreen[None] - it inherit from the Textual Modal Screen
    """

    # keyboard bindings for this modal screen
    BINDINGS = [("escape", "pop_screen", "Escape about screen"), ("l", "show_license", "Show License info")]

    # set css file
    CSS_PATH: str = "../style.tcss"

    def compose(self) -> ComposeResult:
        """
        Main Textual compose function to render the About Modal Screen
        """

        yield Header(show_clock=True) #show default header with user's local time

        # main container for showing details
        with Container(id="AboutScreen"):
            """
            Main container for the Version Modal Screen
            """
            yield Label(f"[b]Itomori v{__version__}[/b]")  # Show Itomori's current version
            yield Label(
                "[italic bold]Creator : Ahum Maitra[italic bold]"
            )  # My name as creator

            #Show Github repository link
            yield Label(
                "[yellow bold]Github link : [underline]https://github.com/TheAhumMaitra/Itomori[/underline][yellow bold]"
            )

            # inform user, how to see `GPL-3.0-or-later` full license text
            yield Label("[b underline green]Press `L` to view License info[/b underline green]")

        #show footer
        yield Footer()

    # if user requested exit About modal screen
    def action_pop_screen(self) -> None:
        """
        This Textual action method helps to exit the modal screen by pressing 'ESC'
        """
        self.dismiss()  # if the action triggered then dismiss the screen

    # if user requested to see full license text
    def action_show_license(self):
        self.app.push_screen(LicenseScreen()) #then push `License` screen
