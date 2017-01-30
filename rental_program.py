from inventory import *







def customer():
    print('Are you renting or returning an item? ')
    a = input("rent or reutrn\n")
    if a == "rent":
        rent()
    elif a == "return":
        return_item()
    

def rent():
    inv =  get_file_contents('inventory.csv')
    view_inv(inv)
    item = input("What will you be renting? Product name: ").strip().lower()
    Customer_choice = get_item_by_name( get_file_contents('inventory.csv'), item)
    print(Customer_choice.deposit_value, Customer_choice.price)
    print("You must place a deposit of" ,Customer_choice.deposit_value," dollars along with a fee of" ,Customer_choice.price,  " dollars every hour the item is rented. Deposits are refunded upon return.\n")
    print("Conform you purchase for\n", str(Customer_choice))
    confirmation = input('y/n')
    if confirmation == "y":
        update_inventory(Customer_choice.name, int(Customer_choice.quantity)- 1)
        # update_inventory(Customer_choice, Customer_choice.quantity)
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
    inv =  get_file_contents('inventory.csv')
    for item in inv:
        print("\n"+item[0])
    item = input("\nWhat item are you returning\n")
    returning_item = get_item_by_name( get_file_contents('inventory.csv'), item)
    hours = input("How many hours was the product rented? ")
    item_status = input("Is the product broken or damaged y/n? ")
    if item_status == "y":
        print("Your deposit will not be returned you owe the following:"+ str(returning_item.replacement_value) +" dollars for replacement of the item. and "+ str(int(returning_item.price) * int(hours)) + " for rent.")
    elif item_status == 'n':
        print("Your deposit will be returned you owe the following: "+ str(int(returning_item.price) * int(hours)) + " for rent.")
        update_inventory(returning_item.name, int(returning_item.quantity)+1)
        restart()
    else: 
        print('\nInvalid Input\n')
        return_item()

def start():
    print('Are you wanting to do a customer or manager action')
    action = input('c or m\n').strip().lower()
    if action == "c":
        customer()
    if action == "m":
        manager()
    
def manager():
        print("s to restart")
        print("Would you like to view current inventory or transaction history?")
        choice = input("i/t? \n").strip().lower()
        if choice == "i":
            inv =  get_file_contents('inventory.csv')
            view_inv(inv)
            manager()
        elif choice == "t":
            trans = get_file_contents('transaction.csv')
            view_trans(trans)
            manager()
        elif choice == "s":
            start()


    
    
start()
    
    
        # print("Are you renting or returning an item? ")
        # a = input('rent or return? \n').strip().lower()
        # if a == "rent":enumerate
        #     inv =  get_file_contents('inventory.csv')
        #     view_inv(inv)
        #     item = input("What will you be renting? Product name: ").strip().lower()
        #     a = get_item_by_name( get_file_contents('inventory.csv'), item)
        #     print("You must place a deposit of" ,a.deposit_value," dollars along with a fee of" ,a.price,  " dollars every hour the item is rented. Deposits are refunded upon return.\n")
        #     print("Conform you purchase for\n", str(a))
        #     input('y/n')












        # elif a == "return":
        #     ...
        # else:
        #     ...
        
     
    # elif action == "m":
     
    #     print('m')
    # else:
    #     print("invalid input")
    #     start()





