import seaborn as sns
import random
from collections import deque
import matplotlib.pyplot as plt
import sys

class Arena(type):

    def __new__(cls, class_name, class_parents, class_dict):
        if class_dict['isFirst']:
            print(class_name, 'stand in the area')
            class_dict['line'] = int(input('Type line setup for First Cat'))
        else:
            print(class_name, 'stand in the area')
            class_dict['line'] = int(input('Type line setup for Second Cat'))

        class_dict['age'] = random.randint(1, 20)
        new_cat = super().__new__(cls, class_name, class_parents, class_dict)
        return new_cat


class FirstCat(metaclass=Arena):
    isFirst = True
    age = None
    line = 0

    @classmethod
    def getAge(cls):
        return cls.age

    @classmethod
    def getLine(cls):
        return cls.line

class SecondCat(metaclass=Arena):
    isFirst = False
    age = None
    line = 0

    @classmethod
    def getAge(cls):
        return cls.age

    @classmethod
    def getLine(cls):
        return cls.line


class Battle(object):

    def __init__(self):
        self.age1 = FirstCat().getAge()
        self.line1 = FirstCat().getLine()

        self.age2 = SecondCat().getAge()
        self.line2 = SecondCat().getLine()

        self.moves = deque([self.line1, self.line2])

    def getGreaterAge(self):
        if self.age1 >= self.age2:
            print('First Cat is starting')
            return True
        else:
            print('Second cat is starting')
            return False


    def getGreaterLine(self):
        if self.line1 == self.line2:
            print("Both cats cant stand in the same place on the battle area, mismatch")
            sys.exit(0)

        elif self.line2 > self.line1:
            print("First cat moves are appending to left, Second cat moves are appending to right")
            return True

        else:
            print("Second cat moves are appending to left, First cat moves are appending to right")
            return False

    @staticmethod
    def caseIncrement1(increment):
        switcher = {
            0: 2,
            1: 1,
            2: 1
        }
        return switcher.get(increment, "move not possible")

    @staticmethod
    def caseIncrement2(increment):
        switcher = {
            0: 1,
            1: 2,
            2: 1
        }
        return switcher.get(increment, "move not possible")

    def game(self):
        if Battle().getGreaterLine():
            while (self.moves[-1] - self.moves[0]) > 1:
                if Battle().getGreaterAge():
                    if Battle().getGreaterLine():
                        inc1 = Battle().caseIncrement1((self.moves[0] - self.moves[-1]) % 3)
                        self.moves.appendleft(inc1 + self.moves[0])
                        inc2 = Battle().caseIncrement2((self.moves[0] - self.moves[-1]) % 3)
                        self.moves.append(self.moves[-1] - inc2)
                    else:
                        inc1 = Battle().caseIncrement1((self.moves[0] - self.moves[-1]) % 3)
                        self.moves.append(inc1 + self.moves[0])
                        inc2 = Battle().caseIncrement2((self.moves[0] - self.moves[-1]) % 3)
                        self.moves.appendleft(self.moves[-1] - inc2)
                else:
                    if Battle().getGreaterLine():
                        inc2 = Battle().caseIncrement2((self.moves[-1] - self.moves[0]) % 3)
                        self.moves.append(self.moves[-1] - inc2)
                        inc1 = Battle().caseIncrement1((self.moves[-1] - self.moves[0]) % 3)
                        self.moves.appendleft(inc1 + self.moves[0])
                    else:
                        inc2 = Battle().caseIncrement2((self.moves[-1] - self.moves[0]) % 3)
                        self.moves.appendleft(self.moves[-1] - inc2)
                        inc1 = Battle().caseIncrement1((self.moves[-1] - self.moves[0]) % 3)
                        self.moves.append(inc1 + self.moves[0])
        else:
            while (self.moves[0] - self.moves[-1]) > 1:
                if Battle().getGreaterAge():
                    if Battle().getGreaterLine():
                        inc1 = Battle().caseIncrement1((self.moves[0] - self.moves[-1]) % 3)
                        self.moves.appendleft(inc1 + self.moves[0])
                        inc2 = Battle().caseIncrement2((self.moves[0] - self.moves[-1]) % 3)
                        self.moves.append(self.moves[-1] - inc2)
                    else:
                        inc1 = Battle().caseIncrement1((self.moves[0] - self.moves[-1]) % 3)
                        self.moves.append(inc1 + self.moves[0])
                        inc2 = Battle().caseIncrement2((self.moves[0] - self.moves[-1]) % 3)
                        self.moves.appendleft(self.moves[-1] - inc2)
                else:
                    if Battle().getGreaterLine():
                        inc2 = Battle().caseIncrement2((self.moves[-1] - self.moves[0]) % 3)
                        self.moves.append(self.moves[-1] - inc2)
                        inc1 = Battle().caseIncrement1((self.moves[-1] - self.moves[0]) % 3)
                        self.moves.appendleft(inc1 + self.moves[0])
                    else:
                        inc2 = Battle().caseIncrement2((self.moves[-1] - self.moves[0]) % 3)
                        self.moves.appendleft(self.moves[-1] - inc2)
                        inc1 = Battle().caseIncrement1((self.moves[-1] - self.moves[0]) % 3)
                        self.moves.append(inc1 + self.moves[0])
        return self.moves

    def draw(self):
        print(self.moves)
        sns.distplot(self.moves, rug=True, rug_kws={"color": "r", "height": 0.1},
                     kde_kws={"color": "k", "lw": 3})
        plt.show()

if __name__ == '__main__':
    cat1 = FirstCat().getAge()
    cat2 = SecondCat().getAge()
    battle = Battle()
    battle.game()
    battle.draw()
