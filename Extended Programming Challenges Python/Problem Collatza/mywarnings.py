import os
import math
import collatz

def numInput(interface):
    try:
        num = input('Input value')
        if interface == collatz.numberKind.int.value:
            num = int(num)
        else:
            num = math.floor(float(num))
            num = int(num)
    except ValueError:
        print('Try type number again!')
        numInput(interface)
    else:
        return num

def getOutFile(data):
    try:
        os.chmod((os.path.abspath('storage.csv')), 0o770)
    except FileNotFoundError:
        os.mknod('storage.csv', 0o770)
    finally:
        with open('storage.csv', 'a+') as f:
            return f.write(data)
