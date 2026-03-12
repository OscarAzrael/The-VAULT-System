#!/usr/bin/env python3
# Program Made By Oscar Azrael
# Co-Written By Friday
import json
import os

print(f"Working directory: {os.getcwd()}")

# Database as a dictionary
database = {}

# Function to add data to the database
def add_entry():
    keyword = input("Enter the keyword: ").strip()
    
    # Sanity check: prevent unintentional overwrites
    if keyword in database:
        confirm = input(f"'{keyword}' already exists. Overwrite? (y/n): ").lower()
        if confirm != 'y':
            print("Entry not modified.")
            return

    info = input("Enter the information: ").strip()
    database[keyword] = info
    print(f"Added/Updated entry: {keyword}")

# Function to search for data in the database
def search_entry():
    keyword = input("Enter a keyword to search: ").strip().lower()
    matches = {}

    for key, value in database.items():
        print(f"Checking: {key}")  # Optional debug
        if keyword in key.lower():
            matches[key] = value

    if matches:
        print("\nFound the following matches:")
        for key, value in matches.items():
            print(f"Keyword: {key} - Information: {value}")
    else:
        print("No matches found.")

# Function to delete an entry from the database
def delete_entry():
    keyword = input("Enter the keyword to delete: ").strip()
    if keyword in database:
        confirm = input(f"Are you sure you want to delete '{keyword}'? (y/n): ").lower()
        if confirm == 'y':
            del database[keyword]
            print(f"Deleted entry: {keyword}")
        else:
            print("Delete cancelled.")
    else:
        print("Keyword not found in the database.")

# Function to list all keywords in the database
def list_keywords():
    if database:
        print("\nAll stored keywords:")
        for keyword in sorted(database.keys()):
            print(f"- {keyword}")
    else:
        print("The database is currently empty.")

# Function to save the database to a file
def save_database():
    filename = "database.json"
    with open(filename, 'w') as file:
        json.dump(database, file)
    print(f"Database saved to {filename}.")

# Function to load the database from a file
def load_database():
    global database
    filename = "database.json"
    try:
        with open(filename, 'r') as file:
            database = json.load(file)
        print(f"Database loaded from {filename}.")
    except FileNotFoundError:
        print(f"No previous database found. Starting fresh.")

# Main loop for interaction
def main():
    load_database()
    while True:
        print("\nOptions: [1] Add Entry [2] Search [3] Save [4] Delete [5] List Keywords [6] Quit")
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            add_entry()
        elif choice == "2":
            search_entry()
        elif choice == "3":
            save_database()
        elif choice == "4":
            delete_entry()
        elif choice == "5":
            list_keywords()
        elif choice == "6":
            save_database()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Run the main loop
if __name__ == "__main__":
    main()
