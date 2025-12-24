# SPDX-FileCopyrightText: 2025-present Ahum Maitra theahummaitra@gmail.com
#
# SPDX-License-Identifier: 	GPL-3.0-or-later


from textual.app import ComposeResult
from textual.containers import ScrollableContainer
from textual.screen import ModalScreen
from textual.widgets import Label, Footer, Header

from itomori.components.LicenseText import license_text

class LicenseScreen(ModalScreen):
    BINDINGS = [("escape", "pop_screen", "Close License Screen")]


    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        
        with ScrollableContainer(id="LicenseScreen"):
            yield Label(f"{license_text}")

        yield Footer()

    def action_pop_screen(self) -> None:
        """
        This Textual action method helps to exit the modal screen by pressing 'ESC'
        """
        self.dismiss()  # if the action triggered then dismiss the screen
