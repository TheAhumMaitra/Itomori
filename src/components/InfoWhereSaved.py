# all necessary Textual widgets
from textual.widgets import Label

"""
This file is a component, which is just helps to give user a info where the notes are saved in.
"""

WhereSavedWarn: Label = Label(
    "All Notes are saved in ../Itomori/src/notes.json", id="WhereSavedNotesWarn"
)
