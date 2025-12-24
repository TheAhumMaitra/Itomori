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
from textual.app import ComposeResult
from textual.containers import ScrollableContainer
from textual.screen import ModalScreen
from textual.widgets import Footer, Label, Static, Header
from tinydb import TinyDB


class RawNotes(ModalScreen[None]):
    """
    This widget helps users to see all raw json file notes.
    """

    logger.add(".logs/app.log", rotation="10 MB")
    # keyboard bindings for the modal screen
    BINDINGS = [("escape", "pop_screen", "Exit Notes Screen")]

    def compose(self) -> ComposeResult:
        """
        Main method for this widget
        """
        yield Header(show_clock=True)
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
            yield Label("[b yellow underline]ALL NOTES : [/b yellow underline]\n\n\n\n")

            # check notes are empty or not
            if (notes := len(Database)) == 0:
                yield Label("[b blue]No notes found![/b blue]")
            else:
                logger.info("User requested to view notes")
                yield Static(all_notes)

        yield Footer()

    def action_pop_screen(self):
        """
        method helps to dismiss the modal screen
        """
        self.dismiss()
