from Rental_classes import * 
import pytest





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


  