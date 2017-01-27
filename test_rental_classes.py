from Rental_classes import * 
import pytest






 # Testing all attributes for Test class
class Test_Item():


    def test_get_name(self):
        item = Item('Ps4',400,40,3,20)
        assert item.get_name() == 'Ps4'
    

    def test_get_replacement_value(self):
        item = Item('Ps4',400,40,3,20)
        assert item.get_replacement_value() == 400


    def test_get_deposit_value(self):
        item = Item('Ps4',400,40,3,20)
        assert item.get_deposit_value() == 40


    def test_get_price(self):
        item = Item('Ps4',400,40,3,20)
        assert item.get_price() == 3


    def test_get_quantity(self):
        item = Item('Ps4',400,40,3,20)
        assert item.get_quantity() == 20


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
