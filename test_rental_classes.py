from Rental_classes import * 
import pytest


item = Item('Ps4',400,40,3,20)




 # Testing all attributes for Test class
class Test_Item():


    def test_get_name(self):
        assert item.get_name() == 'Ps4'
    

    def test_get_replacement_value(self):
        assert item.get_replacement_value() == 400


    def test_get_deposit_value(self):
        assert item.get_deposit_value() == 40


    def test_get_price(self):
        assert item.get_price() == 3


    def test_get_quantity(self):
        assert item.get_quantity() == 20
