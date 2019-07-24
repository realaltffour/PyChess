import pieces
import Piece

class Board:
    m_WhiteTurn = True
    m_Board_W = 8
    m_Board_H = 8
    m_Board = [Piece] * (m_Board_W * m_Board_H)


    def __init__(self):
        # set-up back row, white's pieces.
        self.setLoc(0,0, PCE_ID_ROOK)
        self.setLoc(1,0, PCE_ID_KNIGHT)
        self.setLoc(2,0, PCE_ID_BISHOP)
        self.setLoc(3,0, PCE_ID_QUEEN)
        self.setLoc(4,0, PCE_ID_KING)
        self.setLoc(5,0, PCE_ID_BISHOP)
        self.setLoc(6,0, PCE_ID_KNIGHT)
        self.setLoc(7,0, PCE_ID_ROOK)
        
        # set-up front row, white's pieces.
        for i in range(self.m_Board_W)
            self.setLoc(i, 1, PCE_ID_PAWN)

        # set-up back row, black's pieces.
        self.setLoc(0,8, PCE_ID_ROOK)
        self.setLoc(1,8, PCE_ID_KNIGHT)
        self.setLoc(2,8, PCE_ID_BISHOP)
        self.setLoc(4,8, PCE_ID_KING)
        self.setLoc(3,8, PCE_ID_QUEEN)
        self.setLoc(5,8, PCE_ID_BISHOP)
        self.setLoc(6,8, PCE_ID_KNIGHT)
        self.setLoc(7,8, PCE_ID_ROOK)
        
        # set-up front row, black's pieces.
        for i in range(self.m_Board_W)
            self.setLoc(i, 7, PCE_ID_PAWN)


    def getLoc(col, row):
        return self.m_Board[(self.m_Board_W*row)+col]

    def setLoc(col, row, pce_id, iswhite):
        self.m_Board[(self.m_Board_W*row)+col] = Piece(pce_id, iswhite)
