#   Copyright (C) 2025  Ahum Maitra

#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.

#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.

#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>



from textual.app import ComposeResult
from textual.containers import ScrollableContainer
from textual.screen import ModalScreen
from textual.widgets import Label

from components.LicenseText import license_text


class LicenseScreen(ModalScreen):
    BINDINGS: list[tuple(str)] = [("escape", "pop_screen")]

    # css link
    CSS_PATH: str = "../style.tcss"

    def compose(self) -> ComposeResult:
        with ScrollableContainer(id="LicenseScreen"):
            yield Label(f"{license_text}")

    def action_pop_screen(self) -> None:
        """
        This Textual action method helps to exit the modal screen by pressing 'ESC'
        """
        self.dismiss()  # if the action triggered then dismiss the screen
