contacts = {}

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    
    if name in contacts:
        print("Contact already exists!")
    else:
        contacts[name] = {"phone": phone, "email": email}
        print(f"Contact '{name}' added successfully.")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for name, details in contacts.items():
            print(f"\nName: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")


def update_contact():
    name = input("Enter the contact name to update: ")
    if name in contacts:
        print("Leave field empty to keep current value.")
        phone = input("New phone number: ") or contacts[name]["phone"]
        email = input("New email: ") or contacts[name]["email"]
        contacts[name] = {"phone": phone, "email": email}
        print(f"Contact '{name}' updated successfully.")
    else:
        print("Contact not found.")


def delete_contact():
    name = input("Enter the contact name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print("Contact not found.")

def menu():
    while True:
        print("\n******Contact Manager******")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice for contact (1-5): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            update_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            print("Exiting Contact Manager.")
            break
        else:
            print("Invalid choice. Please try again.")
menu()
 
