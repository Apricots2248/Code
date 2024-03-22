import csv
import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def edit_q():
    file_path = os.path.join('CSV_Files', 'ProductStock.csv')  # Moved file_path inside edit_q function

    while True:  # Looping menu until the user chooses to quit
        clear_terminal()
        choice = input("Would you like to Add item(1), Edit item(2), Remove item(3), Quit(4): ")
        clear_terminal()
        
        if choice == '1':
            add_item(file_path)  # Pass file_path to add_item function
        elif choice == '2':
            edit_item(file_path)  # Pass file_path to edit_item function
        elif choice == '3':
            remove_item(file_path)  # Pass file_path to remove_item function
        elif choice == '4':
            print('Exiting the program.')
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

def add_item(file_path):  # Accept file_path as an argument
    print_csv_file(file_path)
    item = input("Item name: ")
    price = input("Item price: ")

    with open(file_path, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([item, price])

def edit_item(file_path):  # Placeholder function
    print("Edit item functionality to be implemented.")

def remove_item(file_path):  # Placeholder function
    print("Remove item functionality to be implemented.")

def print_csv_file(file_path):
    try:
        with open(file_path, 'r', newline='') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                print(', '.join(row))
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

edit_q()
