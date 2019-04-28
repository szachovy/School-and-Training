def dataSets():
    return print('How many data sets?\n'
                 'Typo number:\n')


def printMenu():
    return print("Type words after space\n"
                 "I will shorten this words:\n")


def notletterCheck(words):
    try:
        for word in words:
            assert str(word).isalpha()
    except AssertionError:
        print('not every string is built from letters\n'
              'run program again!')
        exit(0)


def howmanyCheck(number) -> int:
    try:
        number = int(number)
        return number
    except ValueError:
        print('Please put integer value in order to type datasets')

        exit(0)
