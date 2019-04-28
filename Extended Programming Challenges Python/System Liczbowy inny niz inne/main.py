# Strategy Pattern
from types import MethodType
import math

class IONumber(object):
    MAXIMUM_INPUT_NUMBER = math.factorial(10)
    MINIMUM_INPUT_NUMER = 0


    @classmethod
    def decimal_input(cls):
        try:
            decimal = int(input('Please enter decimal number: '))

        except ValueError:
            print('only ints are acceptable')
            cls.decimal_input()

        else:
            return decimal

    @staticmethod
    def fatorial_output(decimal):
        factorial_number = 10
        converted_number = ''

        decimal_check_point = decimal

        for row in range(factorial_number, 0, -1):
            multiplier = 1

            while multiplier * math.factorial(row) <= decimal:
                multiplier += 1

            decimal -= (multiplier - 1) * math.factorial(row)

            if decimal != decimal_check_point:
                converted_number += str(multiplier - 1)

        return converted_number

class Factorial(object):

    def __init__(self, **kwargs):
        self.name = kwargs.pop('name', None) or 'Factorial'
        if kwargs.get('check_number', None):
            self.check_number = MethodType(kwargs.pop('check_number'), self)

    def __invert__(self, number):
        number = ~number
        return number

    def __rshift__(self, other):
        print(other)
        while other > math.factorial(10):
            other = other >> 1

        print(other)
        return other

    def check_number(self):
        message = '{} class should implement a limits checking method'.format(
            self.__class__.__name__)

        raise NotImplementedError(message)

def too_small(size):
    print('Number is too {} bits are retreated automatically or/and shifted to smaller'.format(size.name))

def too_big(size):
    print('Number is too {} maximum number is {} number will be shifted to smaller'.format(size.name, IONumber.MAXIMUM_INPUT_NUMBER))


def is_accepted(self):
    print('number is {}'.format(self.name))

def check(data):
    checkpoint = data
    if data > IONumber.MAXIMUM_INPUT_NUMBER:
        data = Factorial(name='big', check_number=too_big)
        data.check_number()
        data = data.__rshift__(checkpoint)

    elif data < IONumber.MINIMUM_INPUT_NUMER:
        data = Factorial(name='small', check_number=too_small)
        data.check_number()
        data= data.__rshift__(data.__invert__(checkpoint))

    else:
        data = Factorial(name='accepted', check_number=is_accepted)
        data.check_number()
        data = checkpoint

    print('(' + str(checkpoint) + ')' + r"'10 = ", end='')
    return data


if __name__ == '__main__':
    decimal_number = check(IONumber().decimal_input())
    convert = IONumber().fatorial_output(decimal_number)
    print('(' + convert + ')' + r"'!")