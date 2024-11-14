# Contact Book
This is a repository for my Contact Book Python project. It is a side-project that I am working on
to better understand Python as a language as I am not familiar with it.

## Functionality
This program reads from a .csv file named contact_book.csv. The file is created if it does not already exist when
the program is run. All contacts are loaded into a List upon the initial start of the program. As changes are made,
the List is modified, and then the file is updated.

Users currently can Add and Delete contacts from the file.

## File Structure
Contact Book/
|-- contact_book/
|   |-- test/
|   |   |-- test_contact_book.py
|   |
|   |-- contact_book.py
|
|-- README.md


## CI/CD
I do not intend to perform a proper "Continuous Delivery" development cycle, however PyTest and GitHub Actions
will be used to ensure functionality of the program.

## Pushing to the Repository
The generated contact_book.csv should *not* be committed to the repository.