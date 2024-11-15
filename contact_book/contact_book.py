'''
This file contains all functions that
involve modifying the contact book.

Functions in this file ONLY modify the rows List.
Any modifications to the contact_book.csv should be done
in csv_functions.py.
'''

from csv_functions import (
    add_to_file,
    delete_from_file
)

# Global Variables
filename = "contact_book.csv"
fields = []
rows = []


# Add Contact to contact_book.csv
def add_contact():
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
    fields, rows = add_to_file(filename, new_contact)


# Find entry in contact book
def search_for_contact(contact_name):
    for row in rows:
        if row[0].lower() == contact_name.lower():
            return row
    return None


def delete_contact():
    name = input(
        "Enter the First Name of the contact you'd like to delete: "
        )
    contact = search_for_contact(name)

    if contact is None:
        print("That contact was not found.")
        return
    else:
        print("Are you sure you want to delete the following contact?")
        print(f"{contact[0]} {contact[1]}")
        response = input("Confirm (Y/N): ")
        if (response == 'Y' or response == 'y'):
            fields, rows = delete_from_file(filename, contact)
        print("Contact Deleted Successfully!")
