# SPDX-FileCopyrightText: 2025-present Ahum Maitra theahummaitra@gmail.com
#
# SPDX-License-Identifier: 	GPL-3.0-or-later


# Necessary Textual components and widgets
import time

# to write logs
from loguru import logger
from rich import box

# To view the table
from rich.table import Table
from textual import on
from textual.app import ComposeResult
from textual.containers import ScrollableContainer, Horizontal
from textual.screen import ModalScreen
from textual.widgets import Footer, Label, Static, Header, Input, ListView, ListItem
from tinydb import TinyDB, Query


from itomori.pages.EditNote import EditNote
from itomori import DB_PATH

class NoteItem(ListItem):
    """Custom ListItem for notes that stores the note ID."""
    def __init__(self, note: dict):
        self.pinned = note.get("Pinned", False)
        pin_indicator = "📌 " if self.pinned else ""
        super().__init__(
            Horizontal(
                Label(f"{pin_indicator}{note.get('Note', '')}", classes="note_column", id=f"note_label_{note.get('ID')}"),
                Label(note.get("Time", ""), classes="time_column"),
            )
        )
        self.note_id = note.get("ID")
        self.note_text = note.get("Note", "")
        self.note_time = note.get("Time", "")

    def update_text(self, new_text: str):
        self.note_text = new_text
        pin_indicator = "📌 " if self.pinned else ""
        self.query_one(f"#note_label_{self.note_id}", Label).update(f"{pin_indicator}{new_text}")

    def toggle_pin(self):
        self.pinned = not self.pinned
        pin_indicator = "📌 " if self.pinned else ""
        self.query_one(f"#note_label_{self.note_id}", Label).update(f"{pin_indicator}{self.note_text}")
        db = TinyDB(DB_PATH)
        db.update({"Pinned": self.pinned}, Query().ID == self.note_id)

