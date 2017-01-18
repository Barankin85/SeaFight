import random

class PositionState:
    NotFired, Missed, Hit = range(3)

States = PositionState()

class Position:
    def __init__(self, isOccupied, isFired):
        self.isOccupied = isOccupied
        self.isFired = isFired

boardSize = 10

class Board:
    def __init__(self):
        self.positions = [[Position(False, False) for x in range(boardSize)] for y in range(boardSize)]
    
    def setOccipied(self, x, y):
        self.positions[x][y].isOccupied = True
    
    def setFired(self, x, y):
        self.positions[x][y].isFired = True

    def getNotFiredPositions(self):
        result = []
        for i in range(0,boardSize-1):
            for j in range(0,boardSize-1):
                if not self.positions[i][j].isFired:
                    result.append([i, j])
        return result

class Layout:
    ships = [
        { "ship": "carrier", "positions": [[2,9], [3,9], [4,9], [5,9], [6,9]] },
        { "ship": "battleship", "positions": [[5,2], [5,3], [5,4], [5,5]] },
        { "ship": "cruiser", "positions": [[8,1], [8,2], [8,3]] },
        { "ship": "submarine", "positions": [[3,0], [3,1], [3,2]] },
        { "ship": "destroyer", "positions": [[0,0], [1,0]] }
    ]

    def getBoard(self):
        board = Board()
        for i in range(0,boardSize-1):
            for j in range(0,boardSize-1):
                for ship in self.ships:
                    if any([i,j] == position for position in ship["positions"]):
                        board.setOccipied(i, j)

        return board

class Player:
    def fire(self, board):
        positionToFire = self.choosePosition(board)
        board.setFired(positionToFire[0], positionToFire[1])
    
    def choosePosition(self, board):
        positions = board.getNotFiredPositions()
        return random.choice(positions)

class Game:
    yourBoard = Layout().getBoard()
    enemyBoard = Layout().getBoard()
    enemy = Player()

    def fire(self, x, y):
        self.enemyBoard.setFired(x,y)
        self.enemy.fire(self.yourBoard)

game = Game()