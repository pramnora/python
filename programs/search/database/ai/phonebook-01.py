'''
Created: Wed 28 Feb 2024 
Updated: Wed 28 Feb 2024

I used Microsoft Bing search engine...and, choose tab: CoPilot/ChatGPT;
I told it to: "Create me a Python phonebook program
which allows me to add: name, address, phone numbers."
The below was the resultant code which came spilling out...in seconds.
'''

# A dictionary to store the phonebook entries
phonebook = {}

# A function to add a new entry to the phonebook
def add_entry(name, address, phone):
    # Check if the name already exists in the phonebook
    if name in phonebook:
        print(f"{name} already exists in the phonebook.")
    else:
        # Create a new entry with the given name, address, and phone
        phonebook[name] = {"address": address, "phone": phone}
        print(f"{name} added to the phonebook.")

# A function to search for an entry by name
def search_entry(name):
    # Check if the name exists in the phonebook
    if name in phonebook:
        # Retrieve the entry and print the details
        entry = phonebook[name]
        print(f"Name: {name}")
        print(f"Address: {entry['address']}")
        print(f"Phone: {entry['phone']}")
    else:
        # Print a message if the name is not found
        print(f"{name} not found in the phonebook.")

# A function to delete an entry by name
def delete_entry(name):
    # Check if the name exists in the phonebook
    if name in phonebook:
        # Delete the entry and print a confirmation message
        del phonebook[name]
        print(f"{name} deleted from the phonebook.")
    else:
        # Print a message if the name is not found
        print(f"{name} not found in the phonebook.")

# A function to display all the entries in the phonebook
def display_entries():
    # Check if the phonebook is empty
    if phonebook:
        # Loop through the phonebook and print each entry
        for name, entry in phonebook.items():
            print(f"Name: {name}")
            print(f"Address: {entry['address']}")
            print(f"Phone: {entry['phone']}")
            print("-" * 20)
    else:
        # Print a message if the phonebook is empty
        print("The phonebook is empty.")

# A function to display the menu and get the user's choice
def display_menu():
    print("Welcome to the phonebook program.")
    print("Please choose an option:")
    print("1. Add a new entry")
    print("2. Search for an entry by name")
    print("3. Delete an entry by name")
    print("4. Display all the entries")
    print("5. Exit the program")
    # Get the user's choice and validate it
    choice = input("Enter your choice: ")
    while choice not in ["1", "2", "3", "4", "5"]:
        print("Invalid choice. Please try again.")
        choice = input("Enter your choice: ")
    # Return the user's choice as an integer
    return int(choice)

# A main function to run the program
def main():
    # Loop until the user chooses to exit
    while True:
        # Display the menu and get the user's choice
        choice = display_menu()
        # Perform the appropriate action based on the user's choice
        if choice == 1:
            # Get the name, address, and phone from the user
            name = input("Enter the name: ")
            address = input("Enter the address: ")
            phone = input("Enter the phone number: ")
            # Add the new entry to the phonebook
            add_entry(name, address, phone)
        elif choice == 2:
            # Get the name from the user
            name = input("Enter the name: ")
            # Search for the entry by name
            search_entry(name)
        elif choice == 3:
            # Get the name from the user
            name = input("Enter the name: ")
            # Delete the entry by name
            delete_entry(name)
        elif choice == 4:
            # Display all the entries in the phonebook
            display_entries()
        elif choice == 5:
            # Exit the program
            print("Thank you for using the phonebook program. Goodbye.")
            break

# Call the main function
main()
