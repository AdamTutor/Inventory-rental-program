class Item():
    """A Inventory object that represents a item in inventory. 

    Attributes:
        name: A string representing the items's name. 
        replacement value: A interger that represents the cost to replace the item if it was to be returned broken or damaged. 
        deposit value: A integer value representing 10 percent of the replacement value. 
        price: a integer value represents the cost of the item's rent
        quantity: a integer value representing how many of the item is in stock. """


    def __init__(self, name, replacement_value, deposit_value, price, quantity):
        """Initializes item object wit a name, replacement value, deposit value, price, and quantity"""
        self.name = name
        self.replacement_value = replacement_value
        self.deposit_value = deposit_value
        self.price = price
        self.quantity = quantity
    def get_name(self):
        "returns the name of the object"
        return self.name 
        

    def get_replacement_value(self):
        """Return the replacement value of the object"""
        return self.replacement_value


    def get_deposit_value(self):
        """Return the deposit value of the object"""
        return self.deposit_value


    def get_price(self):
        """Return the price value of the object"""
        return self.price


    def get_quantity(self):
        """Return the pricet value of the object"""
        return self.quantity

    def item_rented(self):
        self.quantity = self.quantity -1
        return self.quantity