from InquirerPy import inquirer
from utils.key import generate_key
from utils.cryptography import encrypt_data, decrypt_data
import pyperclip

class OptionsMenu:
    def __init__(self):
        self.actions = {
            "Encrypt": self._encrypt_menu,
            "Decrypt": self._decrypt_menu,
            "Exit": self._exit_program,
        }


    def run(self):
        self._display_main_menu()


    def _display_main_menu(self):
        selected = inquirer.select(
            message="Select an option:",
            choices=list(self.actions.keys())
        ).execute()
        self._handle_mode_selection(selected)


    def _handle_mode_selection(self, option):
        action = self.actions.get(option)
        if action:
            action()


    def _encrypt_menu(self):
        text = self._prompt_text("Data to encrypt:")
        try:
            key = generate_key()
            encrypted_data = encrypt_data(key, text)
            print(f"\nKey: {key}\nEncrypted data: {encrypted_data}\n")
            self._offer_copy_to_clipboard(encrypted_data)
        except Exception as e:
            print(f"An error occurred: {e}\n")
        self._display_main_menu()


    def _decrypt_menu(self):
        key = self._prompt_text("Key:")
        data = self._prompt_text(message="Encrypted data:")
        try:
            decrypted = decrypt_data(key.encode(), data)
            print(f"\nDecrypted data: {decrypted}\n")
        except Exception as e:
            print(f"Invalid key or text inserted\n")
        self._display_main_menu()


    def _offer_copy_to_clipboard(self, data):
        if inquirer.confirm(message="Copy to clipboard?", default=True).execute():
            pyperclip.copy(data)
            print("Copied to clipboard\n")


    def _prompt_text(self, message):
        while True:
            text = inquirer.text(message=message).execute().strip()
            if text:
                return text
            print("Input cannot be empty, please try again.\n")

    def _exit_program():
        lambda: exit(0)


