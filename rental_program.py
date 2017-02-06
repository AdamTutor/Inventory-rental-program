
"""
This module contains all functions that make up the rental program.
Each function represents a different choice in the program. The first function start() calles the first input in the
program and your choice will call the next part of the program. The program is mutually recursive.
"""

import datetime
from inventory import *
import sys
import os
from test_rental_classes import create_file


if os.path.isfile("inventory.csv") == False:
    create_file("inventory.csv")
    create_file('deposit.csv')
    create_file('revenue.csv')
    create_file('transaction.csv')
    write_row("inventory.csv", [['Ps4',400,40,3,24],['Xbox 1',20,25,3,250],['Gaming computer',1000,100,3,20], ['Ps4 controller',60,5,1,50], ['Xbox 1 controller',50,5,1,50], ['Standard headsets',80,8,0.25,20],['Premium headsets',200,20,0.75,20]])

def customer():
    "Determines all customer actions and takes inputs to complete them"
    print('Are you renting or returning an item? ')
    choice = input("rent or return\n").strip().lower()
    if choice == "rent":
        rent()
    elif choice == "return":
        return_item()
    elif choice == "q":
        print("System closing...")
        sys.exit()
    else:
        print("\nINVALID INPUT\n")
        print('did you mean rent or return? ')
        customer()


def rent():
    "Input determines what item is being rented"
    inv = get_file_contents('inventory.csv')
    print(view_inv(inv))
    item = input("What will you be renting? Product name: ").strip().capitalize()
    if item == "Q":
        print('System closing...')
        sys.exit()
    else:
        customer_choice = get_item_by_name(get_file_contents('inventory.csv'), item)
        if customer_choice == None:
            print("\nInvalid choice " + item + " is not in inventory\n")
            rent()
        else:
            print(customer_choice.deposit_value, customer_choice.price)
            print("You must place a deposit of $", customer_choice.deposit_value,\
                "along with a fee of $", customer_choice.price,\
                "every hour the item is rented. Deposits are refunded upon return.\n")
            print("Conform you purchase for\n", str(customer_choice))
            confirmation = input('y/n\n').strip().lower()
            if confirmation == "y":
                update_inventory(customer_choice.name, \
                int(customer_choice.quantity)- 1, 'inventory.csv')
                update_transaction(datetime.datetime.now(),\
                 customer_choice.name, "pending", 'transaction.csv')
                update_deposits(customer_choice.deposit_value, 'deposit.csv')
                restart()
            elif confirmation == "n":
                restart()
            elif confirmation == "q":
                print("System closing...")
                sys.exit()
            else:
                print('invalid entry')
                restart()


def restart():
    "Takes in user input to direct them to a different program section of their choice"
    print("\nType: rent to rent an item\nType: return to return an item\nType: start to restart program\nType: q to quit\n")
    choice = input().strip().lower()
    if choice == "rent":
        rent()
    elif choice == "return":
        return_item()
    elif choice == "start":
        start()
    elif choice == "q":
        print('System closing....')
    else:
        print("invalid input")
        restart()


def return_item():
    "contains inputs to determine how to calculate revenue on returned items"
    inv = get_file_contents('inventory.csv')
    for item in inv:
        print("\n"+item[0])
    item = input("\nWhat item are you returning\n").strip().capitalize()
    if item == 'Q':
        print("System closing....")
        sys.exit()
    else:
        returning_item = get_item_by_name(get_file_contents('inventory.csv'), item)
        if returning_item == None:
            print("Invalid Input " + item + " is not in inventory to be returned")
            return_item()
        else:
            hours = input("How many hours was the product rented? ").strip().lower()
            if hours == "q":
                print('System closing....')
                sys.exit()
            elif hours.isdigit():
                item_status = input("Is the product broken or damaged y/n? ").strip().lower()
                if item_status == "y":
                    print("Your deposit will not be returned you owe the following:"+ \
                            str(returning_item.replacement_value) +\
                            " dollars for replacement of the item. and "\
                            + "$" + str(int(returning_item.price) * int(hours)) + " for rent.")
                    rent_amount = int(returning_item.price) * int(hours)
                    sales_tax = rent_amount * 0.07
                    update_revenue(rent_amount, sales_tax, 'revenue.csv')
                    update_transaction(datetime.datetime.now(), returning_item.name, \
                    "compensated", 'transaction.csv')
                    restart()
                elif item_status == 'n':
                    print("Your deposit will be returned you owe the following: $"+ \
                    str(int(returning_item.price) * int(hours)) + " for rent.")

                    update_inventory(returning_item.name, int(returning_item.quantity)+1, 'inventory.csv')
                    rent_amount = int(returning_item.price) * int(hours)
                    sales_tax = rent_amount * 0.07
                    update_revenue(rent_amount, sales_tax, 'revenue.csv')
                    update_transaction(datetime.datetime.now(), returning_item.name, \
                    "returned", 'transaction.csv')
                    restart()
                elif item_status == "q":
                    print('System closing....')
                else:
                    print('\nInvalid Input\n')
                    return_item()

            else:
                print('invalid input')
                print('hours must be a number')
                return_item()

def start():
    "Initialized program start"
    
    print('At anytime q will exit program')
    action = input('Are you a customer or manager\n').strip().lower()
    if action == "customer":
        customer()
    elif action == "manager":
        manager()
    elif action == "q":
        print('System closing....')
        sys.exit()
    else:
        print("\nINVALID INPUT\n")
        start()


def manager():
    "Inputs for all manager actions"
    choice = input('Type: i to view inventory\nType: t to view transaction history\nType: r to view revenue\nType: Replace to add a replacement item to inventory.\nType: s to restart\n').strip().lower()
    if choice == "i":
        inv = get_file_contents('inventory.csv')
        print(view_inv(inv))
        manager()
    elif choice == "t":
        trans = get_file_contents('transaction.csv')
        print(view_trans(trans))
        manager()
    elif choice == "r":
        trans = get_file_contents('revenue.csv')
        rev = view_revenue('revenue.csv', 'deposit.csv')
        print(rev[0], rev[1], "\n" + rev[2], rev[3], "\n" + rev[4], rev[5], "\n"+ rev[6], rev[7])
        manager()
    elif choice == 'rq':
        name = input("Product being replaced: ").strip().capitalize()
        quantity = input("How many? ").strip()
        if quantity.isdigit() != True:
            print("invalid input")
            manager()
        if name == "q" or quantity == "q":
            print('System closing...')
            sys.exit()
        inv = get_file_contents("inventory.csv")
        item = get_item_by_name(inv, name)
        if item == None:
            print('invaid input')
            manager()
        update_inventory(name, int(item.quantity)+int(quantity), 'inventory.csv')
        print("\nInventory has been updated\n")
        manager()
    elif choice == "s":
        start()
    elif choice == "q":
        print('System closing....')
        sys.exit()
start()
