
#Alex Nickle
#August 28, 2022
# rps.py
# a python version of rock paper scissors lizard spock
# 

import random, sys

print('ROCK, PAPER, SCISSORS, LIZARD, SPOCK')

# These variables keep track of the number of wins, losses, and ties.
wins = 0
losses = 0
ties = 0

while True: # The main game loop.
    print(f'{wins} wins, {losses} losses, {ties} ties')
    while True: # The player input loop.
        print('Enter your move: (r)ock (p)aper (x)cissors (l)izard (s)pock or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit() # Quit the program.
        if playerMove == 'r' or playerMove == 'p' or playerMove == 'x' or playerMove == 'l' or playerMove == 's':
            break # Break out of the player input loop.
        print('Type one of r, p, x, l, s, or q.')

    # Display what the player chose:
    if playerMove == 'r':
        print('ROCK versus...')
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove == 'x':
        print('SCISSORS versus...')
    elif playerMove == 'l':
        print('LIZARD versus...')
    elif playerMove == 's':
        print('SPOCK versus...')

    # Display what the computer chose:
    randomNumber = random.randint(1, 5)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 'x'
        print('SCISSORS')
    elif randomNumber == 4:
        computerMove = 'l'
        print('LIZARD')
    elif randomNumber == 5:
        computerMove = 's'
        print('SPOCK')

    # Display and record the win/loss/tie:
    if playerMove == computerMove:
        print('It is a tie!')
        ties+=1

    elif playerMove == 'r':
        if computerMove == 'x' or computerMove == 'l':
            print('You win!')
            wins+=1
        else:
            print('You lose!')
            losses+=1

    elif playerMove == 'p':
        if computerMove == 'r' or computerMove == 's':
            print('You win!')
            wins+=1
        else:
            print('You lose!')
            losses+=1

    elif playerMove == 'x':
        if computerMove == 'p' or computerMove == 'l':
            print('You win!')
            wins+=1
        else:
            print('You lose!')
            losses+=1

    elif playerMove == 'l':
        if computerMove == 's' or computerMove == 'p':
            print('You win!')
            wins+=1
        else:
            print('You lose!')
            losses+=1

    elif playerMove == 's':
        if computerMove == 'x' or computerMove == 'r':
            print('You win!')
            wins+=1
        else:
            print('You lose!')
            losses+=1




            


