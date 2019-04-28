import multiprocessing
import time
import wrongs
import json


class GetWords(object):
    def __init__(self, words):
        self.words = words
        self.shortenwords = []
        self.preparedwords = []

    def preparation(self):
        wrongs.notletterCheck(self.words)
        for word in self.words:
            word = str(word.upper()) + ';'
            self.preparedwords.append(word)

        return self.preparedwords

    def shortenWords(self):
        num = 1
        for word in self.preparedwords:
            for index, item in enumerate(word):
                try:
                    if word[index] == word[index + 1]:
                        num += 1
                        continue
                    else:
                        self.shortenwords.append(word[index] + str(num))
                        num = 1
                except IndexError:
                    continue
            self.shortenwords.append(' ')

        return self.shortenwords

    def toString(self):
        return ''.join(self.shortenwords)


def oneDatasetTasks():
    words = [word for word in input().split()]

    shorten = GetWords(words)
    shorten.preparation()
    shorten.shortenWords()
    return shorten.toString()


def getPreResult():
    print('values ->')


def getResult(collection):
    time.sleep(0.5)
    print(collection)


if __name__ == '__main__':
    collection = {}

    wrongs.dataSets()
    howmany = input()
    wrongs.howmanyCheck(howmany)

    for i in range(int(howmany)):
        wrongs.printMenu()
        collection[i] = oneDatasetTasks()

    getPreRes = multiprocessing.Process(target=getPreResult())
    getRes = multiprocessing.Process(target=getResult(collection))

    getPreRes.start()
    getRes.start()

    getPreRes.join()
    getRes.join()

    with open('DataFile.json', 'w') as f:
        json.dump(collection, f)

