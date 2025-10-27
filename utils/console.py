import os
from art import text2art
from config.config import TITLE


def logo():
    clear()
    logo = text2art(TITLE,font='colossal',chr_ignore=True)
    print(f"\n\n{logo}")

def clear():
    os.system('clear')