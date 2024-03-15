#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Customer
from classes.many_to_many import Order
from classes.many_to_many import Coffee

if __name__ == '__main__':
    print("HELLO! :) let's debug")
    #! Set up the experiment by instantiating a few objects
    
    coffee_1 = Coffee("Mocha")
    coffee_2 = Coffee("Vanilla Latte")
    customer = Customer("Steve")
    customer_2 = Customer("Dima")
    order_1 = Order(customer, coffee_1, 2.0)
    order_2 = Order(customer_2, coffee_1, 5.0)
    order_3 = Order(customer, coffee_2, 5.0)

    #! Jump in ipdb to test your properties and methods
    ipdb.set_trace()
