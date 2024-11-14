'''
This file contains all functions that
involve reading from or updating contact_book.csv
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
