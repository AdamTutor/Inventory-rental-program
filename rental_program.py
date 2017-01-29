from inventory import *



def program():
    print('Are you wanting to do a customer or manager action')
    action = input('c or m\n').strip().lower()
    if action == "c":
        print("Are you renting or returning an item? ")
        a = input('rent or return? \n').strip().lower()
        if a == "rent":
            inv = get_inv('inventory.csv')
            view_inv(inv)
            item = input("What will you be renting? Product name: ").strip().lower()
            get_item_by_name(get_inv('inventory.csv'), item)

        
        # elif a == "return":
        #     ...
        # else:
        #     ...
        
     
    elif action == "m":
     
        print('m')
    else:
        print("invalid input")
        program()


program()



