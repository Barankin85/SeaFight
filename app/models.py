import random

#class for single field on the game board
class Position:
    def __init__(self, isOccupied, isFired):
        self.isOccupied = isOccupied  #flad indicates whether position is occupied with some ship
        self.isFired = isFired #flag indicates whether position was fired by enemy

#width and height of board
boardSize = 10

#class for game board
class Board:
    def __init__(self):
        self.positions = [[Position(False, False) for x in range(boardSize)] for y in range(boardSize)] #set all positions as not occupied and not fired
    
    #sets position with specified coordinates as occupied and returns it
    def setOccipied(self, x, y):
        position = self.positions[x][y]
        position.isOccupied = True
        return position

    def isOccupied(self, x, y):
        return self.positions[x][y].isOccupied
    
    #sets position with specified coordinates as fired
    def setFired(self, x, y):
        self.positions[x][y].isFired = True

    #gets all not fired positions
    def getNotFiredPositions(self):
        result = []
        for i in range(0,boardSize):
            for j in range(0,boardSize):
                if not self.positions[i][j].isFired:
                    result.append([i, j])
        return result

#class for ship
class Ship:
    def __init__(self, type):
        self.type = type #ship type (carrier, battleship etc.)
        self.positions = [] #list of positions occupied by ship
    
    #indicates whether ship is alive - has at least one not fired position
    def isAlive(self):
        return len(self.positions) == 0 or any(position.isFired == False for position in self.positions)

#class for player
class Player:
    #default ships layout configuration
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
    
    #indicates whether the player has at least one alive ship
    def hasAliveShips(self):
        return any(ship.isAlive() for ship in self.ships)

    #fires board position with specified coordinates
    def fireBoard(self, x, y):
        self.board.setFired(x,y)

#class for computer player 
class AIPlayer(Player):
    #fires some enemy board position
    def fireEnemyBoard(self, board):
        positionToFire = self._choosePosition(board)
        board.setFired(positionToFire[0], positionToFire[1])

    #chooses position to fire randomly from list of all not fired positions
    def _choosePosition(self, board):
        positions = board.getNotFiredPositions()
        return random.choice(positions)

#class for game
class Game:
    def __init__(self):
        self.start()

    #fires board position of computer player and call computer player to fire board of human player
    #returns True is ship was hit otherwise returns False
    def fire(self, x, y):
        self.enemy.fireBoard(x, y)
        
        #if some of players don`t have alive ships - his foe is a winner
        if not self.enemy.hasAliveShips():
            self.winner = self.you
        else:
            self.enemy.fireEnemyBoard(self.you.board)
            if not self.you.hasAliveShips():
                 self.winner = self.enemy

        return self.enemy.board.isOccupied(x, y)

    #sets game to initial state
    def start(self):
        self.you = Player()
        self.enemy = AIPlayer()
        self.winner = None

game = Game()