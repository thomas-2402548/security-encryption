import os
from art import text2art
from config.config import TITLE, LOGO_FONT, LOGO_COLOR


def display_logo():
    # Generate and display ASCII art logo
    logo_text = text2art(TITLE, font=LOGO_FONT)
    print(f"\n{LOGO_COLOR}{logo_text}")


def clear():
    # Clear the terminal screen
    os.system('clear')