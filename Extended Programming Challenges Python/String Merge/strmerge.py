import re
import sys
import asyncio
import hashlib

class MergeStr(object):
    def __init__(self, count):
        self.count = count
        self.string = input('Input ' + self.count + ' string')

    def __gt__(self, other):
        if len(self.string) > len(other.string):
            print('first string is greater so his ending letters are removed')
        elif len(self.string) == len(other.string):
            print('same length in two strings so nothing is removed')
        else:
            print('second string is greater so his ending letters are removed')
        return len(self.string) > len(other.string)

    def __iter__(self):
        liststring = []
        for letter in self.string:
            liststring.append(letter)
        return iter(liststring)

    def stringCHECK(self):
        characterRegex = re.compile(r'[^a-zA-Z]')
        check = characterRegex.search(self.string)
        if not bool(check):
            return True
        else:
            print('Input incorrect try again')
            sys.exit(0)

    def shrink(self, other):
        string = list(self.string)
        other = list(other.string)

        diff = len(string) - len(other)
        for i in range(diff):
            string.pop()

        return string

def iterere(string):
    for it in string:
        yield it

async def getIter(string, long, finalstr):
    for i in range(long):
        finalstr.append(next(iterere(string)))

def getRes(finalstr, long):
    results = []
    i = 0
    while i < long:
        results.append(finalstr[i])
        results.append(finalstr[long + i])
        i += 1

    return ''.join(results)

def hashit(results):
    results = results.encode()

    h = hashlib.new('sha256')
    h.update(results)

    return h.hexdigest()

if __name__ == '__main__':
    finalstr = []
    string1 = MergeStr('first')
    string2 = MergeStr('second')

    if string1.stringCHECK() and string2.stringCHECK():
        if string1 > string2:
            string1 = string1.shrink(string2)
            string2 = list(string2)
            long = len(string1)

            string1 = iter(string1)
            string2 = iter(string2)

            loop = asyncio.get_event_loop()

            loop.run_until_complete(getIter(string1, long, finalstr))
            loop.run_until_complete(getIter(string2, long, finalstr))

            result = getRes(finalstr, long)
            print(result)
            print(hashit(result))

        else:
            string2 = string2.shrink(string1)
            string1 = list(string1)
            long = len(string2)

            string1 = iter(string1)
            string2 = iter(string2)

            loop = asyncio.get_event_loop()

            loop.run_until_complete(getIter(string1, long, finalstr))
            loop.run_until_complete(getIter(string2, long, finalstr))

            result = getRes(finalstr, long)
            print(result)
            print(hashit(result))