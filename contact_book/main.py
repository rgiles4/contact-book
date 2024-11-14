'''
Simple Contact Book
Create a contact book where users can add, search, and delete contact details
(like name, phone number, and email).
You can store the data in a dictionary or use a CSV file to
practice file operations.
'''

from csv_functions import (
    read_contact_book_file
)

from contact_book import (
    add_contact,
    delete_contact
)

# Main Method
read_contact_book_file()

'''
Print Testing :)
print(fields)
print(rows)
'''

add_contact()
delete_contact()
