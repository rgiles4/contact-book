'''
This file contains all functions that
involve reading from or updating contact_book.csv

Functions in this file ONLY modify the .csv file.
Any modifications to the rows or fields List should be
done in contact_book.py UNLESS they need to be updated
from the file.
'''

import csv

# Important Variables
fields = []
rows = []


# Read file
def read_contact_book_file(filename):
    # print(f"Opening {filename}...")
    try:
        with open(filename, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            fields.append(next(csvreader))
            for row in csvreader:
                rows.append(row)
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
        create_contact_book_file(filename)
    except Exception as e:
        print(f"An error occured: {e}")
    return fields, rows


# Create file if it does not exist
def create_contact_book_file(filename):
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
    read_contact_book_file()


# Call when the file has been added to
# Ensures rows List is updated
def add_to_file(filename, new_contact):
    with open(filename, "a", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(new_contact)
    fields, rows = read_contact_book_file(filename)
    return fields, rows


# Call when the file has a row deleted
# Ensures rows List is updated
def delete_from_file(filename, contact):
    for row in rows:
        if row[0].lower() != contact[0].lower():
            rows.append(row)
    with open(filename, "w", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(rows)
    fields, rows = read_contact_book_file(filename)
    return fields, rows
