import abc
from math import ceil

class Page(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def display(self, records, records_on_page, page_number):
        raise NotImplementedError('Display function not implemented')

    # noinspection PyDeprecation
    @abc.abstractstaticmethod
    def set_alert():
        raise NotImplementedError('Alert pages is in demand of operating on pages finite')


class MoveNext(Page):
    @staticmethod
    def set_alert(state = False):
        return state

    def display(self, records, records_on_page, page_number):
        alert = False
        number_of_pages = ceil(records/records_on_page)

        if page_number > number_of_pages:
            page_number -= 1
            alert = self.set_alert(True)

        for record in range(records_on_page):
            if records < (records_on_page * (page_number - 1)) + record:
                continue
            else:
                print('record', (records_on_page * (page_number - 1)) + record)
            
        for page in range(number_of_pages):
            if page_number > number_of_pages:
                break
            if page + 1 == page_number:
                print('[', page + 1, ']', sep='', end=' ')
            else:
                print(page + 1, end=' ')

        if alert:
            Pagination().page_num_too_big()


class MovePrevious(Page):
    @staticmethod
    def set_alert(state=False):
        return state

    def display(self, records, records_on_page, page_number):
        alert = False
        number_of_pages = ceil(records / records_on_page)

        if page_number <= 0:
            page_number += 1
            alert = self.set_alert(True)

        for record in range(records_on_page):
            print('record', (records_on_page * (page_number - 1)) + record)

        for page in range(number_of_pages):
            if page + 1 == page_number:
                print('[', page + 1, ']', sep='', end=' ')
            else:
                print(page + 1, end=' ')

        if alert:
            Pagination().page_num_too_small()


class Pagination(object):
    page_number = 0

    def __getattr__(self, item):
        if item == 'n':
            self.move('MoveNext', True)
        elif item == 'p':
            self.move('MovePrevious', False)
        else:
            print('wrong key, retry')

    @classmethod
    def records(cls):
        try:
            cls.records_number = int(input('Type number of records'))
        except ValueError:
            print('Integer expected, try again')
            cls.records()

        return cls.records_number

    @classmethod
    def records_on_page(cls):
        try:
            cls.records_on_page_number = int(input('Type number of records displayed on one single page'))
        except ValueError:
            print('Integer expected, try again')
            cls.records_on_page()

        return cls.records_on_page_number

    @classmethod
    def move(cls, name, is_next):
        if is_next:
            cls.page_number += 1
        else:
            cls.page_number -= 1
        return eval(name)().display(cls.records_number, cls.records_on_page_number, cls.page_number)

    @classmethod
    def page_num_too_big(cls):
        cls.page_number -= 1

    @classmethod
    def page_num_too_small(cls):
        cls.page_number += 1


if __name__ == '__main__':
    side = Pagination()
    side.records()
    side.records_on_page()
    print('How do you want to move your page?\n'
          '[n] -> next\n'
          '[p] -> previous\n'
          '[e] -> exit')
    while True:
        arg = input()
        #xd
        if arg == 'n':
            side.n
        elif arg == 'p':
            side.p
        elif arg == 'e':
            quit(0)
        else:
            side.arg
