import csv
from Rental_classes import *


def get_file_contents(filename):
    """ (file_obj) --> (list)
    Takes in a csv file as a parameter and reads 
    the file and outputs a cvs.reader object that is converted to a list of lists."""
    content_list = []
    with open(filename, newline='') as inv:
    #csv.reader(file to be read, singe character to seperate feilds, A one-character string used to quote fields containing special characters)
        content = csv.reader(inv, delimiter=',', quotechar='|')
        # returns list of lists from reader object. 
        return list(content)


def get_item_by_name(inventory_list, name):
    """ (list(list), str) --> (Item)
    Searches for item in inventory by name and converts item in to Item object.
    """
    #initializes customer_item variable
    customer_item = ''
    for i in inventory_list:
        # Checks if the name of a Item object is = to the name paramater
            customer_item = Item(i[0], i[1], i[2], i[3], i[4])
            return customer_item

def view_trans(trans_list):
    """(list(list), str) --> (Item)
    Searches for item in inventory by name and converts item in to Item object."""
    transaction = ''
    for transaction in trans_list:
        print("\nDatetime: " + transaction[0], "\nItem:", transaction[1], "\nstatus", transaction[2])
        

def view_inv(inventory_list):
    """ (list) --> none
    Takes in a list of Items and prints all attribues out for each Item in the list"""
    for item in inventory_list:
        print('\nProduct: ' + item[0], '\ndeposit: ' ,item[1], "\nprice per hour: ",item[2], '\ncurrent stock: ', item[3], "\n")


def update_inventory(name, quantity):
    """ (str, int) --> none
    takes in a name as a str and a quantity as a integer. Searches Inventory file for a item where that item's name matches the parameter. The item with that
    name is has its quantity overwritten and the new data is rewritten over inventory file. """
        Item_obj_l = []
        inv =  get_file_contents('inventory.csv')
        for i in inv:
            Item_obj_l.append(Item(i[0],i[1],i[2],i[3],i[4]))
        for i in Item_obj_l:
            if i.name == name:
                i.quantity = quantity
        file = open('inventory.csv', 'w')
        writer = csv.writer(file, delimiter=',')
        for i in Item_obj_l:
            writer.writerow([i.name, i.replacement_value, i.deposit_value, i.price, i.quantity]) 
        file.close()

def update_transaction(date, item, status):
    """ (Datetime, Item_obj, str) --> none
    Takes in a datetime, Item object and status. That data is appended to transaction.csv file"""
    with open('transaction.csv','a',newline='') as f:
        writer=csv.writer(f)
        writer.writerow([date,item, status])
    with open('transaction.csv') as f:
        print(f.read())
       








