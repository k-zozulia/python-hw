import utilities

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = utilities.parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(utilities.add_contact(args, contacts))
        elif command == "change":
            print(utilities.change_contact(args, contacts))
        elif command == "phone":
            print(utilities.show_phone(args, contacts))
        elif command == "all":
            print(utilities.show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()