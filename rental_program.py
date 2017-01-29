from inventory import *


def customer():
    print('Are you renting or returning an item? ')
    a = input("rent or reutrn\n")
    if a == "rent":
        rent()
    

def rent():
    inv = get_inv('inventory.csv')
    view_inv(inv)
    item = input("What will you be renting? Product name: ").strip().lower()
    a = get_item_by_name(get_inv('inventory.csv'), item)
    print("You must place a deposit of" ,a.deposit_value," dollars along with a fee of" ,a.price,  " dollars every hour the item is rented. Deposits are refunded upon return.\n")
    print("Conform you purchase for\n", str(a))
    input('y/n')

def  start():
    print('Are you wanting to do a customer or manager action')
    action = input('c or m\n').strip().lower()
    if action == "c":
        customer()
    
def manager()
    
    
    
    
    
        # print("Are you renting or returning an item? ")
        # a = input('rent or return? \n').strip().lower()
        # if a == "rent":
        #     inv = get_inv('inventory.csv')
        #     view_inv(inv)
        #     item = input("What will you be renting? Product name: ").strip().lower()
        #     a = get_item_by_name(get_inv('inventory.csv'), item)
        #     print("You must place a deposit of" ,a.deposit_value," dollars along with a fee of" ,a.price,  " dollars every hour the item is rented. Deposits are refunded upon return.\n")
        #     print("Conform you purchase for\n", str(a))
        #     input('y/n')












        # elif a == "return":
        #     ...
        # else:
        #     ...
        
     
    elif action == "m":
     
        print('m')
    else:
        print("invalid input")
        start()

start()



