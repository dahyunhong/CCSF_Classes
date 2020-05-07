"""
Dahyun Hong
Project 1
CS110A

This program plays rock, scissors, paper with the computer.
"""

import random


def getPlayerMove():
    """ 
    Gets the player's move. Validates that it is valid move

    Returns: 
      string: The validated player move 
    """
    MOVES = ['rock', 'paper', 'scissors', 'scissor']
    playerMove = input(
        'Please enter your move: Paper, Rock, or Scissors: ').lower()
    while (playerMove not in MOVES):
        print("You must enter a valid move!")
        playerMove = input(
            'Please enter your move: Paper, Rock, or Scissors: ').lower()
    return playerMove


def getComputerMove():
    """ 
    Gets the computer's move using random integer and list of moves

    Returns: 
      string: The random computer move 
    """
    MOVES = ['rock', 'paper', 'scissors']
    move = random.randrange(0, 3)
    print("Computer move is {}".format(MOVES[move]))
    return MOVES[move]


def winner(playerMove, computerMove):
    """ 
    Gets who the winner of rock paper scissors is is using two moves

    Parameters:
      playerMove: String: The player's move
      computerMove: String: The computer's move

    Returns: 
      string: The result of rock paper scissors 
    """
    if(playerMove == computerMove):
        print('Tie with {}'.format(playerMove))
    elif(playerMove == 'rock' and computerMove == 'paper'):
        print('Computer wins! Paper covers rock')
    elif(playerMove == 'paper' and computerMove == 'rock'):
        print('Player wins! Paper covers rock')
    elif((playerMove == 'scissor' or playerMove == 'scissors') and computerMove == 'paper'):
        print('Player wins! Scissors cuts paper')
    elif((computerMove == 'scissor' or computerMove == 'scissors') and playerMove == 'paper'):
        print('computer wins! Scissors cuts paper')
    elif(playerMove == 'rock' and (computerMove == 'scissor' or computerMove == 'scissors')):
        print('Player wins! Rock beats scissors')
    elif(computerMove == 'rock' and (playerMove == 'scissor' or playerMove == 'scissors')):
        print('computer wins! Rock beats scissors')


def again():
    return input('Go again? (y/n) ').lower()


def main():
    goAgain = 'y'

    while (goAgain == 'y'):
        playerMove = getPlayerMove()
        computerMove = getComputerMove()
        winner(playerMove, computerMove)

        print()
        goAgain = again()

    print("Thanks for playing!")
    print()


main()
