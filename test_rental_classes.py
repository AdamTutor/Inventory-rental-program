from Rental_classes import *
import pytest
import os
import datetime
import csv
from inventory import *




# # Helper functions for testing.
def create_file(filename):
    "creates a file called test.csv"
    with open(filename, 'w') as tfile:
        return tfile.close()



 # Testing all attributes for Test class
class Test_Item():
    def test_class_Item(self):
        i = Item('ps4', 400, 40, 3, 20)
        assert i.name == 'ps4'
        assert i.replacement_value == 400
        assert i.deposit_value == 40
        assert i.price == 3
        assert i.quantity == 20
        assert str(i) ==  "product: " + 'ps4' + "\nreplacement value: " + '400' + \
              "\nDeposit value: " + '40'+ "\nprice: " + \
                '3'+ "\nquantity: " + '20'

    



class Test_Transaction():
    def test_class_transaction(self):
        trans = Transaction(71017, 'ps4', 'pending')
        assert trans.datetime == 71017
        assert trans.item == 'ps4'
        assert trans.status == 'pending'
        assert str(trans) == "date: " + '71017' + " Item " + 'ps4' + " status " + 'pending'

# Tests that create or read files
def test_create_file():
    'Tests that create_file() function creates a empty file'
    create_file('test.csv')
    assert os.path.isfile("test.csv")


def test_get_file_contents():
    "tests that get_file_contents() reads and returns the content of a file in a list of lists"
    create_file('test.csv')
    write_row('test.csv', [['TEST', 'Test', 'test']])
    Test_inventory = get_file_contents('test.csv')
    assert Test_inventory[0][0] == 'TEST'
    assert Test_inventory[0][1] == 'Test'
    assert Test_inventory[0][2] == 'test'
    os.remove('test.csv')


def test_get_item_by_name():
    create_file("test.csv")
    write_row("test.csv", [['ps4', 400, 40, 3, 20], \
            ['xbox1', 400, 40, 3, 20], ['TEST', 400, 40, 3, 20]])
    test_inventory = get_file_contents('test.csv')
    name = get_item_by_name(test_inventory, 'ps4')
    xbox = get_item_by_name(test_inventory, 'xbox1')
    test = get_item_by_name(test_inventory, 'TEST')
    not_an_item = get_item_by_name(test_inventory, 'notanitem')
    assert name.name == 'ps4'
    assert xbox.name ==  'xbox1'
    assert test.name == 'TEST'
    assert not_an_item == None
    
    os.remove("test.csv")




# Tests functions that update or change files
def test_update_inventory():
    create_file('test.csv')
    write_row('test.csv', [['test', 0, 0, 0, 0]])
    name = "test"
    quantity = 3 -1
    filename = 'test.csv'
    inv = update_inventory(name, quantity, filename)
    assert inv == "test,0,0,0,2\n"
    os.remove('test.csv')



def test_update_transaction():
    create_file('test.csv')
    date = 'date'
    item = 'item'
    status = 'status'
    filename = 'test.csv'
    trans = update_transaction(date, item, status, filename)
    assert trans == 'date,item,status\n'
    os.remove('test.csv')

    


def test_update_revenue():
    create_file('test.csv')
    rent = '300'
    sales = '300'
    filename = 'test.csv'
    x = update_revenue(rent, sales, filename)
    assert x == '300,300\n'
    os.remove("test.csv")


def test_update_deposits():
    deposit = 20
    test = update_deposits(deposit, 'test.csv')
    assert test == '20\n'
    return_deposits('20', 'test.csv')
    assert len(get_file_contents('test.csv')) == 0
    return_deposits('20', 'test.csv')
    os.remove('test.csv')




def test_view_inv():
    inv = [['ps4', '100', '20', '20','20']]
    test = view_inv(inv)
    assert test == ('\nProduct: ' + 'ps4' + '\nreplacement value: '+ "$" + '100' + '\ndeposit: '+\
                     "$" + '20' +"\nprice per hour: "+ "$" + '20' + '\ncurrent stock: '+ '20' + "\n")


def test_view_trans():
    trans = [['2017-01-30 14:37:54.026520','xbox1','pending']]
    test = view_trans(trans)
    assert test == ("\nDatetime: " + '2017-01-30 14:37:54.026520' + "\nItem:" + 'xbox1' + \
                                         "\nstatus " + 'pending' + "\n")


def test_view_revenue():
    create_file('test.csv')
    create_file('test2.csv')
    test = view_revenue('test.csv', 'test2.csv')
    assert test == ("All current pending deposits: " + "$", 0, "total w/o tax: $",0, "sales tax: $", 0, "total: $", 0)
    write_row("test.csv", [[90000, 38.0]])
    write_row("test2.csv", [[20],[20],[20],[20]])
    test2 = view_revenue('test.csv', 'test2.csv')
    assert test2 == ("All current pending deposits: " + "$", 80, "total w/o tax: $",90000, "sales tax: $", 38.0, "total: $", 90038.0)
    os.remove("test.csv")
    os.remove("test2.csv")


def test_write_row():
    create_file('test.csv')
    write_row('test.csv', [['TEST', 'TEST', 'TEST'], ['TEST', 'TEST', 'TEST']])
    with open('test.csv') as file:
        content = file.read()
    assert content == ('TEST,TEST,TEST\nTEST,TEST,TEST\n')
    os.remove("test.csv")


   

    




