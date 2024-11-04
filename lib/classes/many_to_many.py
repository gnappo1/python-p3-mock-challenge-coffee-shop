class Coffee:
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("name must be a string")
        elif len(value) < 3:
            raise ValueError("names must be between 3 or more characters")
        elif hasattr(self, "_name"):
            raise AttributeError("name cannot be reset after birth")
        self._name = value
        
    def orders(self):
        return [order for order in Order.all if order.coffee is self]
        # result = []
        # for order in Order.all:
        #     if order.coffee is self:
        #         result.append(order)
        # return result
    
    def customers(self):
        return list({order.customer for order in self.orders()})
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        #! I have a way to get orders for a specific coffee
        #! I can then sum() the order prices
        #! and then divide by the order total
        if orders := self.orders():
            return sum(order.price for order in orders) / len(orders)
        return 0

class Customer:
    def __init__(self, name):
        self.name = name
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("name must be a string")
        elif len(value) not in range(1, 16):
            raise ValueError("names must be between 1 and 15 characters, inclusive")
        self._name = value
        
    def orders(self):
        return [order for order in Order.all if order.customer is self]
    
    def coffees(self):
        return list({order.coffee for order in self.orders()})
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)
    
class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        type(self).all.append(self)

    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, value):
        if not isinstance(value, Customer):
            raise TypeError("customer must be of type Customer")
        self._customer = value
    
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, value):
        if not isinstance(value, Coffee):
            raise TypeError("coffee must be of type Coffee")
        self._coffee = value

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if not isinstance(value, float):
            raise TypeError("price must be of type float")
        elif not 1.0 <= value <= 10.0:
            raise ValueError("price must be between 1.0 and 10.0 inclusive")
        elif hasattr(self, "_price"):
            raise AttributeError("price cannot change after birth")
        self._price = value


# import ipdb; ipdb.set_trace()