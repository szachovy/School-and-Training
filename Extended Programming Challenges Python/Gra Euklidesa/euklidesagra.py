import matplotlib.pyplot as plt
import pandas as pd
import random

class Preparation(object):
    def __repr__(self):
        return "Table is cleaning..."

    def setRange(self):
        ran = input('what range of possibilities you want to set ?')
        if Preparation().setRangeCHECK(ran):
            return int(ran)
        else:
            Preparation().setRange()

    def setRangeCHECK(self, ran):
        try:
            ran = int(ran)
            assert ran > 1
        except ValueError:
            print('Int type of range is expected!')
            return False
        except AssertionError:
            print('Required integer must be bigger than one!')
            return False
        return True

class Player(object):
    def __init__(self, getRange):
        self.data = []
        self.value = random.randint(1, getRange)

    def __setitem__(self, key):
        if isinstance(key, int):
            self.data[key] = self.value
        else:
            raise ValueError('Key must be an int!')

    def __getitem__(self, item):
        return self.data[item]

class Game(Preparation, Player):
    pass

def game(ran1, ran2, tableList, playerList):
    allcredits, gameRounds = 0, 0
    while ran1 != ran2:
        if ran1 > ran2:
            ran1 -= ran2
            print(allcredits)
            allcredits += ran2
            playerList.append('Player One')
        elif ran2 > ran1:
            ran2 -= ran1
            print(allcredits)
            allcredits += ran1
            playerList.append('Player Two')
        tableList.append(allcredits)
        gameRounds += 1
    return gameRounds


if __name__ == '__main__':
    tableList, playerList, gameRoundsFinal = [], [], []
    plt.title('Game time graph')
    plt.xlabel('Credits Taken')
    plt.ylabel('Round')
    print(Preparation())
    Player1 = Game(Preparation().setRange())
    print(Player1.value)
    Player2 = Game(Preparation().setRange())
    print(Player2.value)
    gameRounds = game(Player1.value, Player2.value, tableList, playerList)
    for i in range(gameRounds):
        gameRoundsFinal.append(i)
    dataSet = pd.DataFrame()
    dataSet['Credits_Taken'] = tableList
    dataSet['Taken_From'] = playerList
    print(dataSet)
    plt.plot(tableList, gameRoundsFinal)
    plt.legend()
    plt.show()