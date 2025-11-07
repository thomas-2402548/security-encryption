import os
from config.config import TITLE
from utils.key import generate_key, load_key
from utils.cryptography import encrypt_data, decrypt_data
from utils.console import display_logo, clear
from utils.options import OptionsMenu


def main():
    try:
        clear()
        display_logo()
        menu = OptionsMenu()
        menu.run()
    except KeyboardInterrupt:
        print("\nExiting program.")    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()