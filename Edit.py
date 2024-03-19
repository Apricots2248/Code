import os
import sys
import csv

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def edit_q():
    choice = input("Would you like to Add item(1), Edit item(2), Remove item(3): ")
    if choice == '1':
