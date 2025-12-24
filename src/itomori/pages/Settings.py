from textual.app import ComposeResult
from textual.containers import ScrollableContainer, Container
from textual.screen import ModalScreen
from textual.widgets import Footer, Header, Label, Select
from textual import on

class Settings(ModalScreen):
    BINDINGS = [("escape", "escape_screen", "Close Settings Screen")]
    CSS_PATH = "../styles/settings.tcss"

    def compose(self) -> ComposeResult:
        logs_options = ["Enable", "Disable"]

        yield Header()
        yield ScrollableContainer(
            Container(
                Label("Logs", id="logs_text"), Select.from_values(logs_options),
                Label("", id="log_status"),
            ),
            Label("Settings are unavailable! Please wait for settings to come!", id="not")
            )

        yield Footer()
    @on(Select.Changed)
    def select_changed(self, event: Select.Changed) -> None:
        option = str(event.value)

        match option:
            case "Enable":
               self.query_one("#log_status", Label).update("Logs are enabled!")
            case "Disable":
                self.query_one("#log_status", Label).update("Logs are disabled!")


    def action_escape_screen(self) -> None:
        self.dismiss()
