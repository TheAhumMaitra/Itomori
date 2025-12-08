# SPDX-FileCopyrightText: 2025-present Ahum Maitra theahummaitra@gmail.com
#
# SPDX-License-Identifier: 	GPL-3.0-or-later


# Necessary Textual components and widgets
import time
from textual.screen import ModalScreen
from textual.app import ComposeResult
from textual.widgets import Label
from textual.containers import ScrollableContainer
from tinydb import TinyDB
from textual.widgets import Static

# to write logs
from loguru import logger

# To view the table
from rich.table import Table
from rich import box


class RawNotes(ModalScreen[None]):
    """
    This widget helps users to see all raw json file notes.
    """

    logger.add(".logs/app.log", rotation="10 MB")
    # keyboard bindings for the modal screen
    BINDINGS = [("escape", "pop_screen")]

    def compose(self) -> ComposeResult:
        """
        Main method for this widget
        """

        # read the json file
        with ScrollableContainer(id="ViewRawNotesScreen"):
            try:
                Database: TinyDB = TinyDB("./notes.json")

                all_notes: Table = Table(
                    box=box.SQUARE,  # ← adds a border all around
                    border_style="cyan",  # border color
                    show_lines=True,  # optional: lines between rows
                    expand=True,
                    highlight=True,
                )

                all_notes.add_column("Note", style="green")
                all_notes.add_column("Time", style="yellow")

                for row in Database.all():
                    all_notes.add_row(row["Note"], row["Time"])

            except FileNotFoundError as FileError:
                yield Label(
                    f"[b red]File not found, ERROR={FileError}! The app will close in 5 seconds[/b red]"
                )
                time.sleep(5)
                raise FileNotFoundError("THe 'notes.json' file is not here!")

            except Exception as UnexpectedError:
                yield Label(
                    f"[b red]Unexpected error - {UnexpectedError}! The app will close in 5 seconds[/b red]"
                )
                time.sleep(5)
                raise Exception(
                    f"Something is wrong! Unexpected error - {UnexpectedError}"
                )

            # all labels
            yield Label("[b yellow]Press ESC to exit this screen[/b yellow]\n\n\n\n")
            yield Label("[b yellow underline]ALL NOTES : [/b yellow underline]\n\n\n\n")

            # check notes are empty or not
            if (notes := len(Database)) == 0:
                yield Label("[b blue]Nothing in here![/b blue]")
            else:
                logger.info("User requested to view notes")
                yield Static(all_notes)

    def action_pop_screen(self):
        """
        method helps to dismiss the modal screen
        """
        self.dismiss()
