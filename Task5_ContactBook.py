contacts = {}

def add_contact():
    #add the contact details 
    name = input("Enter Name: ").strip() #give name as input
    if name in contacts: #cheks if name is in contacts or not
        print("Contact already exists.")
        return
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts[name] = {"phone":phone, "email": email, "address": address} #storing the details 
    print("Contact added successfully.")

def view_contacts():
    #view the contact details
    if not contacts:
        return print("No contacts found.")
    print("\nContact Lists: ")
    for name, details in contacts.items():
        print(f"Name: {name}, Phone:{details['phone']}")

def search_contact():
    #search the contact details
    search = input("Enter name or phone number to search: ")
    found = False 
    for name, details in contacts.items():
        if search.lower() in name.lower() or search == details['phone'] : #checks if the searched name is present or not
            print("\nFound Contact: ")
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            found = True
            break
    if not found:
        print("Contact not found.")

def update_contact():
    #update the contact details
    name = input("Enter the name of the contact to update: ").strip()
    if name not in contacts:
        print("Contact not found.")
        return 
    print("Enter new details (leave blank to keep the current value): ") #Giving a new details
    new_name = input(f"Name ({name}): ").strip()
    phone = input(f"Phone ({contacts[name]['phone']}): ").strip() 
    email = input(f"Email ({contacts[name]['email']}): ").strip() 
    address = input(f"Address ({contacts[name]['address']}): ").strip() 

    contacts.pop(name)
    contacts[new_name] = {'phone': phone, 'email': email, 'address': address}
    print("Contact updated successfully!")

def delete_contact():
    #delete the contact details
    name = input("Enter the name of the contact to delete: ") 
    if name in contacts: #checks if name is present or not
        del contacts[name]
        print("Contact deleted successfully!") 
    else:
        print("Contact not found")

def main():
    print("\n-----Contact Lists-----")
    print("1.Add Contact")
    print("2.View Contact List")
    print("3.Search Contact")
    print("4.Update Contact")
    print("5.Delete Contact")
    
    while True:
        choice = input("Enter the choice (1-6): ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Existing the program.")
            break
        else:
            print("Invalid Choice!")

if __name__ == '__main__' :
    main()