from collections import UserDict, defaultdict
from datetime import datetime


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        super().__init__(value)


class Phone(Field):
    def __init__(self, value):
        super().__init__(value)

    def validate(self):
        # Check phone number format (10 digits)
        if len(self.value) != 10 or not self.value.isdigit():
            raise ValueError("Phone number should contained 10 digits")


class Birthday(Field):
    def __init__(self, value):
        super().__init__(value)

    def validate(self):
        # TODO: finish this realization
        pass


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = ""

    def add_phone(self, phone):
        new_phone = Phone(phone)
        new_phone.validate()
        self.phones.append(new_phone)

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        self.remove_phone(old_phone)
        self.add_phone(new_phone)

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        raise ValueError("Phone not found.")

    def __str__(self):
        return f"Contact name: {self.name.value} have phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record):
        if record.name.value in self.data:
            raise ValueError("Contact already exists.")
        self.data[record.name.value] = record

    def find(self, name):
        if name in self.data:
            return self.data[name]
        raise ValueError("Contact not found.")

    def delete(self, name):
        if name not in self.data:
            raise ValueError("Contact not found.")
        del self.data[name]

    # TODO: finish this realization

    def get_birthdays_per_week(self, users):
        today = datetime.today().date()
        res = defaultdict(list)
        for user in users:
            name = user["name"]
            birthday = user["birthday"].date()
            birthday_this_year = birthday.replace(year=today.year)
            if birthday_this_year > today:
                birthday_this_year.replace(year=today.year + 1)
                delta_days = (birthday_this_year - today).days
                if delta_days < 7:
                    birthday_week_day = birthday_this_year.strftime("%A")
                    if birthday_week_day == ("Sunday" or "Saturday"):
                        res["Monday"].append(name)
                    else:
                        res[birthday_week_day].append(name)

        for key, value in res.items():
            birth_name = ", ".join(value)
            print(f"{key}: {birth_name}")
