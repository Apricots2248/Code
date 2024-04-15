import csv 
import os
import sys

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_csv_file(file_path):
    with open(file_path, 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            print(', $'.join(row))

total_amount_overall = 0
receipt_items = []

def get_item():
    
    global total_amount_overall
    global receipt_items

    while True:# Prompt the user to enter a keyword and column number 
        print_csv_file('ProductStock.csv')
        Name = input("Enter Product: ").lower().capitalize()
        column_num = 0

        # Open the CSV file 
        with open('ProductStock.csv', 'r') as csvfile: 
            # Create a CSV reader object 
            reader = csv.reader(csvfile)
            found = False
            # Loop through each row in the CSV file 
            for row in reader: 
                # Check if the keyword is in the specified column 
                if Name in row[column_num]:
                    try:
                        amt = float(input("Enter item Amount:"))                        
                    except:
                        clear_terminal()
                        print("invalid input")
                        return      
                    total_amount = amt * float(row[1])           
                    print("Current item $ amount:", total_amount)
                    total_amount_overall += total_amount
                    found = True
                    receipt_items.append((Name, amt, total_amount))  # Add item details to receipt
            if not found:
                print("Product not found")        
            
        
        while True:
            choice = input("Would you like to add another item? (Y/N): ").upper()
            clear_terminal()
            if choice == 'Y' or choice == 'N':
                break
            else:
                print("Invalid input, Please enter 'Y' or 'N'")

        if choice.upper() == 'N':  # Corrected the comparison
            receipt()


def receipt():
    global total_amount_overall
    global receipt_items
    # Display receipt
    print("\nReceipt:")
    for item in receipt_items:
        print(f"{item[0]} x{item[1]}: ${item[2]}")
    print("Overall $ amount: ", total_amount_overall)
    sys.exit()



get_item()