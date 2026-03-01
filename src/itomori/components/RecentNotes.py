from textual.widgets import ListItem, Label
from textual.containers import Horizontal
from tinydb import TinyDB
from itomori import DB_PATH


def get_recent_notes():
    """Returns the last 5 notes from the database, with pinned notes first."""
    db = TinyDB(DB_PATH)
    notes = db.all()
    # Sort: Pinned first, then by time (newest first)
    notes.sort(key=lambda x: (x.get("Pinned", False), x.get("Time", "")), reverse=True)
    
    recent_notes = notes[:5]
    
    return [
        ListItem(
            Horizontal(
                Label(f"{'📌 ' if note.get('Pinned', False) else ''}{note['Note']}", classes="recent_note"),
                Label(note["Time"], classes="recent_time"),
            )
        )
        for note in recent_notes
    ]


recent_notes_text = Label("Recent Notes: ", id="recent_notes_text")

