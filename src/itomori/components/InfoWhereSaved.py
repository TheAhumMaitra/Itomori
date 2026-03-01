# SPDX-FileCopyrightText: 2025-present Ahum Maitra theahummaitra@gmail.com
#
# SPDX-License-Identifier: 	GPL-3.0-or-later


# all necessary Textual widgets
from textual.widgets import Label
from itomori import DB_PATH

"""
This file is a component, which is just helps to give user a info where the notes are saved in.
"""

WhereSavedWarn: Label = Label(
    f"All Notes are saved in {DB_PATH}", id="WhereSavedNotesWarn"
)
