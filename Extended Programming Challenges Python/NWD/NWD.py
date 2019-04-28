from threading import Thread
import threading
import pickle
import timeit


def inputCHECK():
    try:
        value = int(input('Type value : '))
        if value < 1:
            raise ValueError
        return value
    except ValueError:
        print('Digits bigger than one are accepted')
        exit(0)


def showResult(iter):
    if iter == 1:
        print(str(iter) + 'st NWD is ->', end=' ')
    elif iter == 2:
        print(str(iter) + 'nd NWD is ->', end=' ')
    else:
        print(str(iter) + 'rd NWD is ->', end=' ')


class NWD(Thread):
    def __init__(self, first, second):
        super().__init__()
        self.first = first
        self.second = second

    def run(self):
        #algorytm Euklidesa

        while self.first != self.second:
            if self.first > self.second:
                self.first -= self.second
            else:
                self.second -= self.first
        return print(self.first)


if __name__ == '__main__':
    print('How many data sets do you want do regard:\n')
    num = inputCHECK()

    for i in range(num):
        print('Type value of ' + str(i + 1) + ' set\n')
        first = inputCHECK()
        second = inputCHECK()

        threadNWD = NWD(first, second)
        threadResponse = threading.Thread(target=showResult(i+1))

        threadResponse.start()
        threadNWD.start()

        threadResponse.join()
        threadNWD.join()

    attempt = 'This attempt scores -> {} seconds'.format(timeit.timeit())

    with open('data.pickle', 'wb') as f:
        pickle.dump(attempt, f, pickle.HIGHEST_PROTOCOL)

    with open('data.pickle', 'rb') as f:
        print(pickle.load(f))
