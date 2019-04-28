a = 0
b = 1
c = 2
if a:
    print(a)
if b:
    print(b)

if c % 2:
    print(c)
if b % 2:
    print(b)

class A(object):
    def __init__(self):
        self.huj = 0

    def __call__(self, *args, **kwargs):
        self.huj += 1
        print('avokado', *args)

    def ale(self):
        print(self.huj)

a = A()
a(123)
a.ale()
"""
if class_dict[isFirst]:
    print(class_name)
    class_dict['isFirst'] = False
else:
    print('jest')


class Mac(Cat):
    def eggs(self):
        print("[insert example string here]")
    def ea(self):
        print('jhu')
"""


def game(self):
    while (self.moves[0] - self.moves[-1]) <= 1 or (self.moves[-1] - self.moves[0]) <= 1:
        if Battle().getGreaterAge():
            if Battle().getGreaterLine():
                inc1 = Battle().caseIncrement1((self.moves[0] - self.moves[-1]) % 3)
                self.moves.appendleft(inc1)
                inc2 = Battle().caseIncrement2((self.moves[0] - self.moves[-1]) % 3)
                self.moves.append(inc2)
            else:
                inc1 = Battle().caseIncrement1((self.moves[0] - self.moves[-1]) % 3)
                self.moves.append(inc1)
                inc2 = Battle().caseIncrement2((self.moves[0] - self.moves[-1]) % 3)
                self.moves.appendleft(inc2)
        else:
            if Battle().getGreaterLine():
                inc2 = Battle().caseIncrement2((self.moves[-1] - self.moves[0]) % 3)
                self.moves.append(inc2)
                inc1 = Battle().caseIncrement1((self.moves[-1] - self.moves[0]) % 3)
                self.moves.appendleft(inc1)
            else:
                inc2 = Battle().caseIncrement2((self.moves[-1] - self.moves[0]) % 3)
                self.moves.appendleft(inc2)
                inc1 = Battle().caseIncrement1((self.moves[-1] - self.moves[0]) % 3)
                self.moves.append(inc1)
    return self.moves