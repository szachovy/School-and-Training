DICT_OF_VALUES = {7: 'millions ->', 6: 'hundreds thousands ->',
                  5: 'tens thousands ->', 4: 'thousands ->',
                  3: 'hundreds ->', 2: 'dozens ->', 1: 'units ->'}


class LookForNumbers:
    def __repr__(self):
        return 'During calculations'

    def __init__(self):
        self.__number = int
        self.result = 1

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        if not value:
            self.__number = 'Unknown'
        else:
            self.__number = value


class CalculateThis(object):
    def __init__(self, number):
        self.result = 1
        self.number = number

    def calculations(self):
        while self.number >= 1:
            self.result *= self.number
            self.number -= 1

        return self.result

    def separate(self):
        separatedList = [int(digits) for digits in str(self.result)]
        dict_of_val_appender = len(separatedList)

        for element in separatedList:
            print(DICT_OF_VALUES.get(dict_of_val_appender), end=' ')
            print(element)
            dict_of_val_appender -= 1