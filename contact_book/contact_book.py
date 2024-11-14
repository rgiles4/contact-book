import csv

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

    with open(filename, "a", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(new_contact)


# Find entry in contact book
def _search_for_contact_(contact_name):
    for row in rows:
        if row[0].lower() == contact_name.lower():
            return row
    return None


def delete_contact():
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
