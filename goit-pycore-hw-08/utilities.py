from address_book import AddressBook
from record import Record
from datetime import datetime, timedelta

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return str(e)
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Enter user name."
    return inner

def parse_input(user_input):
    parts = user_input.split()
    command = parts[0].strip().lower()
    args = parts[1:]
    return command, args

@input_error
def add_contact(args, book: AddressBook):

    if len(args) != 2:
        raise ValueError("Give me name and phone please.")
    
    name, phone = args

    record = book.find(name)

    if record is None:
        record = Record(name)
        record.add_phone(phone)
        book.add_record(record)
        return "Contact added."
    
    record.add_phone(phone)
    return "Phone number updated."

@input_error
def change_contact(args, book: AddressBook):
    if len(args) != 3:
        raise ValueError("Please provide name, old phone number, and new phone number.")

    name, old_phone, new_phone = args
    
    record = book.find(name)
    if record is None:
        raise KeyError
    
    record.edit_phone(old_phone, new_phone)
    return "Phone number updated."

@input_error
def show_phone(args, book: AddressBook):
    if len(args) != 1:
        raise IndexError
    
    name = args[0]

    record = book.find(name)
    if record is None:
        raise KeyError
    
    return f"{name}'s phone numbers: {', '.join(phone.value for phone in record.phones)}"

@input_error
def show_all_contacts(args, book: AddressBook):
    if not book:
        return "No contacts found."
    
    return '\n'.join(str(record) for record in book.values())

@input_error
def add_birthday(args, book: AddressBook):
    if len(args) != 2:
        raise ValueError("Please provide name and birthday")
    
    name, birthday = args
    record = book.find(name)

    if record is None:
        raise KeyError
    
    record.add_birthday(birthday)
    return "Birthday added."

@input_error
def show_birthday(args, book: AddressBook):
    if len(args) != 1:
        raise IndexError
    
    name = args[0]
    record = book.find(name)

    if record is None:
        raise KeyError
    
    if record.birthday:
        return f"{name}'s birthday: {record.birthday.value}"
    else:
        return f"{name} has no birthday set."


@input_error
def birthdays(args, book: AddressBook):
    upcoming_birthdays = book.get_upcoming_birthdays()

    if not upcoming_birthdays:
        return "No upcoming birthdays in the next week."
    
    return '\n'.join(f"{user['name']} - {user['congratulation_date']}" for user in upcoming_birthdays)