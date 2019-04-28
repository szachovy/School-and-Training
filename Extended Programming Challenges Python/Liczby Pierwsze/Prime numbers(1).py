import menus

class Numbers(object):
    def __repr__(self):
        return "You can type here : "

    def __init__(self):
        self.number = None

    def writeNumber(self):
        try:
            self.number = int(input())
        except TypeError:
            print("Digits is only acceptable type, please do it again\n")
            Numbers.writeNumber(self)

        return self.number

    def makeDecision(self):
        for i in range(2, self.number):
            if (self.number % i) == 0:
                print(str(self.number) + ' isn`t prime number')
                return False
        else:
            print(str(self.number) + ' is prime number')
            return True

    def writeCollection(self):
        try:
            with open('save_collections.txt', 'a') as f:
                f.write(str(self.number))
                f.close()
        except IOError as e:
            print(e + ' occurred something goes wrong in saving file')


class Statics(Numbers):
    def readCollectiion(self):
        try:
            with open('save_collections.txt', 'r') as f:
                print(str(f.readlines()))
                f.close()
        except IOError as e:
            print(e + ' occurred something goes wrong in saving file')


def satisfiesOne():
    print(repr(Numbers()))
    getnum = Numbers()
    getnum.writeNumber()
    getnum.makeDecision()
    getnum.writeCollection()
    try:
        with open('save_collections.txt', 'a') as f:
            if getnum.makeDecision():
                f.write('   This is prime number\n')
            else:
                f.write('   This isn`t prime number\n')
    except IOError:
        print('Something goes wrong with required data file')
    selectingContinous()

def satisfiesTwo():
    getall = Statics()
    getall.readCollectiion()


def checkCorrection(select):
    if select != 'q' or select != '1' or select != '2':
        return True
    else:
        return False


def selectingContinous():
    continuing = input("Do you want to continue typing? [Y/N]")
    continuing = continuing.lower()
    if continuing == 'y':
        return satisfiesOne()
    elif continuing == 'n':
        return
    else:
        print('Wrong type do it again ')
        selectingContinous()


if __name__ == '__main__':
    select = None
    print(menus.GENERAL_MENU)
    while select != 'q':
        select = input()
        if checkCorrection(select):
            if select == '1':
                print(menus.SELECTING_MENU)
                satisfiesOne()
                print('What`s next?')
                continue
            elif select == '2':
                print(menus.STATISTICS_MENU)
                satisfiesTwo()
                print('What`s next?')
                continue

    exit(code=0)
