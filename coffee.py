class Coffee:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if hasattr(self, '_name'):
            raise AttributeError("Cannot change the name of the coffee.")
        if not isinstance(name, str) or len(name) < 3:
            raise ValueError("Name must be a string of at least 3 characters.")
        self._name = name

    def orders(self):
        """Returns a list of all orders for this coffee."""
        from .order import Order
        return [order for order in Order.all if order.coffee == self]

    def customers(self):
        """Returns a unique list of customers who have ordered this coffee."""
        return list(set(order.customer for order in self.orders()))
