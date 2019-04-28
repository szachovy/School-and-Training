from abc import *
from queue import Queue
import re

class Moves(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def transformIntoQueue(self):
        raise NotImplementedError('Caption must be converted into queue to get fun')

    @abstractmethod
    def count(self):
        raise NotImplementedError('This function must be implemented for calculations')

    @abstractmethod
    def resetMachine(self):
        raise NotImplementedError('Cleaning after successfully executed program is necessary')


class Caption(object):
    def __set__(self, instance, value):
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

        print('Setting:', value)
        self.__mystery_caption = value

    def __get__(self, instance, owner):
        return self.__mystery_caption

    def __delete__(self, instance):
        print('Thank you for using this program!')
        del self.__mystery_caption

class MoveMachine(Moves):
    caption = Caption()

    def __init__(self):
        super().__init__()
        self.caption = input('Input string to calculate all moves from'
          ' machine to sign it on plate : ')
        self.queueOfLetters = Queue()
        self.result = 0

    def transformIntoQueue(self):
        for letter in self.caption.lower():
            self.queueOfLetters.put(letter)

    def count(self):
        letter = 0
        for place in range(self.queueOfLetters.qsize()):
            nextletter = ord(self.queueOfLetters.get()) - 97

            difference = abs(nextletter - letter)
            if difference <= 13:
                self.result += difference
            else:
                self.result += 26 - difference

            letter = nextletter

        return self.result

    def resetMachine(self):
        del self.caption

if __name__ == '__main__':
    b = MoveMachine()
    b.transformIntoQueue()
    print('Machine will do:', b.count(), 'moves')
    b.resetMachine()