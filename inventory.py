import csv
from Rental_classes import *


def get_inv(filename):
    """Takes in a csv file as a parameter and reads 
    the file and outputs a cvs.reader object that is converted to a list of lists."""
    inventory_list = []
    with open(filename, newline='') as inv:
    #csv.reader(file to be read, singe character to seperate feilds, A one-character string used to quote fields containing special characters)
        inventory = csv.reader(inv, delimiter=' ', quotechar='|')
        # returns list of lists from reader object. 
        return list(inventory)


def view_inv(inventory_list):
    for item in inventory_list:
        print(item[0].split()[0])

# view_inv(get_inv("inventory.csv"))


def update_inventory():
    with open("inventory.csv", "a", newline='') as myfile:
    
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        name = 'ps4'
        replacement_value = 400
        deposit_value = 40
        price = 3
        quanity = 20
        wr.writerow([name, replacement_value, deposit_value, price, quanity])


# with open('inventory.csv', newline='') as inv:
#         inventory = csv.reader(inv, delimiter=' ', quotechar='|')
#         l = list(inventory)
#         print(l[0][0].split(",")[0])
   


l = get_inv('inventory.csv')
print(l)