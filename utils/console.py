import os
from art import text2art
from config.config import TITLE, LOGO_FONT, LOGO_COLOR


def display_logo():
    logo_text = text2art(TITLE, font=LOGO_FONT)
    print(f"\n{LOGO_COLOR}{logo_text}")


def clear():
    os.system('clear')