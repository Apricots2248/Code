import csv
import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

file_path = os.path.join('ProductStock.csv')

def edit_q():
    clear_terminal()
    choice = input("Would you like to Add item(1), Edit item(2), Remove item(3), Quit(4): ")
    clear_terminal()
    if choice == '1':
        add_item()
        clear_terminal()
    elif choice == '2':
        edit_item()
        clear_terminal()
    elif choice == '3':
        remove_item()
        clear_terminal()
    else:
        if choice == '4':
            print('done')
            clear_terminal()

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
    print_csv_file('ProductStock.csv')
    item_name = input("Enter the name of the item to remove: ")
    file_path = 'ProductStock.csv'
    temp_file_path = 'temp_ProductStock.csv'
    
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = [row for row in reader if row[0] != item_name]
    
    with open(temp_file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows)
    
    os.replace(temp_file_path, file_path)
    
    print(f"Item '{item_name}' removed successfully.")

def print_csv_file(file_path):
    with open(file_path, 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            print(', $'.join(row))

edit_q()