class RawNotes(ModalScreen[None]):
    """
    This widget helps users to see all raw json file notes.
    """

    # keyboard bindings for the modal screen
    BINDINGS = [
        ("escape", "pop_screen", "Exit Notes Screen"),
        ("d", "delete_note", "Delete Selected Note"),
        ("e", "edit_note", "Edit Selected Note"),
        ("p", "toggle_pin", "Pin/Unpin Selected Note"),
        ("c", "copy_note", "Copy Selected Note"),
        ("x", "export_notes", "Export All Notes to Markdown")
    ]

    def compose(self) -> ComposeResult:
        """
        Main method for this widget
        """
        yield Header(show_clock=True)
        # read the json file
        with ScrollableContainer(id="ViewRawNotesScreen"):
            yield Label("[b underline] All Notes : [/b underline]\n\n", id="all_notes_text")
            yield Input(placeholder="Search notes...", id="search_input")
            # Label for showing search status (no matches)
            yield Label("", id="search_status")
            
            # Header for our fake table
            yield Horizontal(
                Label("[b]Note[/b]", classes="table_header_note"),
                Label("[b]Time[/b]", classes="table_header_time"),
                id="notes_table_header"
            )

            yield ListView(id="notes_list_view")

        yield Footer()

    def on_mount(self) -> None:
        self.populate_list()

    def populate_list(self) -> None:
        list_view = self.query_one("#notes_list_view", ListView)
        list_view.clear()
        
        db = TinyDB(DB_PATH)
        notes = db.all()
        
        if not notes:
            list_view.mount(ListItem(Label("No notes found!", classes="empty_table_label")))
            return

        # Sort: Pinned first, then by time (newest first)
        notes.sort(key=lambda x: (x.get("Pinned", False), x.get("Time", "")), reverse=True)

        seen_ids = set()
        new_items = []
        for note in notes:
            note_id = note.get("ID")
            if not note_id or note_id in seen_ids:
                continue
            seen_ids.add(note_id)
            new_items.append(NoteItem(note))
        
        if new_items:
            list_view.mount_all(new_items)
            self.query_one("#search_status", Label).update("")

    def update_list(self, search_term: str = "") -> None:
        list_view = self.query_one("#notes_list_view", ListView)
        search_term = search_term.lower()
        
        count = 0
        for item in list_view.query(NoteItem):
            matches = search_term in item.note_text.lower() or search_term in item.note_time.lower()
            item.display = matches
            if matches:
                count += 1
        
        if count == 0 and search_term:
             self.query_one("#search_status", Label).update("No matches found!")
        else:
             self.query_one("#search_status", Label).update("")

    @on(Input.Changed, "#search_input")
    def on_search(self, event: Input.Changed) -> None:
        self.update_list(event.value)

    def action_delete_note(self) -> None:
        list_view = self.query_one("#notes_list_view", ListView)
        if list_view.index is None:
            return
            
        selected_item = list_view.highlighted_child
        if not isinstance(selected_item, NoteItem):
            return
            
        note_id = selected_item.note_id
        
        db = TinyDB(DB_PATH)
        db.remove(Query().ID == note_id)
        
        logger.info(f"Deleted note with ID: {note_id}")
        
        # Remove from UI immediately
        selected_item.remove()
        
        # Check if list is empty now
        if not list_view.query(NoteItem):
             list_view.mount(ListItem(Label("No notes found!", classes="empty_table_label")))
        else:
             self.query_one("#search_status", Label).update("[b green]Note deleted![/b green]")

    def action_edit_note(self) -> None:
        list_view = self.query_one("#notes_list_view", ListView)
        if list_view.index is None:
            return
            
        selected_item = list_view.highlighted_child
        if not isinstance(selected_item, NoteItem):
            return
            
        def handle_edit(new_text: str | None) -> None:
            if new_text:
                selected_item.update_text(new_text)
                self.query_one("#search_status", Label).update("[b green]Note updated![/b green]")
                logger.info(f"Edited note with ID: {selected_item.note_id}")

        self.app.push_screen(EditNote(selected_item.note_text, selected_item.note_id), handle_edit)

    def action_toggle_pin(self) -> None:
        list_view = self.query_one("#notes_list_view", ListView)
        if list_view.index is None:
            return
            
        selected_item = list_view.highlighted_child
        if not isinstance(selected_item, NoteItem):
            return
            
        selected_item.toggle_pin()
        status = "pinned" if selected_item.pinned else "unpinned"
        self.query_one("#search_status", Label).update(f"[b green]Note {status}![/b green]")
        logger.info(f"Toggled pin for note ID: {selected_item.note_id} (New status: {status})")
        
        # Refresh the list to apply sorting
        self.populate_list()

    def action_copy_note(self) -> None:
        list_view = self.query_one("#notes_list_view", ListView)
        if list_view.index is None:
            return
            
        selected_item = list_view.highlighted_child
        if not isinstance(selected_item, NoteItem):
            return
            
        note_text = selected_item.note_text
        try:
            self.app.copy_to_clipboard(note_text)
            self.query_one("#search_status", Label).update("[b green]Note copied to clipboard![/b green]")
            logger.info(f"Copied note with ID: {selected_item.note_id} to clipboard")
        except Exception as e:
            self.query_one("#search_status", Label).update(f"[b red]Copy failed: {e}[/b red]")
            logger.error(f"Copy failed: {e}")

    def action_export_notes(self) -> None:
        db = TinyDB(DB_PATH)
        notes = db.all()
        
        if not notes:
            self.query_one("#search_status", Label).update("[b red]No notes to export![/b red]")
            return
            
        import arrow
        from pathlib import Path
        
        # Sort notes for export (Pinned first, then time)
        notes.sort(key=lambda x: (x.get("Pinned", False), x.get("Time", "")), reverse=True)
        
        filename = f"Itomori_Notes_{arrow.now().format('YYYY-MM-DD')}.md"
        export_path = Path.home() / filename
        
        try:
            with open(export_path, "w", encoding="utf-8") as f:
                f.write("# Itomori Notes : \n\n")
                f.write(f"Generated on: {arrow.now().format('YYYY-MM-DD HH:mm:ss')}\n\n")
                
                for note in notes:
                    pin_marker = "📌 " if note.get("Pinned", False) else ""
                    f.write(f"### {pin_marker}{note.get('Time', 'Unknown Time')}\n")
                    f.write(f"{note.get('Note', '')}\n\n")
                    tags = note.get("Tags", [])
                    if tags:
                        f.write(f"*Tags: {', '.join(tags)}*\n\n")
                    f.write("---\n\n")
            
            self.query_one("#search_status", Label).update(f"[b green]Exported to ~/{filename}[/b green]")
            logger.info(f"Exported notes to {export_path}")
        except Exception as e:
            self.query_one("#search_status", Label).update(f"[b red]Export failed: {e}[/b red]")
            logger.error(f"Export failed: {e}")

    def action_pop_screen(self):
        """
        method helps to dismiss the modal screen
        """
        self.dismiss()
