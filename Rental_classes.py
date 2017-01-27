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