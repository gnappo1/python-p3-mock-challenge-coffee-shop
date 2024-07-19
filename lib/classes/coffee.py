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


class Coffee:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("names must be strings")
        elif hasattr(self, "_name"):
            raise ValueError("names cannot be reset")
        elif len(name) < 3:
            raise ValueError("names must be at least 2 characters long")

        self._name = name

    def orders(self):
        from classes.order import Order

        #! go through the order list
        #! filter by self as the order's coffee choice
        return [order for order in Order.all if self is order.coffee]

    def customers(self):
        return list({order.customer for order in self.orders()})

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        # total = 0
        # for order in self.orders():
        #     total += order.price
        # return total / self.num_orders()

        # return sum(order.price for order in self.orders()) / self.num_orders()
        from functools import reduce
        # return reduce(lambda acc, order: acc + order.price, self.orders(), 0) / self.num_orders()
        from statistics import mean
        orders = self.orders()
        return orders and mean(order.price for order in orders)

        # if orders := self.orders():
        #     return mean(order.price for order in orders)
        # return 0.0

c = Coffee("test")
c.average_price()
# # c.name = "test"
print("done")
