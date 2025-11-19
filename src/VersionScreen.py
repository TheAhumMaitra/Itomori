from textual.screen import ModalScreen
from textual.app import ComposeResult
from textual.widgets import Label
from textual.containers import Container

class VersionScreen(ModalScreen[None]):
    BINDINGS = [("escape", "pop_screen")]
    CSS_PATH = "./style.tcss"

    def compose(self) -> ComposeResult:
        with Container(id="VersionScreen"):
           yield Label("[b]Itomori v1.0.0[/b]")
           yield Label("[italic bold]Author : Ahum Maitra[italic bold]")
           yield Label("[yellow bold]Github link : [underline]https://github.com/TheAhumMaitra/Itomori[/underline][yellow bold]")
           yield Label("Press [b]ESC[/b] to exit this screen.")

    def action_pop_screen(self):
        self.dismiss()
