'''
Simple Contact Book
Create a contact book where users can add, search, and delete contact details
(like name, phone number, and email).
You can store the data in a dictionary or use a CSV file to
practice file operations.
'''

import csv

# Global Variables
filename = "contact_book.csv"
fields = []
rows = []


# Read file; File is automatically closed
def _read_contact_book_file_():
    print(f"Opening {filename}...")
    try:
        with open(filename, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            fields.append(next(csvreader))
            for row in csvreader:
                rows.append(row)
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
        _create_contact_book_file_()
    except Exception as e:
        print(f"An error occured: {e}")


# Asks the user if they want to create a contact_book file.
# If yes, creates contact_book.csv
# If no, exits program
def _create_contact_book_file_():
    print("Creating new contact_book file...")
    try:
        with open(filename, "w") as csvfile:
            fields = ['First Name', 'Last Name', 'Email']
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(fields)

    # Prevent loop of being unable to create a file
    except FileNotFoundError:
        print(f"Could not create {filename}. Exiting program...")
        exit()

    # If, for some reason, the file does actually exist, exit to
    # prevent data loss. This is a programming error.
    except FileExistsError:
        print(f"{filename} already exists. Exiting...")
        exit()
    _read_contact_book_file_()


# Add Contact to contact_book.csv
def _add_contact_():
    try:
        first_name = input("Please enter the contact's First Name: ")
        last_name = input("Please enter the contact's Last Name: ")
        email = input("Please Enter the contact's Email Address: ")
        if (
            first_name.isnumeric() or
            last_name.isnumeric() or
            email.isnumeric()
        ):
            raise ValueError("Inputs should not be numbers.")
    except ValueError as e:
        print(f"Invalid Input: {e}")

    new_contact = [first_name, last_name, email]

    with open(filename, "a", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(new_contact)


# Find entry in contact book
def _search_for_contact_(contact_name):
    for row in rows:
        if row[0].lower() == contact_name.lower():
            return row
    return None


def _delete_contact_():
    name = input(
        "Enter the First Name of the contact you'd like to delete: "
        )
    contact = _search_for_contact_(name)

    if contact is None:
        print("That contact was not found.")
        return
    else:
        print("Are you sure you want to delete the following contact?")
        print(f"{contact[0]} {contact[1]}")
        response = input("Confirm (Y/N): ")
        if (response == 'Y' or response == 'y'):
            for row in rows:
                if row[0].lower() != contact[0].lower():
                    rows.append(row)
        with open(filename, "w", newline="") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(rows)
        print("Contact Deleted Successfully!")


# Main Method
_read_contact_book_file_()

'''
Print Testing :)
print(fields)
print(rows)
'''

_add_contact_()
# _delete_contact_()
