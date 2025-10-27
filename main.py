import os
from config.config import TITLE
from utils.key import generate_key, load_key
from utils.cryptography import encrypt_data, decrypt_data
from utils.console import logo, clear
from utils.options import display_options

def main():
    try:
        logo()
        os.system(f"{TITLE} - Encryption Tool")
        display_options()
    except KeyboardInterrupt:
        print("\nExiting program.")    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()