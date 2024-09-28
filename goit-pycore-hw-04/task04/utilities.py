def parse_input(user_input):
    parts = user_input.split()
    command = parts[0].strip().lower()
    args = parts[1:]
    return command, args

def add_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command. Usage: add [name] [phone]"
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command. Usage: change [name] [new phone]"
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."

def show_phone(args, contacts):
    if len(args) != 1:
        return "Invalid command. Usage: phone [name]"
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found." 

def show_all(contacts):
    if not contacts:
        return "Contacts not found"
    result = ""
    for contact, phone in contacts.items():
        result += f"{contact} - {phone}\n"
    return result
