import sys
sys.path.insert(0, '../')

import Piece

class Bishop(Piece):
    def __init__(self, iswhite):
        Piece.__init__(self, PCE_ID_BISHOP, iswhite)
