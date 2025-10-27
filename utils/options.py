from InquirerPy import inquirer

def display_options():
    options = ["Encrypt", "Decrypt", "Exit"]

    selected = inquirer.select(
        message="Select an option:",
        choices=options,
    ).execute()

    handle_selection(selected)


def handle_selection(option):
    if option == "Encrypt":
        pass
    elif option == "Decrypt":
        pass
    elif option == "Exit":
        raise SystemExit
