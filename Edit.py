import csv
import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

file_path = os.path.join('ProductStock.csv')

def edit_q():
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
    elif choice == '4':
            print('done')
            clear_terminal()
    else:
        print('invalid input')
        edit_q()

def add_item():
    print_csv_file('ProductStock.csv')
    item = input("Item name: ").capitalize()  
    price = input("Item price: ")
    if price.isalpha():
        clear_terminal()
        print('Invalid inout, Item Price must be a number, Try again')
        add_item()

    with open(file_path, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([item, price])

def edit_item():
    choice = input("would you like to edit Name(1), or Price (2): ")
    if choice == '1':
        clear_terminal()
        edit_item_name()
    elif choice == '2':
        clear_terminal()
        edit_item_price()
    else:
        clear_terminal()
        print('invalid input')
        edit_item()
        
def edit_item_name():
    print_csv_file('ProductStock.csv')
    item_name = input("Enter the name of the item to edit: ")
    new_name = input("Enter the new name: ")
    file_path = 'ProductStock.csv'
    temp_file_path = 'temp_ProductStock.csv'
    
    # Read the CSV file and store data in a list
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
    
    # Find and update the item's price
    for row in rows:
        if row[0] == item_name:
            row[0] = new_name
            break
    
    # Write the modified data back to a temporary file
    with open(temp_file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows)
    
    # Replace the original file with the temporary file
    os.replace(temp_file_path, file_path)
    
    print(f"Item '{item_name}' updated successfully.")

def edit_item_price():
    print_csv_file('ProductStock.csv')
    item_name = input("Enter the name of the item to edit: ")
    new_price = input("Enter the new price: ")
    file_path = 'ProductStock.csv'
    temp_file_path = 'temp_ProductStock.csv'
    
    # Read the CSV file and store data in a list
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
    
    # Find and update the item's price
    for row in rows:
        if row[0] == item_name:
            row[1] = new_price
            break
    
    # Write the modified data back to a temporary file
    with open(temp_file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows)
    
    # Replace the original file with the temporary file
    os.replace(temp_file_path, file_path)
    
    print(f"Item '{item_name}' updated successfully.")


def remove_item():
    print_csv_file('ProductStock.csv')
    item_name = input("Enter the name of the item to remove: ").lower().capitalize()
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
clear_terminal()
edit_q()