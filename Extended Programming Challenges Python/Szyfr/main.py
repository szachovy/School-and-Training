# Proxy Pattern
# Docker
from math import ceil
import binascii
import hashlib
import re
import configparser
import abc

class Requires(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def convert(self):
        raise NotImplementedError('Conversions must be present in this class')

    @abc.abstractmethod
    def check_input(self, sth):
        raise NotImplementedError('Checking binary input is required')

    @abc.abstractmethod
    def choose_endian(self):
        raise NotImplementedError('Specific endian in reading requred')

class BinCode(Requires):

    @classmethod
    def convert(cls):
        code = input('Type binary code to get translated letters')
        cls.check_input(code)

        autocomplete = (ceil(len(code) / 8) * 8) - len(code)
        code = autocomplete * '0' + code

        letter = 0
        output = ''

        if cls.choose_endian():
            code = reversed(code)

        for byte in code:
            if not (letter % 8):
                output += output.join(':')

            output += output.join(byte)
            letter += 1

        print('This is your byte code')
        print(output)

        output = output.split(':')
        output.remove('')

        for key, val in enumerate(output):
            output[key] = binascii.b2a_uu(val.encode())
            output[key] = str(output[key]).replace(r'\n', '').replace('b', '')

        print('And there is your bytecode translated')
        print(output)

    @staticmethod
    def check_input(code, **kwargs):
        try:
            character_regex = re.compile(r'[0-1]')
            check = character_regex.search(code)
            assert check

        except AssertionError:
            print('Only binary code is acceptable')
            BinCode.convert()

    @staticmethod
    def choose_endian(**kwargs):
        endian = input('what endian should be covered small or big [s/b]?')
        if endian is 's':
            print('You`ve choosen small endian')
            return False
        elif endian is 'b':
            print('You`ve choosen big endian')
            return True
        else:
            print('Wrong input, retry')
            return BinCode.choose_endian()


class Proxy(BinCode):
    config = configparser.ConfigParser()
    config.read('config.ini')


    def __init__(self, typed_password):
        self.__password = hashlib.pbkdf2_hmac('sha256', str(self.config['DEFAULT']['password']).encode(),
                                                str(self.config['DEFAULT']['salt']).encode(), 10000)

        self.authorize = str(typed_password).encode()
        print(self.authorize)

    @property
    def authorize(self):
        if binascii.hexlify(self.__typed_password) == binascii.hexlify(self.__password):
            print('access granted')
            return self.convert()
        else:
            print('authorization failed')
            quit(0)

    @authorize.setter
    def authorize(self, value):
        self.__typed_password = hashlib.pbkdf2_hmac('sha256', value,
                                                    str(self.config['DEFAULT']['salt']).encode(), 10000)


class ProxyImage(Proxy):
    def __init__(self, typed_password = input('Type password to get access: ')):
        super().__init__(typed_password)


if __name__ == '__main__':
    attempt = ProxyImage()