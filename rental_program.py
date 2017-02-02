
"""
This module contains all functions that make up the rental program. 
Each function represents a different choice in the program. The first function start() calles the first input in the
program and your choice will call the next part of the program. The program is mutually recursive. 
"""


from inventory import *
import datetime


def customer():
    print('Are you renting or returning an item? ')
    choice = input("rent or reutrn\n")
    if choice == "rent":
        rent()
    elif choice == "return":
        return_item()
    else:
        print("\nINVALID INPUT\n")
        print('did you mean rent or return? ')
        customer()


def rent():
    inv = get_file_contents('inventory.csv')
    print(view_inv(inv))
    item = input("What will you be renting? Product name: ").strip().lower()
    customer_choice = get_item_by_name(get_file_contents('inventory.csv'), item)
    print(customer_choice.deposit_value, customer_choice.price)
    print("You must place a deposit of", customer_choice.deposit_value,\
         " dollars along with a fee of", customer_choice.price,\
         " dollars every hour the item is rented. Deposits are refunded upon return.\n")
    print("Conform you purchase for\n", str(customer_choice))
    confirmation = input('y/n')
    if confirmation == "y":
        update_inventory(customer_choice.name, int(customer_choice.quantity)- 1, 'inventory.csv')
        update_transaction(datetime.datetime.now(), customer_choice.name, "pending", 'transaction.csv')
        update_deposits(customer_choice.deposit_value, 'deposit.csv')
        restart()
    elif confirmation == "n":
        restart()
    else:
        print('invalid entry')
        restart()


def restart():
    choice = input("k to keep shopping, s to start over, q to quit ?\n")
    if choice == "k":
        rent()
    elif choice == "s":
        start()
    elif choice == "q":
        print('System closing....')
    else:
        print("invalid input")
        restart()


def return_item():
    inv = get_file_contents('inventory.csv')
    for item in inv:
        print("\n"+item[0])
    item = input("\nWhat item are you returning\n")
    returning_item = get_item_by_name(get_file_contents('inventory.csv'), item)
    hours = input("How many hours was the product rented? ")
    item_status = input("Is the product broken or damaged y/n? ")
    if item_status == "y":
        print("Your deposit will not be returned you owe the following:"+ \
                str(returning_item.replacement_value) +" dollars for replacement of the item. and "\
                + str(int(returning_item.price) * int(hours)) + " for rent.")
        rent_amount = int(returning_item.price) * int(hours)
        sales_tax = rent_amount * 0.07
        update_revenue(rent_amount, sales_tax, 'revenue.csv')
        update_transaction(datetime.datetime.now(), returning_item.name, "compensated",'transaction.csv')
        restart()
    elif item_status == 'n':
        print("Your deposit will be returned you owe the following: "+ \
        str(int(returning_item.price) * int(hours)) + " for rent.")

        update_inventory(returning_item.name, int(returning_item.quantity)+1, 'inventory.csv')
        rent_amount = int(returning_item.price) * int(hours)
        sales_tax = rent_amount * 0.07
        update_revenue(rent_amount, sales_tax, 'revenue.csv')
        update_transaction(datetime.datetime.now(), returning_item.name, "returned", 'transaction.csv')
        restart()
    else:
        print('\nInvalid Input\n')
        return_item()


def start():
    print('Are you wanting to do a customer or manager action')
    action = input('c or m\n').strip().lower()
    if action == "c":
        customer()
    elif action == "m":
        manager()
    else:
        print("\nINVALID INPUT\n")
        start()


def manager():
    print("s to restart")
    print("Would you like to view current inventory , transaction history or revenue?")
    choice = input("i/t/r? \n").strip().lower()
    if choice == "i":
        inv = get_file_contents('inventory.csv')
        print(view_inv(inv))
        manager()
    elif choice == "t":
        trans = get_file_contents('transaction.csv')
        view_trans(trans)
        manager()
    elif choice == "r":
        trans = get_file_contents('revenue.csv')
        x = view_revenue('revenue.csv', 'deposit.csv')
        print(x[0], x[1], "\n" + x[2], x[3], "\n" + x[4], x[5], "\n"+ x[6], x[7])
        manager()
    elif choice == "s":
        start()


start()
