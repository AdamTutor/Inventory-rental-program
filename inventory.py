import csv
from Rental_classes import *


def get_file_contents(filename):
    """ (file_obj) --> (list)
    Takes in a csv file as a parameter and reads
    the file and outputs a cvs.reader object that is converted to a list of lists."""

    with open(filename, newline='') as inv:
    #csv.reader(file to be read, singe character to seperate feilds,
    #  A one-character string used to quote fields containing special characters)
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
        if customer_item.name == name:
            return customer_item


def view_trans(trans_list):
    """(list) --> None
    Takes in a list of data representing transactions and displays them in a human readable format.
    """
    # Pulls transaction data from a list of lists and prints it
    for transaction in trans_list:
        print("\nDatetime: " + transaction[0], "\nItem:", transaction[1],\
                                         "\nstatus", transaction[2], "\n")


def view_inv(inventory_list):
    """ (list) --> none
    Takes in a list of Items and prints all attribues out for each Item in the list"""
    # Pulls inventory data from a list of lists and prints it
    for item in inventory_list:
        print('\nProduct: ' + item[0], '\nreplacement value: ', item[1], '\ndeposit: ',\
                     item[2], "\nprice per hour: ", item[3], '\ncurrent stock: ', item[4], "\n")


def update_inventory(name, quantity, filename):
    """ (str, int) --> none
    takes in a name as a str and a quantity as a integer. Searches Inventory file
    for a item where that item's name matches the parameter. The item with that
    name is has its quantity overwritten and the new data is rewritten over inventory file. """
    Item_obj_l = []
    # fetches all inventory items and stores them in 'inv'
    inv = get_file_contents(filename)
    # creates a Item objects from all items in 'inv'
    for i in inv:
        Item_obj_l.append(Item(i[0], i[1], i[2], i[3], i[4]))
    # sets the object's quantity as the parameter quantity where
    #  the object name is the smae as the parameter name
    for i in Item_obj_l:
        if i.name == name:
            i.quantity = quantity
    # opens and clears the inventory file
    file = open(filename, 'w')
    writer = csv.writer(file, delimiter=',')
    # rewrites the existing data along with the updated quanitity on Item Obj.
    for i in Item_obj_l:
        writer.writerow([i.name, i.replacement_value, i.deposit_value, i.price, i.quantity])
    file.close()
    with open(filename) as file:
        inv = file.read()
        if len(inv) == 0:
            return True


def update_transaction(date, item, status, filename):
    """ (Datetime, Item_obj, str) --> none
    Takes in a datetime, Item object and status. That data is appended to transaction.csv file"""
    return write_row(filename, [date, item, status])


def update_revenue(rent, sales_tax, filename):
    """ (int, int) --> none
 Takes in the amount a person paid on rent plus the taxes of that sale"""
 # opens revenue file in append mode and appends new deposit to file
    return write_row(filename, [rent, sales_tax])

def write_row(filename, values_to_write):
    """ (file, list) --> None
    Takes in a filename and list of data to be written in a row on the file.
    """
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(values_to_write)
    with open(filename) as file:
        content = file.read()
        if len(content) > 0:
            return True


def update_deposits(deposit, filename):
    """ (int) --> none
 Takes in the deposit amount from a sale and writes it to a file"""
    return write_row(filename, [deposit])


def view_revenue():
    """Reads all files pertaining to income and money loss or
     gain and displays them in a human readable format"""
    revenue_list = []
    tax_list = []
    deposits_list = []
    rev = get_file_contents('revenue.csv')
    # Pulls data from files and stores them in lists. Gets the sum
    #  of those lists to do calculations for sales tax and total profit
    for i in rev:
        revenue_list.append(int(i[0]))
        tax_list.append(float(i[1]))
        total = sum(revenue_list)
        tax = sum(tax_list)
        final_total = total + tax
    deposits = get_file_contents('deposit.csv')
    # Reads deposit fle and collects total deposits
    for deposit in deposits:
        deposits_list.append(int(deposit[0]))
    deposit_total = sum(deposits_list)
    print("All current pending deposits: ", deposit_total)
    print("total w/o tax:", total)
    print("sales tax: ", tax)
    print("total: ", final_total)







