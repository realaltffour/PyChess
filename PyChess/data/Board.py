import pieces
import Piece

class Board:
    m_WhiteTurn = True
    m_Board = [Piece] * 64
    m_Board_W = 8
    m_Board_H = 8

    def getLoc(row, col):
        return self.m_Board[(self.m_Board_W*row)+col]

    def setLoc(row, col, pce_id):
        self.m_Board[(self.m_Board_W*row)+col] = Piece(pce_id)
