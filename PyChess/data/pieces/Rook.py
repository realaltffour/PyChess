import sys
sys.path.insert(0, '../')

import Piece

class Rook(Piece):
    def __init__(self, iswhite):
        Piece.__init__(self, PCE_ID_ROOK, iswhite)
