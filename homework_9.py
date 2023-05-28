contacts = {}

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Invalid input."
        except IndexError:
            return "Invalid command."
    return inner


@input_error
def add_contact(name, phone):
    contacts[name] = phone
    return "Contact added successfully."


@input_error
def change_phone(name, phone):
    contacts[name] = phone
    return "Phone number updated successfully."


@input_error
def get_phone(name):
    return contacts[name]


def show_all_contacts():
    if not contacts:
        return "No contacts found."
    else:
        result = ""
        for name, phone in contacts.items():
            result += f"{name}: {phone}\n"
        return result


def main():
    while True:
        user_input = input("Enter a command: ").lower()
        
        if user_input == "good bye" or user_input == "close" or user_input == "exit":
            print("Good bye!")
            break
        
        elif user_input == "hello":
            print("How can I help you?")
        
        elif user_input.startswith("add"):
            try:
                _, name, phone = user_input.split()
                print(add_contact(name, phone))
            except ValueError:
                print("Give me name and phone, please.")
        
        elif user_input.startswith("change"):
            try:
                _, name, phone = user_input.split()
                print(change_phone(name, phone))
            except ValueError:
                print("Give me name and phone, please.")
        
        elif user_input.startswith("phone"):
            try:
                _, name = user_input.split()
                print(get_phone(name))
            except ValueError:
                print("Enter a name.")
        
        elif user_input == "show all":
            print(show_all_contacts())
        
        else:
            print("Invalid command. Try again.")


if __name__ == "__main__":
    main()
