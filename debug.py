from coffee_shop.customer import Customer
from coffee_shop.coffee import Coffee
from coffee_shop.order import Order

if __name__ == '__main__':
    # Create some instances of your classes
    c1 = Coffee(name="Mocha")
    c2 = Coffee(name="Latte")
    c3 = Coffee(name="Espresso")

    cust1 = Customer(name="Saron")
    cust2 = Customer(name="John")

    # Create orders using your methods
    order1 = cust1.create_order(c1, 4.50)
    order2 = cust1.create_order(c2, 5.00)
    order3 = cust2.create_order(c1, 4.50)
    order4 = cust2.create_order(c3, 3.00)
    order5 = cust2.create_order(c1, 4.75) # John orders another Mocha

    print("--- Testing Methods ---")

    # Test Customer methods
    print(f"{cust1.name}'s orders: {[o.coffee.name for o in cust1.orders()]}")
    print(f"{cust1.name}'s unique coffees: {[c.name for c in cust1.coffees()]}")

    # Test Coffee methods
    print(f"Number of Mocha orders: {c1.num_orders()}")
    print(f"Average price of a Mocha: ${c1.average_price():.2f}")
    print(f"Customers who ordered Mocha: {[c.name for c in c1.customers()]}")

    # Test the class method
    most_dedicated = Customer.most_aficionado(c1)
    if most_dedicated:
        print(f"The biggest Mocha aficionado is: {most_dedicated.name}")

    # You can add a breakpoint here to debug interactively
    # import ipdb; ipdb.set_trace()
    print("\nDebug script finished.")