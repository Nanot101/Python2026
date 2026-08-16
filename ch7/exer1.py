 # Contact Book — Store contacts as a dictionary of dictionaries ({"Alex": {"phone": "...", "email": "..."}}). Let the user add/look up/delete contacts.

contacts = {}

while True:
    print("Contact book options:\n\tAdd\n\tLook up\n\tDelete\n\tView\n\tQuit")
    user_choice = str(input("Input: "))
    user_choice = user_choice.lower()

    match user_choice:
        case "add":
            print("Adding contact...")
            name = str(input("Enter name: "))
            if name != "" and name not in contacts:
                print(f"Adding {name}...")
                contacts[name] = {}
                phone = str(input(f"Enter phone number of {name}: "))
                contacts[name]["phone"] = phone
                email = str(input(f"Enter email of {name}: "))
                contacts[name]["email"] = email
                # print(contacts)
                print(f"Successfully added contact {name}\n")
            else:
                print("Not a valid name, try again.\n")
                continue

        case "look up":
            print("Looking up contact...")
            name = str(input("Enter name: "))
            if name != "" and name in contacts:
                print(f"Looking up info for {name}: ")
                print(contacts[name])
                print(f"Successfully looked up contact {name}\n")
            else:
                print("Not a valid name, try again.\n")
                continue

        case "delete":
            print("Deleting contact...")
            name = str(input("Enter name to delete: "))
            if name != "" and name in contacts:
                print(f"Deleting {name}...")
                del contacts[name]
                # print(contacts)
                print(f"Successfully deleted contact {name}\n")
            else:
                print("Name not found, try again.\n")
                continue
        
        case "view":
            print("Viewing all contacts...")
            for contact in contacts.items():
                print(contact)
            print()
            

        case "quit": 
            print("Quitting...")
            break

        case _:
            print("Invalid input\n")
            continue