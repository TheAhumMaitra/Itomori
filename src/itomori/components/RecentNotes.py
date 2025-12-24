from textual.widgets import ListItem, Label
from tinydb import TinyDB


notes = TinyDB("./notes.json").all()[-5:]  # last 5 notes
recent_notes_text = Label("Recent Notes: ", id="recent_notes_text")
items = [ListItem(Label(note["Note"])) for note in notes]

