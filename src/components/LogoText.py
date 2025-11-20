# all necessary Textual widgets
from textual.widgets import Label

"""
This file is a component, which is just helps to render the Itomori logo.
"""

ascii_logo = '''
 █████  █████                                                 ███
▒▒███  ▒▒███                                                 ▒▒▒
 ▒███  ███████    ██████  █████████████    ██████  ████████  ████
 ▒███ ▒▒▒███▒    ███▒▒███▒▒███▒▒███▒▒███  ███▒▒███▒▒███▒▒███▒▒███
 ▒███   ▒███    ▒███ ▒███ ▒███ ▒███ ▒███ ▒███ ▒███ ▒███ ▒▒▒  ▒███
 ▒███   ▒███ ███▒███ ▒███ ▒███ ▒███ ▒███ ▒███ ▒███ ▒███      ▒███
 █████  ▒▒█████ ▒▒██████  █████▒███ █████▒▒██████  █████     █████
▒▒▒▒▒    ▒▒▒▒▒   ▒▒▒▒▒▒  ▒▒▒▒▒ ▒▒▒ ▒▒▒▒▒  ▒▒▒▒▒▒  ▒▒▒▒▒     ▒▒▒▒▒



'''
LogoRender = Label(ascii_logo, id="LogoText")
