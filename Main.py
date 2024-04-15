import os
import csv

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')



def main():
    while True:
        choice = input("Would you like to Edit items(1), Process Purchase(2), Veiw Items(3), Quit(4): ")
        clear_terminal()
        if choice == '1':
            import Edit
            Edit.edit_q()
        elif choice == '2':
            import Purchase
            Purchase.get_item()
        elif choice == '3':
            print_csv_file('productStock.csv')
            input("press anything when done veiwing: ")
            clear_terminal()
        elif choice == '4':
            print ('Toodles')
            break
        else:
            (print('Invalid input, Try again'))
            main()

def print_csv_file(file_path):
    with open(file_path, 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            print(', $'.join(row))
            
clear_terminal()
main()