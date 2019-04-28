import pydotplus
from collections import deque
import time

class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

class Connections(object):
    PLACES = {0: [0, -1], 1: [0, 1], 2: [-1, -3], 3: [-1, -2], 4: [1, 2], 5: [1, 3],
              6: [-3, -7], 7: [-3, -6], 8: [-2, -5], 9: [-2, -4], 10: [2, 4],
              11: [2, 5], 12: [3, 6], 13: [3, 7]}

class BinaryTree(Singleton):
    def __init__(self):
        self.digram_beginning = 'digraph tree {'
        self.digram_ending = '}'

        self.data = []

        self.noder = deque()
        self.nodel = deque()

        self.used_nodel_left = [False, False]
        self.used_nodel_right = [False, False]
        self.used_noder_left = [False, False]
        self.used_noder_right = [False, False]

        self.tree = deque()

        self.root = 0


    def insert_data(self):
        try:
            self.data = input().split(' ')
            list(filter(int, self.data))

        except ValueError:
            print('Letters detected try again')
            self.insert_data()

        self.data = list(map(int, self.data))

        try:
            assert min(self.data) >= 0

        except AssertionError:
            print('Only positive numbers are acceptable to generate graph')
            self.insert_data()

    def calculate(self):
        size = 0

        for attempt in range(len(self.data)):
            if not size:
                self.root = self.data[0]
                self.tree.append(self.data[0])
            else:
                try:
                    self.tree.appendleft(self.nodel[0])
                except IndexError:
                    pass
                try:
                    self.tree.append(self.noder[0])
                except IndexError:
                    pass

            for val in self.tree:
                if val in self.data:
                    self.data.remove(val)

            self.nodel.clear()
            self.noder.clear()

            checkrr = 0
            idxrr = 0

            checkrl = 0
            idxrl = 0

            checkll = 0
            idxll = 0

            checklr = 0
            idxlr = 0

            for data in self.data:
                if not size:
                    if data >= self.tree[0]:
                        self.noder.append(data)
                    else:
                        self.nodel.append(data)
                else:
                    if data >= self.tree[size - 1]:
                        if data >= self.tree[size]:
                            if not checkrr:
                                idxrr = data
                                self.noder.append(data)
                            else:
                                self.noder.append(data)

                            self.used_noder_right[checkrr] = True
                            checkrr += 1
                        else:
                            if not checkrl:
                                idxrl = data
                                self.noder.appendleft(data)
                            else:
                                self.noder.appendleft(data)

                            self.used_noder_left[checkrl] = True
                            checkrl += 1

                        if self.used_noder_right[0] and self.used_noder_right[1] and not self.used_noder_left[0]:
                            for key, value in enumerate(self.noder):
                                if value == idxrr:
                                    self.noder.insert(key - 1, NotImplemented)

                        if self.used_noder_left[0] and self.used_noder_left[1] and not self.used_noder_right[0]:
                            for key, value in enumerate(self.noder):
                                if value == idxrl:
                                    self.noder.insert(key + 1, NotImplemented)

                    else:
                        if data >= self.tree[0]:
                            if not checkll:
                                idxll = data
                                self.nodel.appendleft(data)
                            else:
                                self.nodel.appendleft(data)
                            self.used_nodel_left[checkll] = True
                            checkll += 1
                        else:
                            if not checklr:
                                idxlr = data
                                self.nodel.append(data)
                            else:
                                self.nodel.append(data)
                            self.used_nodel_right[checklr] = True
                            checklr += 1

                        if self.used_nodel_right[0] and self.used_nodel_right[1] and not self.used_nodel_left[0]:
                            for key, value in enumerate(self.nodel):
                                if value == idxlr:
                                    self.noder.insert(key - 1, NotImplemented)

                        if self.used_nodel_left[0] and self.used_nodel_left[1] and not self.used_nodel_right[0]:
                            for key, value in enumerate(self.nodel):
                                if value == idxll:
                                    self.noder.insert(key + 1, NotImplemented)

            self.used_noder_right = [False, False]
            self.used_noder_left = [False, False]
            self.used_nodel_right = [False, False]
            self.used_nodel_left = [False, False]

            size += 2
            #print(self.tree)

    def get_root(self):
        for index, value in enumerate(self.tree):
            if value == self.root:
                return index

    def write_line(self, root, first_num, second_num):
        try:
            return '\n  ' + str(self.tree[root + first_num]) + ' -> ' + str(self.tree[root + second_num]) + ';'

        except TypeError:
            return

    def make_file(self):
        self.tree = list(self.tree)
        print(self.tree)
        root = self.get_root()
        node = 0

        with open('tree.dot', 'w') as file:
            file.truncate(0)
            file.write(self.digram_beginning)
            for attempt in range(len(self.tree) - 1):
                try:
                    file.write(self.write_line(root, Connections.PLACES[node][0], Connections.PLACES[node][1]))

                except IndexError:
                    pass

                finally:
                    node += 1


            file.write(self.digram_ending)


    @staticmethod
    def graph():
        gentree = pydotplus.graph_from_dot_file('tree.dot')
        gentree.write_svg('gen.svg')

if __name__ == '__main__':
    s = BinaryTree()
    s.insert_data()
    s.calculate()

    s.make_file()
    time.sleep(1)

    s.graph()