# -*- coding: utf-8 -*-


class EuroService(object):
    rates = {
        "EUR": 1,
        "GBP": 1.2,
        "USD": 0.8,
    }

    def rate(self, cur):
        return self.rates[cur]

euro_service = EuroService()

symbols = {
    "EUR": "¢",
    "GBP": "£",
    "USD": "$",
}


class Currency(object):
    @classmethod
    def dollar(cls, amount):
        return cls(amount, "USD")

    @classmethod
    def pound(cls, amount):
        return cls(amount, "GBP")

    @classmethod
    def euro(cls, amount):
        return cls(amount, "EUR")

    def __init__(self, amount, cur):
        self.amount = amount
        self.cur = cur
        self.symbol = symbols[cur]

    def __add__(self, other):
        if type(other) in (int, long, float):
            return Currency(self.amount + other, self.cur)
        r1 = euro_service.rate(self.cur)
        r2 = euro_service.rate(other.cur)
        in_euros = self.amount * r1 + other.amount * r2
        return Currency(in_euros * 1.0 / r1, self.cur)

    def __radd__(self, other):
        return self + other

    def __mul__(self, other):
        if type(other) in (int, long, float):
            return Currency(self.amount * other, self.cur)
        if self.cur != other.cur:
            raise TypeError("cannot multiply %s in %s" % (self.cur, other.cur))
        return Currency(self.amount * other.amount, self.cur)

    def __repr__(self):
        return "%s%s" % (self.symbol, self.amount)


d = Currency.dollar(5)
p = Currency.pound(5)
e = Currency.euro(5)

print d
print p
print e

print (e + d)
print (d + e)
print (p + 6)
print (6 + p)
print (p * p)
print (d * d)


