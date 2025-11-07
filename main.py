import os
from utils.console import display_logo, clear
from utils.options import OptionsMenu


def main():
    try:
        clear()
        display_logo()
        menu = OptionsMenu()
        menu._display_main_menu()
    except KeyboardInterrupt:
        print("\nExiting program.")    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()