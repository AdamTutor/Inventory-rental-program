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
    Test_inventory = get_file_contents('test.csv')
    assert Test_inventory[0][0] == 'TEST'
    assert Test_inventory[0][1] == 'Test'
    assert Test_inventory[0][2] == 'test'
    os.remove('test.csv')




    

    
    