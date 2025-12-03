#   Copyright (C) 2025  Ahum Maitra

#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.

#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.

#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>


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
