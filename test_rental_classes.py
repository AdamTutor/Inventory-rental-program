from Rental_classes import * 
import pytest
import os
import datetime
import csv
from inventory import *



 # Testing all attributes for Test class
class Test_Item():
    def test_class_Item(self):
        i = Item('ps4', 400, 40, 3,20)
        assert i.name == 'ps4'
        assert i.replacement_value == 400
        assert i.deposit_value == 40
        assert i.price == 3
        assert i.quantity == 20

    def test_in_stock(self):
         a = Item('ps4', 400, 40, 3,0)
         i = Item('ps4', 400, 40, 3,20)
         assert i.in_stock() == True
         assert a.in_stock() == False



class Test_Transaction():
    def test_class_Transaction(self):
        T = Transaction(71017, 'ps4', 'pending')
        assert T.Datetime == 71017
        assert T.Item == 'ps4'
        assert T.status == 'pending'


def test_get_file_contents():
    with open("test.csv", 'w') as t:
         writer=csv.writer(t)
         writer.writerow(['TEST','Test', 'test'])
         t.close()
    Test_inventory = get_file_contents('test.csv')
    assert Test_inventory[0][0] == 'TEST'
    assert Test_inventory[0][1] == 'Test'
    assert Test_inventory[0][2] == 'test'
    os.remove('test.csv')


def test_get_item_by_name():
     with open("test.csv", 'w') as t:
         writer=csv.writer(t)
         writer.writerow(['ps4', 400, 40, 3,20])
         writer.writerow(['xbox1', 400, 40, 3,20])
         writer.writerow(['TEST', 400, 40, 3,20])
     test_inventory = get_file_contents('test.csv')
     name = get_item_by_name(test_inventory, 'ps4')
     t = get_item_by_name(test_inventory, 'xbox1')
     test = get_item_by_name(test_inventory,'TEST')
     assert name.name == 'ps4'
     assert t.name == 'xbox1'
     assert test.name == 'TEST'
     os.remove("test.csv")
 

def test_update_inventory():
    with open("test.csv",'w') as f:
        f.close()
    name = "name"
    quantity = 3
    filename = 'test.csv'
    x = update_inventory(name, quantity, filename)
    assert x == True



def test_update_transaction():
    date = 'date'
    item = 'item'
    status = 'status'
    with open('test.csv','a',newline='') as f:
        writer=csv.writer(f)
        writer.writerow([date,item, status])
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





    

    
    