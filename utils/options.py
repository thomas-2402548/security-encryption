from InquirerPy import inquirer
from utils.key import generate_key
from utils.cryptography import encrypt_data, decrypt_data
import pyperclip

class OptionsMenu:

    def __init__(self):
        # Initializes the menu and generates a new encryption key
        self._key = generate_key()
        self._actions = {
            "Encrypt": self._encrypt_menu,
            "Decrypt": self._decrypt_menu,
            "Exit": self._exit_program,
        }


    def _display_main_menu(self):
        # Displays the main menu and handles user selection
        selected = inquirer.select(
            message="Select an option:",
            choices=list(self._actions.keys())
        ).execute()
        self._handle_mode_selection(selected)


    def _handle_mode_selection(self, option):
        # Handles the selected menu option
        action = self._actions.get(option)
        if action:
            action()


    def _encrypt_menu(self):
        # Menu for encrypting data
        text = self._prompt_text("Data to encrypt:")
        try:
            encrypted_data = encrypt_data(self._key, text)
            print(f"\nKey: {self._key}\nEncrypted data: {encrypted_data}\n")
            self._offer_copy_to_clipboard(encrypted_data)
        except Exception as e:
            print(f"An error occurred: {e}\n")
        self._display_main_menu()


    def _decrypt_menu(self):
        # Menu for decrypting data
        key = self._prompt_text("Key:")
        data = self._prompt_text(message="Encrypted data:")
        try:
            decrypted = decrypt_data(key.encode(), data)
            print(f"\nDecrypted data: {decrypted}\n")
        except Exception as e:
            print(f"Invalid key or text inserted, please try again\n")
            return self._decrypt_menu()
        self._display_main_menu()


    def _offer_copy_to_clipboard(self, data):
        # Offers to copy data to clipboard
        if inquirer.confirm(message="Copy to clipboard?", default=True).execute():
            pyperclip.copy(data)
            print("Copied to clipboard\n")


    def _prompt_text(self, message):
        # Prompts the user for text input
        while True:
            text = inquirer.text(message=message).execute().strip()
            if text:
                return text
            print("Input cannot be empty, please try again.\n")

    def _exit_program():
        lambda: exit(0)


