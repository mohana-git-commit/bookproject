def display_menu():
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def add_contact(contacts):
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    print(f"Contact '{name}' added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts to display.")
        return
    print("\nContact List:")
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. {contact['name']} - {contact['phone']}")

def search_contacts(contacts):
    query = input("Enter name or phone number to search: ").strip().lower()
    found = [c for c in contacts if query in c['name'].lower() or query in c['phone']]
    
    if not found:
        print("No contacts found matching your search.")
    else:
        print(f"\nFound {len(found)} contact(s):")
        for contact in found:
            print_contact_details(contact)

def print_contact_details(contact):
    print("-------------------------------")
    print(f"Name   : {contact['name']}")
    print(f"Phone  : {contact['phone']}")
    print(f"Email  : {contact['email']}")
    print(f"Address: {contact['address']}")
    print("-------------------------------")

def update_contact(contacts):
    query = input("Enter name or phone number of the contact to update: ").strip().lower()
    for contact in contacts:
        if query in contact['name'].lower() or query in contact['phone']:
            print("Contact found:")
            print_contact_details(contact)
            print("Enter new details (leave blank to keep current value):")
            
            new_name = input(f"New name [{contact['name']}]: ").strip()
            new_phone = input(f"New phone [{contact['phone']}]: ").strip()
            new_email = input(f"New email [{contact['email']}]: ").strip()
            new_address = input(f"New address [{contact['address']}]: ").strip()

            if new_name:
                contact['name'] = new_name
            if new_phone:
                contact['phone'] = new_phone
            if new_email:
                contact['email'] = new_email
            if new_address:
                contact['address'] = new_address

            print("Contact updated successfully!")
            return
    print("Contact not found.")

def delete_contact(contacts):
    query = input("Enter name or phone number of the contact to delete: ").strip().lower()
    for i, contact in enumerate(contacts):
        if query in contact['name'].lower() or query in contact['phone']:
            print("Contact found:")
            print_contact_details(contact)
            confirm = input("Are you sure you want to delete this contact? (y/n): ").strip().lower()
            if confirm == 'y':
                contacts.pop(i)
                print("Contact deleted successfully.")
            else:
                print("Deletion cancelled.")
            return
    print("Contact not found.")

def main():
    contacts = []
    print("Welcome to the Contact Book!")

    while True:
        display_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contacts(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
