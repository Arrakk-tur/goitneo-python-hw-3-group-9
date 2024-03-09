from adress_book import AddressBook, Record


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return str(e)
        except SyntaxError:
            return "Give me name and phone please. Use spaces to separate your command."
        except IndexError:
            return "Not enough arguments"

    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts):
    name, phone = args
    record = Record(name=name)
    record.add_phone(phone)
    contacts.add_record(record)
    return f"Contact {name} added."


@input_error
def change_contact(args, contacts):
    name, old_phone, new_phone = args
    record = contacts.find(name)
    record.edit_phone(old_phone=old_phone, new_phone=new_phone)
    return f"Phone {old_phone} for contact {name} changed to {new_phone}."


@input_error
def get_phone(args, contacts):
    name = args[0]
    return contacts[name]


@input_error
def add_birthday(args, contacts):
    name, birthday = args
    contacts[name].add_birthday(birthday)
    return f"Birthday for {name} added."


@input_error
def show_birthday(args, contacts):
    name = args[0]
    record = contacts.find(name)
    return record.get_birthday()


def main():
    book = AddressBook()
    print(
        """Welcome to the assistant bot!
    You can use commands:
    - "add" - add a new contact,
    - "change" - change a contact's phone number,
    - "add-birthday" - add a contact's birthday,
    - "show-birthday" - show a contact's birthday,
    - "birthdays" - show birthdays of contacts for this week,
    - "phone" - show a contact's phone number,
    - "all" - show all contacts,
    """
    )
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))

        elif command == "change":
            print(change_contact(args, book))

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            book.get_birthdays_per_week()

        elif command == "phone":
            print(get_phone(args, book))

        elif command == "all":
            [print(value) for key, value in book.items()]

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
