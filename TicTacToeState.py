#class that implements a state and the playing logic of the TicTacToe game.
import Square
from TicTacToeAction import TicTacToeAction


class TicTacToeState:
    def checkWinner(self, player):
        # Check rows
        for i in range(0, 9, 3):
            if self.field[i] == self.field[i+1] == self.field[i+2] == player:
                return True
        # Check columns
        for i in range(3):
            if self.field[i] == self.field[i+3] == self.field[i+6] == player:
                return True
        # Check diagonals
        if self.field[0] == self.field[4] == self.field[8] == player or self.field[2] == self.field[4] == self.field[6] == player:
            return True
        return False


    # Updates the utility value.
    def updateUtility(self):
        #print ("Updates the utility value.")
        if self.checkWinner(Square.X) == True:
            self.utility = 1
        elif self.checkWinner(Square.O) == True:
            self.utility = -1
        else:
            self.utility = 0
        # TODO The utility value for the TicTacToe game is defined as follows:
        #   - if player has three marks in a row, it is 1

        #   - if the other player has three marks in a row, it is -1
        #   - otherwise it is 0
        #   Note tha "three marks in a row" can actually be a row, a column
        #   or a diagonal.So basically, first find out if there are three
        #   identical values in a row, and if so, check whether the marks belong
        #   to player or not.


    # Default constructor.
    def __init__(self):
        self.field = [] # < The field, consisting of nine squares.First three values correspond to first row, and so on.
        for i in range(9):
            self.field.append(Square.EMPTY)
        self.player = Square.X # < The player who started
        self.playerToMove = Square.X # < The player that is about to move.
        self.utility = 0 # < The utility value of this state.Can be 0, 1 (won) or -1 (lost).
        self.numMoves = 0

    def getActions(self):
        #  TODO For the TicTacToe game, there is one valid action
        #   for each empty square.The action would then consist
        #   of the position of the empty square and the "color" of
        #   the player to move.
        #print("getActions")
        actions = []
        for position, square in enumerate(self.field):
            if square == Square.EMPTY:
                action = TicTacToeAction(self.playerToMove, position)
                actions.append(action)
        return actions

    def getUtility(self):
        return self.utility

    def getResult(self, action):
    
        new_state = TicTacToeState()
        new_state.field = self.field.copy()
        new_state.numMoves = self.numMoves + 1
    
        new_state.player = self.playerToMove #Last Player
        #new_state.player = self.player
        # Invert the playerToMove for the new state
        new_state.playerToMove = Square.O if self.playerToMove == Square.X else Square.X
    
        # Add resulting action to field
        position = action.getPosition()
        new_state.field[position] = action.getPlayer()
    
        new_state.updateUtility()
    
        return new_state


    def  isTerminal(self):
        #TODO Hint: the utility value has specific values if one of
        # the players has won, which is a terminal state. However,
        # you will also have to check for terminal states in which
        # no player has won, which can not be inferred immediately
        # from the utility value.
        if self.numMoves == 9 and self.utility == 0:
            #print("No Winner")
            return True
        if self.utility == 1 or self.utility == -1:
            #print("Winner detected")
            return True
        return False

    def printresult(self):
        s = "" + self.field[0] + "|" + self.field[1] + "|" + self.field[2] + "\n"
        s += "-+-+-\n"
        s += self.field[3] + "|" + self.field[4] + "|" + self.field[5] + "\n"
        s += "-+-+-\n"
        s += self.field[6] + "|" + self.field[7] + "|" + self.field[8] + "\n"
        print(s)