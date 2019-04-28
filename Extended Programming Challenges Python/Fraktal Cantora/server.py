import configparser
import socket
from json import dumps

def getConfig(section, option):
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config.get(section, option)


class Fractals(object):
    def __init__(self):
        self.rows = 0
        self.pattern = getConfig('DRAWING', 'pattern')
        self.breaks = getConfig('DRAWING', 'breaks')
        self.fractals = {}

    @property
    def rowsInput(self):
        return self.rows

    @rowsInput.setter
    def rowsInput(self, rows_number):
        try:
            rows_number = int(rows_number)
            assert rows_number in range(1, 11)

        except ValueError:
            print('Bad instance of value, please retry and input integer')
            return

        except AssertionError:
            print('Fractal rows must be in range from 1 to 10 included')
            return

        self.rows = rows_number

    def drawFractals(self):
        space = {0: ''}
        for row in range(self.rows):
            if row > 0:
                space[row] = eval(self.breaks) * 3**(self.rows - (row + 1))

            fill_row = (self.pattern * 3**(self.rows - (row + 1)) + space[row]) * 2**row

            self.fractals[row] = fill_row

        return self.fractals

    def server(self):
        print('Starting server...')
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        msg = dumps(self.drawFractals()).encode('utf-8')
        s.sendto(msg, (getConfig('SERVER', 'IPv4'), int(getConfig('SERVER', 'port'))))


if __name__ == '__main__':
    a = Fractals()
    while not a.rows:
        a.rowsInput = input('Please insert number of fractal rows')

    a.server()