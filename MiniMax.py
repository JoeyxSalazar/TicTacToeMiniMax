#class that implements the MiniMax algorithm.
import random
import sys

import Square
from TicTacToeAction import TicTacToeAction


class MiniMax:
    def __init__(self):
        self.numberOfStates=0 #< counter to measure the number of iterations / states.
        self.usePruning=False

    # Start procedure of the MiniMax algorithm.
    # state: The state where the MiniMax algorithm starts searching
    # usePruning: Whether to use alpha - beta - pruning
    # return An optimal action to be taken at this point.
    def MinimaxDecision(self, state, usePruning):
        self.usePruning = usePruning
        self.numberOfStates = 0
        best_action = None
        best_value = float('-inf')
        print("Computer's Turn")
        for action in state.getActions():
            result_state = state.getResult(action)
            if state.player == Square.X:  # Computer Goes First
                value = self.MaxValue(result_state, float('-inf'), float('inf'))
            else: #Player went first
                value = self.MinValue(result_state, float('-inf'), float('inf'))
            # Check if this action results in a better value.
            if value > best_value:
                best_action = action
                best_value = value
        
        print("State space size: ", self.numberOfStates)
        return best_action

    # state: The current state to be evaluated
    # alpha: The current value for alpha
    # beta: The current value for beta
    # return The minimum of the utilites invoking MaxValue, or the utility of the state if it is a leaf.
    def MinValue(self, state, alpha, beta):
        self.numberOfStates += 1
        # TODO implement the MaxValue procedure according to the textbook:
        #  function Min - Value(state, alpha, beta) return a utility value
        #       if TERMINAL - TEST(state) then return UTILITY(state)
        #       v < - +infinity
        #       for each a in ACTIONS(State) do
        #           v < - min(v, MAX-VALUE(RESULT(state, a), alpha, beta))
        #           if MiniMax.usePruning then
        #               if v <= alpha then return v
        #               beta < - min(beta, v)
        #       return v
        # The pseudo code is slightly changed to be able to reuse the code for alpha-beta-pruning.

        # Terminal test: Check if the state is a terminal state.
        if state.isTerminal():
            return state.getUtility()

        v = float('inf')

        for action in state.getActions():
            result_state = state.getResult(action)
            v = min(v, self.MaxValue(result_state, alpha, beta))

            if self.usePruning:
                if v <= alpha:
                    return v
                beta = min(beta, v)

        return v

    # state: The current state to be evaluated
    # alpha: The current value for alpha
    # beta: The current value for beta
    # The maximum of the utilites invoking MinValue, or the utility of the state if it is a leaf.
    def MaxValue(self,state,alpha,beta):
        self.numberOfStates+=1
        # TODO implement the MaxValue procedure according to the textbook:
        #  function Max - Value(state, alpha, beta) return a utility value
        #       if TERMINAL - TEST(state) then return UTILITY(state)
        #       v < - -infinity
        #       for each a in ACTIONS(State) do
        #           v < - max(v, MIN-VALUE(RESULT(state, a), alpha, beta))
        #           if MiniMax.usePruning then
        #               if v >= beta then return v
        #               alpha < - max(alpha, v)
        #       return v
        # The pseudo code is slightly changed to be able to reuse the * code for alpha-beta-pruning.

    # Terminal test: Check if the state is a terminal state.
        if state.isTerminal():
            return state.getUtility()

        v = float('-inf')


        for action in state.getActions():
            result_state = state.getResult(action)
            v = max(v, self.MinValue(result_state, alpha, beta))

            if self.usePruning:
                if v >= beta:
                    return v
                alpha = max(alpha, v)

        return v