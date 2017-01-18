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
        position = self.positions[x][y]
        position.isOccupied = True
        return position
    
    def setFired(self, x, y):
        self.positions[x][y].isFired = True

    def getNotFiredPositions(self):
        result = []
        for i in range(0,boardSize-1):
            for j in range(0,boardSize-1):
                if not self.positions[i][j].isFired:
                    result.append([i, j])
        return result

class Ship:
    def __init__(self, type):
        self.type = type
        self.positions = []
    
    def isAlive():
        return len(self.positions) == 0 or any(position.isFired == False for position in self.positions)

class Player:
    shipsConfiguration = [
        { "ship": "carrier", "positions": [[2,9], [3,9], [4,9], [5,9], [6,9]] },
        { "ship": "battleship", "positions": [[5,2], [5,3], [5,4], [5,5]] },
        { "ship": "cruiser", "positions": [[8,1], [8,2], [8,3]] },
        { "ship": "submarine", "positions": [[3,0], [3,1], [3,2]] },
        { "ship": "destroyer", "positions": [[0,0], [1,0]] }
    ]

    def __init__(self):
        self.ships = []
        self.board = Board()
        
        for shipConfiguration in self.shipsConfiguration:
            ship = Ship(shipConfiguration["ship"])
            self.ships.append(ship)
            for i in range(0,boardSize-1):
                for j in range(0,boardSize-1):
                    if any([i,j] == position for position in shipConfiguration["positions"]):
                        occupiedPosition = self.board.setOccipied(i, j)
                        ship.positions.append(occupiedPosition)

    def fire(self, board):
        positionToFire = self.choosePosition(board)
        board.setFired(positionToFire[0], positionToFire[1])
    
    def choosePosition(self, board):
        positions = board.getNotFiredPositions()
        return random.choice(positions)

class Game:
    you = Player()
    enemy = Player()

    def fire(self, x, y):
        self.enemy.board.setFired(x,y)
        self.enemy.fire(self.you.board)

game = Game()