from typedproperty import String, Integer, Float


class Stock:
    """
    An instance of a stock holding consisting of name, shares, and price.
    """
    # __slots__ = ('name', '_shares', 'price')
    name = String('name')
    shares = Integer('shares')
    price = Float('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        return f'Stock({self.name.__repr__()}, {self.shares}, {self.price})'

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, shares):
        self.shares -= shares
