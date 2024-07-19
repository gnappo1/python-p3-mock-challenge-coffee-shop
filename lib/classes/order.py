class Order:
    all = []
    
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        type(self).all.append(self)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if not isinstance(price, float):
            raise TypeError("prices must be integers")
        elif price not in range(1, 11):
            raise ValueError("prices must be between $1 and $10")
        elif hasattr(self, "_price"):
            raise ValueError("prices cannot be reset")
        self._price = price

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, customer_instance):
        from classes.customer import Customer
        if not isinstance(customer_instance, Customer):
            raise TypeError("customer must be of type Customer")
        self._customer = customer_instance

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, coffee_instance):
        from classes.coffee import Coffee
        if not isinstance(coffee_instance, Coffee):
            raise TypeError("coffee must be of type Coffee")
        self._coffee = coffee_instance

# from customer import Customer
# from coffee import Coffee

# o = Order(Customer("matteo"), Coffee("ristretto"), 11)
# print('done')
