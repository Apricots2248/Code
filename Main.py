import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        choice = input("Would you like to Edit items(1), Process Purchase(2), Quit(3): ")
        clear_terminal()
        if choice == '1':
            import Edit
            Edit.edit_q()
        elif choice == '2':
            import Purchase
            Purchase.get_item()
        elif choice == '3':
            print ('Bye')
            break
        else:
            (print('Invalid input, Try again'))
            

main()