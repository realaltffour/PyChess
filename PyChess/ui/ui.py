import Board
import Piece
import pieces
import os
import sys

sys.path.insert(0, '../data/')
# function to clear the console after user choose
def cls():
    os.system('Cls ' if os.name =='nt' else 'clear')

def Menu():
    print("Welcome To PyChess!\n 1) Start\n 2) Settings\n 3) Credits\n 4) Quit")

    User = input()

    if User == '1':
        cls()
        # Put Here The Game
        

    elif User == '2':
        #Up Comming Feature
        cls()

#credits here
    elif User == '3':
        cls()
        print('PyChess is Co-op Chess Game made by Ayham Mamoun and Ali Alboainin\nCheck Our Github Account\n\nhttps://github.com/realaltffour\nhttps://github.com/alialboainin96\n')
#quit command
    elif User == '4':
        print(sys.exit)
        cls()
Menu()
