from address_book import AddressBook
from data_manager import save_data, load_data
import utilities

def main():
    book = load_data()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = utilities.parse_input(user_input)

        if command in ["close", "exit"]:
            save_data(book)
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(utilities.add_contact(args, book))

        elif command == "change":
            print(utilities.change_contact(args, book))

        elif command == "phone":
            print(utilities.show_phone(args, book))

        elif command == "all":
            print(utilities.show_all_contacts(args, book))

        elif command == "add-birthday":
            print(utilities.add_birthday(args, book))

        elif command == "show-birthday":
            print(utilities.show_birthday(args, book))

        elif command == "birthdays":
            print(utilities.birthdays(args, book))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()