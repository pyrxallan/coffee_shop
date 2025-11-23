class Customer:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str) or not (1 <= len(name) <= 15):
            raise ValueError("Name must be a string between 1 and 15 characters.")
        self._name = name

    def orders(self):
        """Returns a list of all orders for this customer."""
        from .order import Order
        return [order for order in Order.all if order.customer == self]

    def coffees(self):
        """Returns a unique list of all coffees this customer has ordered."""
        return list(set(order.coffee for order in self.orders()))

    def create_order(self, coffee, price):
        """Creates and returns a new Order instance for this customer."""
        from .order import Order
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        """
        Receives a coffee object and returns the Customer who has spent the most on that coffee.
        Returns None if there are no customers for the coffee.
        """
        coffee_orders = coffee.orders()
        if not coffee_orders:
            return None

        customer_spending = {}
        for order in coffee_orders:
            customer_spending[order.customer] = customer_spending.get(order.customer, 0) + order.price

        return max(customer_spending, key=customer_spending.get)