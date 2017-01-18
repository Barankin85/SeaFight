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
        for i in range(0,boardSize):
            for j in range(0,boardSize):
                if not self.positions[i][j].isFired:
                    result.append([i, j])
        return result

class Ship:
    def __init__(self, type):
        self.type = type
        self.positions = []
    
    def isAlive(self):
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
            for i in range(0,boardSize):
                for j in range(0,boardSize):
                    if any([i,j] == position for position in shipConfiguration["positions"]):
                        occupiedPosition = self.board.setOccipied(i, j)
                        ship.positions.append(occupiedPosition)
    
    def hasAliveShips(self):
        return any(ship.isAlive() for ship in self.ships)

    def fireBoard(self, x, y):
        self.board.setFired(x,y)

class AIPlayer(Player):
    def fireEnemyBoard(self, board):
        positionToFire = self._choosePosition(board)
        board.setFired(positionToFire[0], positionToFire[1])

    def _choosePosition(self, board):
        positions = board.getNotFiredPositions()
        return random.choice(positions)

class Game:
    def __init__(self):
        self.start()

    def fire(self, x, y):
        self.enemy.fireBoard(x, y)
        
        if not self.enemy.hasAliveShips():
            self.winner = self.you
        else:
            self.enemy.fireEnemyBoard(self.you.board)
            if not self.you.hasAliveShips():
                 self.winner = self.enemy

    def start(self):
        self.you = Player()
        self.enemy = AIPlayer()
        self.winner = None

game = Game()