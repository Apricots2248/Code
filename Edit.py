import csv
import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

file_path = os.path.join('CSV_Files', 'ProductStock.csv')

def edit_q():
    clear_terminal()
    choice = input("Would you like to Add item(1), Edit item(2), Remove item(3), Quit(4): ")
    clear_terminal()
    if choice == '1':
        add_item()
    elif choice == '2':
        edit_item()
    elif choice == '3':
        remove_item()
    else:
        if choice == '4':
            print('done')

def add_item():
    # Assuming print_csv_file is a function defined elsewhere that prints the contents of a CSV file
    print_csv_file('ProductStock.csv')
    
    item = input("Item name: ")
    price = input("Item price: ")

    with open(file_path, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([item, price])

def edit_item():
    pass

def remove_item():
    pass

def print_csv_file(file_path):
    with open(file_path, 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            print(', '.join(row))

edit_q()