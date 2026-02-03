# SPDX-FileCopyrightText: 2025-present Ahum Maitra theahummaitra@gmail.com
#
# SPDX-License-Identifier: 	GPL-3.0-or-later

# import all necessary textual subpackage
from textual.app import ComposeResult
from textual import on

#import all required containers
from textual.containers import ScrollableContainer, Container
from textual.screen import ModalScreen

# import all required widgets
from textual.widgets import Footer, Header, Label, Select

# import loguru for enable and disabling logging
from loguru import logger

#Settings Modal Screen
class Settings(ModalScreen):

    #set keyboard bindings for Settings modal screen
    BINDINGS = [("escape", "escape_screen", "Close Settings Screen")]

    #set custom css path ofr Settings modal screen
    CSS_PATH = "../styles/settings.tcss"

    def compose(self) -> ComposeResult:

        # options for user logging preference
        logs_options = ["Enable", "Disable"]

        # show default app header with user's local time
        yield Header()

        # main scrollable container
        yield ScrollableContainer(

            #logging settings container
            Container(
                Label("Logs", id="logs_text"), Select.from_values(logs_options),

                #label for showing success message, user did `enabled` or disabled` logging
                Label("", id="log_status"),
            ),
            Label("Settings are applied locally, temporary!", id="not") #inform users that settings are applied locally only for yet
            )

        yield Footer() #show footer, for showing bindings

    #for logging preference
    @on(Select.Changed)
    def select_changed(self, event: Select.Changed) -> None:
        option = str(event.value)

        match option:
            #if user selected `Enabled`
            case "Enable":
               self.query_one("#log_status", Label).update("Logs are enabled!") #inform user about their preference
               
            # if user selected `Disabled`
            case "Disable":
                self.query_one("#log_status", Label).update("Logs are disabled!") #inform user about their preference
                logger.disable("itomori") #disable logging for `itomori` package

    #if user requested to escape Settings
    def action_escape_screen(self) -> None:
        self.dismiss() #dismiss this modal screen
