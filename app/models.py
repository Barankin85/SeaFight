class PositionState:
    NotFired, Missed, Hit = range(3)

States = PositionState()

class Position:
    def __init__(self, occupied, isFired):
        self.occupied = occupied
        self.isFired = isFired

class Layout:
    ships = [
        { "ship": "carrier", "positions": [[2,9], [3,9], [4,9], [5,9], [6,9]] },
        { "ship": "battleship", "positions": [[5,2], [5,3], [5,4], [5,5]] },
        { "ship": "cruiser", "positions": [[8,1], [8,2], [8,3]] },
        { "ship": "submarine", "positions": [[3,0], [3,1], [3,2]] },
        { "ship": "destroyer", "positions": [[0,0], [1,0]] }
    ]

    def getBoard(self):
        result = [[Position(False, False) for x in range(10)] for y in range(10)] 
        for i in range(0,9):
            for j in range(0,9):
                for ship in self.ships:
                    if any([i,j] == position for position in ship["positions"]):
                        result[i][j] = Position(True, False)

        return result

class Game:
    yourBoard = Layout().getBoard()
    enemyBoard = Layout().getBoard()

    def fire(self, x, y):
        # print 'fired ' + str(x) + ' ' + str(y)
        self.enemyBoard[x][y].isFired = True;

game = Game()