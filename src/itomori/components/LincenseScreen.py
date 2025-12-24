# SPDX-FileCopyrightText: 2025-present Ahum Maitra theahummaitra@gmail.com
#
# SPDX-License-Identifier: 	GPL-3.0-or-later

#import all necessary Textual subpackage, Container, Screens, Widgets
from textual.app import ComposeResult
from textual.containers import ScrollableContainer
from textual.screen import ModalScreen
from textual.widgets import Label, Footer, Header

# import full license text of `GPL-3.0` license
from itomori.components.LicenseText import license_text

# License Modal Screen
class LicenseScreen(ModalScreen):

    # set bindings
    BINDINGS = [("escape", "pop_screen", "Close License Screen")]

    def compose(self) -> ComposeResult:
        # show header with user's local tie '
        yield Header(show_clock=True)

        # Main container for showing license text
        with ScrollableContainer(id="LicenseScreen"):
            yield Label(f"{license_text}")

        #show footer for keybindings
        yield Footer()

    # if user requested to exit License Modal Screen
    def action_pop_screen(self) -> None:
        """
        This Textual action method helps to exit the modal screen by pressing 'ESC'
        """
        self.dismiss()  # if the action triggered then dismiss the screen
