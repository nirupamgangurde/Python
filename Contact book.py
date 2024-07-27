import json
import os

CONTACTS_FILE = 'contacts'


def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(name, phone):
    contacts = load_contacts()
    contacts[name] = phone
    save_contacts(contacts)
    print(f"Contact added: {name} - {phone}")

def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No contacts found.")
    else:
        print("Contacts:")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")

def delete_contact(name):
    contacts = load_contacts()
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"Contact deleted: {name}")
    else:
        print("Contact not found.")

def contact_book():
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone number: ")
            add_contact(name, phone)
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            name = input("Enter contact name to delete: ")
            delete_contact(name)
        elif choice == '4':
            print("Exiting the contact book.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    contact_book()
