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
from textual.widgets import Footer, Header, Label, Select, Button

# import loguru for enable and disabling logging
from loguru import logger
from itomori import load_settings, save_settings, LOG_PATH, DB_PATH
from itomori.pages.ConfirmClearLogs import ConfirmClearLogs
from itomori.pages.ConfirmClearNotes import ConfirmClearNotes

#Settings Modal Screen
class Settings(ModalScreen):

    #set keyboard bindings for Settings modal screen
    BINDINGS = [
        ("escape", "escape_screen", "Close Settings Screen"),
        ("c", "clear_logs", "Clear Logs"),
        ("n", "clear_notes", "Clear Notes")
    ]

    #set custom css path ofr Settings modal screen
    CSS_PATH = "../styles/settings.tcss"

    def compose(self) -> ComposeResult:

        # options for user logging preference
        logs_options = ["Enable", "Disable"]

        # options for theme preference
        theme_options = [
            ("Mocha (Default)", "catppuccin-mocha"),
            ("Latte", "catppuccin-latte"),
            ("Nord", "nord"),
            ("Dracula", "dracula"),
            ("Monokai", "monokai"),
            ("Tokyo Night", "tokyo-night"),
            ("Textual Dark", "textual-dark"),
            ("Textual Light", "textual-light"),
            ("Rose Pine", "rose-pine"),
            ("Rose Pine (Moon)", "rose-pine-moon"),
            ("Rose Pine (Dawn)", "rose-pine-dawn"),
            ("Atom One Light","atom-one-light"),
            ("Solarized Light", "solarized-light"),
            ("Your Name", "your-name-theme"),
            ("Flexoki","flexoki")
        ]
        
        # options for startup text preference
        startup_options = [
            ("Jokes (Default)", "jokes"),
            ("John Wick Quotes", "quotes"),
            ("Disabled", "disabled")
        ]

        # current settings
        self.settings = load_settings()
        current_logs = "Enable" if self.settings.get("logs", True) else "Disable"
        current_theme = self.settings.get("theme", "catppuccin-mocha")
        current_startup = self.settings.get("startup_text", "jokes")

        # show default app header with user's local time
        yield Header()

        # main scrollable container
        yield ScrollableContainer(

            #logging settings container
            Container(
                Label("Logs", id="logs_text"), Select.from_values(logs_options, value=current_logs),

                #label for showing success message, user did `enabled` or disabled` logging
                Label("", id="log_status"),
                id="logs_container"
            ),

            #theme settings container
            Container(
                Label("Theme", id="theme_text"), Select(theme_options, value=current_theme, id="theme_select"),
                Label("", id="theme_status"),
                id="theme_container"
            ),

            #startup text settings container
            Container(
                Label("Startup Text", id="startup_text_label"), Select(startup_options, value=current_startup, id="startup_select"),
                Label("", id="startup_status"),
                id="startup_container"
            ),
            Label("Settings are applied permanently!", id="not"), #inform users that settings are applied permanently
            Container(
                Label("Danger Zone", id="danger_text"),
                Button("Clear All Logs", variant="error", id="clear_logs_btn"),
                Button("Clear All Notes", variant="error", id="clear_notes_btn"),
                Label("", id="clear_status"),
                id="danger_container"
            )
            )

        yield Footer() #show footer, for showing bindings

    #for logging preference
    @on(Select.Changed)
    def select_changed(self, event: Select.Changed) -> None:
        if event.select.id == "theme_select":
            self.theme_changed(event)
            return
        
        if event.select.id == "startup_select":
            self.startup_changed(event)
            return

        option = str(event.value)

        match option:
            #if user selected `Enabled`
            case "Enable":
               self.query_one("#log_status", Label).update("Logs are enabled!") #inform user about their preference
               logger.enable("itomori") #enable logging for `itomori` package
               self.settings["logs"] = True
               
            # if user selected `Disabled`
            case "Disable":
                self.query_one("#log_status", Label).update("Logs are disabled!") #inform user about their preference
                logger.disable("itomori") #disable logging for `itomori` package
                self.settings["logs"] = False
        
        save_settings(self.settings)

    def theme_changed(self, event: Select.Changed) -> None:
        theme_name = str(event.value)
        self.app.theme = theme_name
        self.settings["theme"] = theme_name
        save_settings(self.settings)
        self.query_one("#theme_status", Label).update(f"Theme changed to {theme_name}!")

    def startup_changed(self, event: Select.Changed) -> None:
        startup_option = str(event.value)
        self.settings["startup_text"] = startup_option
        save_settings(self.settings)
        
        status_msg = {
            "jokes": "Startup text changed to Jokes!",
            "quotes": "Startup text changed to John Wick Quotes!",
            "disabled": "Startup text disabled!"
        }.get(startup_option, "Startup text changed!")
        
        self.query_one("#startup_status", Label).update(status_msg)
        
        # Trigger an immediate update if the app has the method
        if hasattr(self.app, "update_joke"):
            self.app.update_joke()

    @on(Button.Pressed, "#clear_logs_btn")
    def action_clear_logs(self) -> None:
        def check_confirm(confirm: bool) -> None:
            if confirm:
                try:
                    LOG_PATH.write_text("")
                    self.query_one("#clear_status", Label).update("Logs cleared successfully!")
                    logger.info("Logs cleared by user from Settings")
                except Exception as e:
                    self.query_one("#clear_status", Label).update(f"Error: {e}")
        
        self.app.push_screen(ConfirmClearLogs(), check_confirm)

    @on(Button.Pressed, "#clear_notes_btn")
    def action_clear_notes(self) -> None:
        def check_confirm(confirm: bool) -> None:
            if confirm:
                try:
                    DB_PATH.write_text("")
                    self.query_one("#clear_status", Label).update("Notes cleared successfully!")
                    logger.info("Notes cleared by user from Settings")
                    self.refresh_main_notes()
                except Exception as e:
                    self.query_one("#clear_status", Label).update(f"Error: {e}")
        
        self.app.push_screen(ConfirmClearNotes(), check_confirm)

    def refresh_main_notes(self) -> None:
        # Refresh recent notes if on main screen
        try:
            from itomori.components.RecentNotes import get_recent_notes
            from textual.widgets import ListView
            notes_list = self.app.query_one("#notes_list", ListView)
            notes_list.clear()
            for item in get_recent_notes():
                notes_list.append(item)
        except Exception:
            pass

    #if user requested to escape Settings
    def action_escape_screen(self) -> None:
        self.dismiss() #dismiss this modal screen
