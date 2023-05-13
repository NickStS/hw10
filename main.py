from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass


class Record:
    def __init__(self, name, phone=None):
        self.name = Name(name)
        self.phones = []
        if phone:
            self.add_phone(phone)

    def add_phone(self, phone):
        phone = Phone(phone)
        self.phones.append(phone)

    def edit_phone(self, index, phone):
        phone = Phone(phone)
        self.phones[index] = phone

    def delete_phone(self, index):
        del self.phones[index]


class AddressBook(UserDict):
    def add_contact(self, record):
        self.data[record.name.value] = record

    def edit_contact(self, name, phone):
        record = self.data[name]
        record.edit_phone(0, phone)
        self.add_contact(record)

    def delete_contact(self, name):
        del self.data[name]

    def show_all(self):
        if self.data:
            return "\n".join("{}: {}".format(name, record.phones[0].value) for name, record in self.data.items())
        else:
            return "No contacts found"


def input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except KeyError:
            return "Contact not found"
        except ValueError:
            return "Enter name and phone"
        except IndexError:
            return "Enter name and phone"

    return wrapper


@input_error
def add_contact(ab, name, phone):
    record = Record(name, phone)
    ab.add_contact(record)
    return "Contact added"


@input_error
def change_phone(ab, name, phone):
    ab.edit_contact(name, phone)
    return "Phone number changed"


@input_error
def show_phone(ab, name):
    record = ab.data[name]
    return record.phones[0].value


ab = AddressBook()

def main():
    print("Hello!)")

    while True:
        command = input().lower()

        if command == "hello":
            print("How can I help you?")

        elif command.startswith("add"):
            try:
                name, phone = input("Enter name and phone: ").split()
                result = add_contact(ab, name, phone)
            except ValueError:
                result = "Enter name and phone"
            print(result)

        elif command.startswith("change"):
            try:
                name, phone = input("Enter name and phone: ").split()
                result = change_phone(ab, name, phone)
            except ValueError:
                result = "Enter name and phone"
            print(result)

        elif command.startswith("phone"):
            try:
                name = command.split()[1]
                result = show_phone(ab, name)
            except IndexError:
                result = "Enter name"
            print(result)

        elif command == "show all":
            result = ab.show_all()
            print(result)

        elif command in ["good bye", "close", "exit"]:
            print("Good bye!")
            break

        else:
            print("Unknown command")


main()