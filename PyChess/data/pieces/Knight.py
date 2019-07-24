import sys
sys.path.insert(0, '../')

import Piece

class Knight(Piece):
    def __init__(self, iswhite):
        Piece.__init__(self, PCE_ID_KNIGHT, iswhite)
