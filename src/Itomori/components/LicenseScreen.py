# SPDX-FileCopyrightText: 2025-present Ahum Maitra theahummaitra@gmail.com
#
# SPDX-License-Identifier: 	GPL-3.0-or-later


from textual.app import ComposeResult
from textual.containers import ScrollableContainer
from textual.screen import ModalScreen
from textual.widgets import Label

from Itomori.components.LicenseText import license_text

class LicenseScreen(ModalScreen):
    BINDINGS = [("escape", "pop_screen")]


    def compose(self) -> ComposeResult:
        with ScrollableContainer(id="LicenseScreen"):
            yield Label(f"{license_text}")

    def action_pop_screen(self) -> None:
        """
        This Textual action method helps to exit the modal screen by pressing 'ESC'
        """
        self.dismiss()  # if the action triggered then dismiss the screen
