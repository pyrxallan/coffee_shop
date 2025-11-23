from customer import Customer
from coffee import Coffee
from order import Order

if __name__ == '__main__':
    print("Starting debug script...")

    # 1. Create instances
    cappuccino = Coffee("Cappuccino")
    latte = Coffee("Latte")
    espresso = Coffee("Espresso")
    cold_brew = Coffee("Cold Brew") # A coffee that won't be ordered

    ken = Customer(name="Ken")
    allan = Customer(name="Allan")

    # 2. Create orders to build relationships
    # Ken loves Cappuccinos
    ken.create_order(cappuccino, 4.75)
    ken.create_order(cappuccino, 4.75)
    ken.create_order(latte, 5.0)

    # Allan is exploring the menu
    allan.create_order(latte, 5.25)
    allan.create_order(cappuccino, 4.5)

    # 3. Test your methods and print the results
    print("\n--- Testing Customer Methods ---")
    print(f"Number of orders for {ken.name}: {len(ken.orders())}")
    print(f"Coffees {ken.name} has tried: {[c.name for c in ken.coffees()]}")

    print("\n--- Testing Coffee Methods ---")
    print(f"Number of Cappuccino orders: {cappuccino.num_orders()}")
    print(f"Customers who ordered Cappuccino: {[c.name for c in cappuccino.customers()]}")
    print(f"Average price for a Latte: ${latte.average_price():.2f}")

    # 4. Test edge cases
    print("\n--- Testing Edge Cases ---")
    print(f"Number of orders for Cold Brew: {cold_brew.num_orders()}")
    print(f"Average price for Cold Brew: {cold_brew.average_price()}")

    # 5. Test the class method
    print("\n--- Testing Class Methods ---")
    top_cappuccino_fan = Customer.most_aficionado(cappuccino)
    if top_cappuccino_fan:
        print(f"The biggest Cappuccino aficionado is: {top_cappuccino_fan.name}")

    import ipdb; ipdb.set_trace()

    print("\nDebug script finished.")
