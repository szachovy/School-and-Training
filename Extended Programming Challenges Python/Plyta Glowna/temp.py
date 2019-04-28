"""
import re

value = 'fewfe$w'

if len(value) > 20:
    print('string is too big to be drawed')
    raise Exception(quit(0))

try:
    characterRegex = re.compile(r'[^A-Za-z]')
    only_letters = characterRegex.search(value)
    assert not bool(only_letters) is True

except AssertionError as a:
    print('Only letters are acceptable', a)
    quit(0)

print(value)
"""
print(chr(nextletter + 97))
print(chr(letter + 97))
class NonNegative:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Cannot be negative.')
        instance.__dict__[self.name] = value
    def __set_name__(self, owner, name):
        self.name = name

class Order:
    price = NonNegative()
    quantity = NonNegative()

    def __init__(self, name, price, quantity):
        self._name = name
        self.price = price
        self.quantity = quantity

    def total(self):
        return self.price * self.quantity

apple_order = Order('apple', 1, 10)
print(apple_order.total())
# 10
#apple_order.price = -10