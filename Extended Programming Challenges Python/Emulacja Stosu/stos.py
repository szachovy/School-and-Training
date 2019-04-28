import sys
import sqlite3
import menu

class Container(object):
    def __init__(self):
        self.element = None
        self.stack = {}
        self.size = len(self.stack)

    @property
    def inspectInput(self):
        try:
            self.element = float(self.element)
        except ValueError:
            print('Only numbers are acceptable in our Stack')
            return False
        except:
            print("Unexpected Error: "), sys.exc_info()
            return False
        return self.element

    @inspectInput.setter
    def inspectInput(self, value):
        if self.size > 10000:
            raise OverflowError('Current Stack is too big' + sys.exit(0))
        else:
            self.element = value

    @staticmethod
    def stackconverter():
        stackconv = ""
        temp = 0
        for val in operationinterface.stack.values():
            stackconv += str(val)
            temp += 1
            if temp != len(operationinterface.stack):
                stackconv += '->'
        return stackconv

    def __setitem__(self):
        self.stack[self.size] = self.element

    def __delitem__(self):
        if self.size >= 1:
            del self.stack[self.size - 1]
        else:
            print('Zero elements in Stack')

    def __getitem__(self, index):
        try:
            return self.stack[index]
        except KeyError:
            print('Indexed value is not introduced in stack')
            return False

def move(choice, operationinterface, conn, c):
    if choice == 1:
        pushtostack(operationinterface)
    elif choice == 2:
        operationinterface.__delitem__()
        operationinterface.size -= 1
    elif choice == 3:
        checkit = int(input('What index to check'))
        if operationinterface[checkit] is not False:
            print('value of this index is ', end=' ')
            print(operationinterface[checkit])
    elif choice == 4:
        print('Size of stack is -> ' + str(operationinterface.size))
    elif choice == 5:
        print('This is our current stack', end=' ')
        print(operationinterface.stack)
    else:
        print('Thank you for using this program')
        stack = operationinterface.stackconverter()
        c.execute("INSERT INTO stack(stack_size, stack) VALUES (?,?)", (operationinterface.size, stack))
        conn.commit()
        conn.close()
        sys.exit(0)

def pushtostack(operationinterface):
    pushit = input('What value to PUSH')
    operationinterface.inspectInput = pushit
    if operationinterface.inspectInput is not False:
        operationinterface.__setitem__()
        operationinterface.size += 1
    else:
        pushtostack(operationinterface)


if __name__ == '__main__':
    operationinterface = Container()
    conn = sqlite3.connect('stosdb')
    c = conn.cursor()
    # c.execute("CREATE TABLE stack (number INTEGER PRIMARY KEY, stack_size INTEGER NOT NULL, stack VARCHAR(64))")

    print(menu.Menu.starter())

    while True:
        move(menu.Menu.choose(), operationinterface, conn, c)


