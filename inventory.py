import csv


def get_inv(filename):
    inventory_list = []
    with open(filename, newline='') as inv:
        inventory = csv.reader(inv, delimiter=' ', quotechar='|')
        for row in inventory:
            item = ', '.join(row)
            inventory_list.append(item)
    return inventory_list


def view_inv(inventory_list):
    for item in inventory_list:
        item = item.split(",")
        print(item)

view_inv(get_inv('inventory.csv'))

