from adress_book import AddressBook, Record


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return str(e)
        except SyntaxError:
            return "Give me name and phone please. Use spaces to separate your command."

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
    name, phone = args
    record = contacts.find(name)

    # TODO: finish this realization
    old_phone = record

    contacts[name] = phone
    return f"Contact {name} changed."


@input_error
def get_phone(args, contacts):
    name = args[0]
    return contacts[name]


def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
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

        # TODO: finish this realization
        elif command == "change":
            print(change_contact(args, book))

        elif command == "phone":
            print(get_phone(args, book))

        elif command == "all":
            [print(value) for key, value in book.items()]

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
