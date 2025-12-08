# SPDX-FileCopyrightText: 2025-present Ahum Maitra theahummaitra@gmail.com
#
# SPDX-License-Identifier: 	GPL-3.0-or-later


# all necessary Textual widgets
from textual.widgets import Label

"""
This file is a component, which is just helps to render the Itomori logo.
"""

ascii_logo: str = """
 █████  █████                                                 ███
▒▒███  ▒▒███                                                 ▒▒▒
 ▒███  ███████    ██████  █████████████    ██████  ████████  ████
 ▒███ ▒▒▒███▒    ███▒▒███▒▒███▒▒███▒▒███  ███▒▒███▒▒███▒▒███▒▒███
 ▒███   ▒███    ▒███ ▒███ ▒███ ▒███ ▒███ ▒███ ▒███ ▒███ ▒▒▒  ▒███
 ▒███   ▒███ ███▒███ ▒███ ▒███ ▒███ ▒███ ▒███ ▒███ ▒███      ▒███
 █████  ▒▒█████ ▒▒██████  █████▒███ █████▒▒██████  █████     █████
▒▒▒▒▒    ▒▒▒▒▒   ▒▒▒▒▒▒  ▒▒▒▒▒ ▒▒▒ ▒▒▒▒▒  ▒▒▒▒▒▒  ▒▒▒▒▒     ▒▒▒▒▒



"""
LogoRender: Label = Label(ascii_logo, id="LogoText")
