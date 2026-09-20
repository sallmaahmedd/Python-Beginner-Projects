import os
import json

contacts={}

filename = "contacts.json"
if os.path.exists(filename):
    with open(filename, "r") as file:
        contacts = json.load(file)

def save_contacts():
    with open(filename, "w") as file:
        json.dump(contacts, file)


print("Welcome to your Contact Book!")
print("""Please choose an your option:
        1. Add Contact
        2. View Contacts
        3. Search Contact
        4. Update Contact 
        5. Delete Contact
        6. Exit""")


while True:

    choice=input("Enter your choice (1-6): ")

    if choice=="1":
        contact_name=input("Enter contact name: ")
        contact_number=input("Enter contact number: ")
        contacts[contact_name]=contact_number
        print(f"Contact '{contact_name}' added successfully!")
        save_contacts()

    elif choice=="2":
        if not contacts:
            print("No contacts found.")
        else:
            for contact_name, contact_number in contacts.items():
                print(f"Name: {contact_name}, Number: {contact_number}")

    elif choice=="3":
        print("search by: 1. Name 2. Number") 
        search_choice=input("Enter your choice (1-2): ")

        if search_choice=="1":
            search_name=input("Enter contact name to search: ")
            if not search_name in contacts.keys():
                print("No available contacts with that name.")

            elif search_name in contacts.keys():
                print(f"contact number:{contacts[search_name]}")


        elif search_choice=="2":
            print("search by number")
            search_number=input("Enter contact number to search: ")

            if not search_number in contacts.values():
                print("No available contacts with that number.")

            elif search_number in contacts.values():

                matching_names = [name for name, number in contacts.items() if number == search_number]
                if len(matching_names) > 1:
                    print(f"Multiple contacts found with the number '{search_number}':")
                    for name in matching_names:
                        print(f"- {name}")
                    print("Please delete the contact by name instead.")

                elif len(matching_names) == 1:
                    print(f"contact name:{matching_names[0]}")


    elif choice=="4":
        name_to_update=input("Enter contact name to update: ")

        if not name_to_update in contacts.keys():
            print("No available contacts with that name.")

        elif name_to_update in contacts.keys():
            print("choose what to update: 1. Name 2. Number")
            update_choice=input("Enter your choice (1-2): ")

            if update_choice=="1":
                new_name=input("Enter the new contact name:")
                if new_name in contacts:
                    print(f"'{new_name}' already exists — choose a different name.")
                else:
                    contacts[new_name]=contacts.pop(name_to_update)
                    print(f"Contact '{name_to_update}''s name updated successfully!")

            elif update_choice=="2":
                new_number=input("Enter the new contact number:")
                contacts[name_to_update]=new_number
                print(f"Contact '{name_to_update}''s number updated successfully!")
            save_contacts()

    elif choice=="5":
        print("Delete contact by: 1. Name 2. Number")
        delete_choice=input("Enter your choice (1-2): ")

        if delete_choice=="1":
            contact_name_to_delete=input("Enter contact name to delete: ")

            if not contact_name_to_delete in contacts.keys():
                print("No available contacts with that name.")

            elif contact_name_to_delete in contacts.keys():
                """ del is a general-purpose Python statement for removing something by reference — a key from a dict, an item from a list, or even an entire variable. """
                del contacts[contact_name_to_delete]
                print(f"Contact '{contact_name_to_delete}' deleted successfully!")
                save_contacts()

        elif delete_choice=="2": 
            contact_number_to_delete=input("Enter contact number to delete: ")

            if not contact_number_to_delete in contacts.values():
                print("No available contacts with that number.")

            elif contact_number_to_delete in contacts.values():
                matching_names= [name for name, number in contacts.items() if number == contact_number_to_delete]
                if len(matching_names) > 1:
                    print(f"Multiple contacts found with the number '{contact_number_to_delete}':")
                    for name in matching_names:
                        print(f"- {name}")
                    print("Please delete the contact by name instead.")
                elif len(matching_names) == 1:
                    """ [0] is used to get the string value(contact name) at index 0 of the list returned by the list comprehension. """
                    contact_name_to_delete=matching_names[0]
                    del contacts[contact_name_to_delete]
                    save_contacts()
                    print(f"Contact '{contact_name_to_delete}''s number deleted successfully!")
            save_contacts()

    elif choice=="6":
        save_contacts()
        print("Your contacts have been saved. Goodbye!")
        break
