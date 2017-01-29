import csv
from Rental_classes import *


def get_inv(filename):
    """Takes in a csv file as a parameter and reads 
    the file and outputs a cvs.reader object that is converted to a list of lists."""
    inventory_list = []
    with open(filename, newline='') as inv:
    #csv.reader(file to be read, singe character to seperate feilds, A one-character string used to quote fields containing special characters)
        inventory = csv.reader(inv, delimiter=',', quotechar='|')
        # returns list of lists from reader object. 
        return list(inventory)

def get_item_by_name(inventory_list, name):
    print(inventory_list, name)
    for i in inventory_list:
        print(Item(i[0], i[1], i[2], i[3]), i[4])
        # print(Item(i[0]))
        # if Item(i[0].split()).name == name: 
        #     customer_item = i
        #     print(customer_item)
        # return(customer_item)
    


def view_inv(inventory_list):
    for item in inventory_list:
        print('\nProduct: ' + item[0], '\ndeposit: ' ,item[1], "\nprice per hour: ",item[2], '\ncurrent stock: ', item[3], "\n")


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
   



