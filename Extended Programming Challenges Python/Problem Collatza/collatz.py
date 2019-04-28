
from enum import Enum, unique
import mywarnings

@unique
class numberKind(Enum):
    int = 'int'
    float = 'float'

def userInterface():
    while True:
        kind = input("What kind of number do you want to input ->")
        if kind == 'int' or kind == 'float':
            return kind
        else:
            print('Bad input try it again')

def calculate(num : int) -> int:
    asc = 0
    while num != 1:
        if num % 2:
            num = (3 * num) + 1
            asc += 1
        else:
            num /= 2
            asc += 1
    return asc

if __name__ == '__main__':
    result = calculate(mywarnings.numInput(userInterface()))
    print('Loop has gone ' + str(result) + ' times.')
    mywarnings.getOutFile(str(result))
    with open('storage.csv') as f:
        f.read()



