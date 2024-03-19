import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        choice = input("Would you like to Edit items(1), Process Purchase(2): ")
        clear_terminal()
        if choice == '1':
            pass
        elif choice == '2':
            import Purchase
            Purchase.get_item()
        else:
            (print('Invalid input, Try again'))
            

main()