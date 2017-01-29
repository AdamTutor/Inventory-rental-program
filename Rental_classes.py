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

    def __str__(self):
        return "product: " + self.name + "\nreplacement value: " + str(self.replacement_value)+ "\nDeposit value: " + str(self.deposit_value)+ "\nprice " + str(self.price)+ "\nquantity " + str(self.quantity)

    def item_rented(self):
        self.quantity = self.quantity -1
        return self.quantity

    
    def item_returned(self):
        self.quantity = self.quantity + 1
        return self.quantity





class Transaction():
    """A Transaction object that represents a transaction that has been made. 

    Attributes:
        Datetime: A Datetime representing the time the transaction was written to the transaction.csv file. 
        Item: Represens a Item object created from data pulled from inventory.csv
        status: A integer value representing 10 percent of the replacement value. 
         """
def __init__(self, Datetime, Item, status):
    self.Datetime = Datetime
    self.Item = Item
    self.status = status