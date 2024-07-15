def change_contact(args, contacts):
    name = args[0]
    new_phone = args[1]
    if name in contacts:
        contacts[name] =  new_phone 
        return "Contact updated"
    else:
        return "Contact not found"
           