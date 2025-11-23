class Customer:
    # Assuming Order class exists and has an 'all' list tracking all instances
    from .order import Order

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
        return [order for order in self.Order.all if order.customer == self]

    def coffees(self):
        """Returns a unique list of all coffees this customer has ordered."""
        customer_orders = self.orders()
        return list(set(order.coffee for order in customer_orders))