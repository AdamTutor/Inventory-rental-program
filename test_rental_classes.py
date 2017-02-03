from Rental_classes import * 
import pytest
import os
import datetime
import csv
from inventory import *

# Helper functions for mocking up files needed to test
def write_row(filename, values_to_write):
    """ (file, list) --> None
    Takes in a filename and list of data to be written in a row on the file.
    """
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        for row in values_to_write:
            writer.writerow(row)
    with open(filename) as file:
        content = file.read()
        if len(content) > 0:
            return True


def create_file(filename):
    "creates a file called test.csv"   
    with open(filename, 'w') as tfile:
        return tfile.close()



 # Testing all attributes for Test class
class Test_Item():
    def test_class_Item(self):
        i = Item('ps4', 400, 40, 3,20)
        assert i.name == 'ps4'
        assert i.replacement_value == 400
        assert i.deposit_value == 40
        assert i.price == 3
        assert i.quantity == 20
        assert str(i) ==  "product: " + 'ps4' + "\nreplacement value: " + '400'+\
              "\nDeposit value: " + '40'+ "\nprice: " + \
                '3'+ "\nquantity: " + '20'

    def test_in_stock(self):
         a = Item('ps4', 400, 40, 3,0)
         i = Item('ps4', 400, 40, 3,20)
         assert i.in_stock() == True
         assert a.in_stock() == False



class Test_Transaction():
    def test_class_Transaction(self):
        T = Transaction(71017, 'ps4', 'pending')
        assert T.datetime == 71017
        assert T.item == 'ps4'
        assert T.status == 'pending'
        assert str(T) == "date: " + '71017' + " Item " + 'ps4' + " status " + 'pending'


def test_get_file_contents():
    create_file('test.csv')
    write_row('test.csv', [['TEST','Test', 'test']])
    Test_inventory = get_file_contents('test.csv')
    assert Test_inventory[0][0] == 'TEST'
    assert Test_inventory[0][1] == 'Test'
    assert Test_inventory[0][2] == 'test'
    os.remove('test.csv')


def test_get_item_by_name():
    create_file("test.csv")
    write_row("test.csv", [['ps4', 400, 40, 3,20],['xbox1', 400, 40, 3,20],['TEST', 400, 40, 3,20]])
    test_inventory = get_file_contents('test.csv')
    name = get_item_by_name(test_inventory, 'ps4')
    t = get_item_by_name(test_inventory, 'xbox1')
    test = get_item_by_name(test_inventory,'TEST')
    assert name.name == 'ps4'
    assert t.name == 'xbox1'
    assert test.name == 'TEST'
    os.remove("test.csv")
 

def test_update_inventory():
    create_file('test.csv')
    name = "name"
    quantity = 3
    filename = 'test.csv'
    x = update_inventory(name, quantity, filename)
    assert x == True
    os.remove('test.csv')



def test_update_transaction():
    date = 'date'
    item = 'item'
    status = 'status'
    with open('test.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([date, item, status])
    with open('transaction.csv') as f:
        test = f.read()
        test[0] == 'date'
        test[1] == 'item'
        test[2] == 'status'
    os.remove('test.csv')


def test_update_revenue():
    with open("test.csv", 'w') as f:
        f.close()
    rent = '300'
    sales = '300'
    filename = 'test.csv'
    x = update_revenue(rent, sales, filename)
    assert x == True
    os.remove("test.csv")


def test_update_deposits():
    deposit = 20
    test = update_deposits(deposit, 'test.csv')
    assert test == True
    os.remove('test.csv')


def test_view_inv():
    inv = [['ps4', '100', '20', '20','-18']]
    test = view_inv(inv)
    assert test == ('\nProduct: ' + 'ps4'+ '\nreplacement value: '+ '100' + '\ndeposit: '+\
                     '20'+ "\nprice per hour: "+ '20' + '\ncurrent stock: '+ '-18' + "\n")


def test_view_trans():
    trans = [['2017-01-30 14:37:54.026520','xbox1','pending']]
    test = view_trans(trans)
    assert test == ("\nDatetime: " +'2017-01-30 14:37:54.026520' + "\nItem:" + 'xbox1' + \
                                         "\nstatus" + 'pending' + "\n")


# def test_view_revenue():
#     rev = [[999,69.93]]
#     file1 = 'revenue.csv'
#     file2 = 'deposit.csv'
#     test = view_revenue(file1, file2)
#     assert test == "All current pending deposits: ", deposit_total, "total w/o tax:",\
#      total, "sales tax: ", tax, "total: ", final_total






