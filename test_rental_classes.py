from Rental_classes import * 
import pytest






 # Testing all attributes for Test class
class Test_Item():

    def test_item_rented(self):
        item = Item('Ps4',400,40,3,20)
        original_quantity = item.quantity
        item.item_rented()
        assert item.quantity == original_quantity - 1


    def test_item_returned(self):
        item = Item('Ps4',400,40,3,20)
        original_quantity = item.quantity
        item.item_returned()
        assert item.quantity == original_quantity + 1
