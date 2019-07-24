import pieces
import Piece

class Board:
    m_WhiteTurn = True
    m_Board = [Piece] * (m_Board_W * m_Board_H)
    m_Board_W = 8
    m_Board_H = 8

    def __init__(self):
        # set-up back row, white's pieces.
        self.setLoc(0,0, PCE_ID_ROOK)
        self.setLoc(1,0, PCE_ID_KNIGHT)
        self.setLoc(2,0, PCE_ID_BISHOP)
        self.setLoc(3,0, PCE_ID_QUEEN)
        self.setLoc(4,0, PCE_ID_KING)
        self.setLoc()

    def getLoc(col, row):
        return self.m_Board[(self.m_Board_W*row)+col]

    def setLoc(col, row, pce_id):
        self.m_Board[(self.m_Board_W*row)+col] = Piece(pce_id)
