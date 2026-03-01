import asyncio
from itomori.components.ViewRawNotes import RawNotes
from textual.app import App

class TestApp(App):
    def on_mount(self):
        self.push_screen(RawNotes())

if __name__ == "__main__":
    # Just checking imports and basic structure
    print("Imports OK")
