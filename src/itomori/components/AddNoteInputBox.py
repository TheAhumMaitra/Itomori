# SPDX-FileCopyrightText: 2025-present Ahum Maitra theahummaitra@gmail.com
#
# SPDX-License-Identifier: 	GPL-3.0-or-later


# all necessary Textual widgets, etc
from textual.widgets import Input
from textual import on

"""
This file is a component, which is just helps to render a input filed for user to write notes.
"""

UserNoteInputBox: Input = Input(placeholder="Write your note", id="NoteInputBox")
