class Customer:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("names must be strings")
        elif len(name) not in range(1, 16):
            raise ValueError("names must be between 1 and 15 characters included")
        self._name = name

    def orders(self):
        from classes.order import Order
        #! go through the order list
        #! filter by self as the order's coffee choice
        return [order for order in Order.all if self is order.customer]

    def coffees(self):
        return list({order.coffee for order in self.orders()})

    def create_order(self, coffee_instance, price):
        from classes.order import Order
        return Order(self, coffee_instance, price)