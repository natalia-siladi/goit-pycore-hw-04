from commands.add_contact import add_contact
from commands.contact import change_contact
from commands.phone import show_phone

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def main():
    contacts =  {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ").strip().lower()
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "phone": 
            print(show_phone(args, contacts)) 
        elif command == "change":
            print(change_contact(args, contacts))    
        elif command == "all":
            print(contacts)              
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
