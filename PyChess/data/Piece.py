
PCE_ID_KING = 1
PCE_ID_QUEEN = 2
PCE_ID_ROOK = 3
PCE_ID_BISHOP = 4
PCE_ID_KNIGHT = 5
PCE_ID_PAWN = 6

class Piece:
    m_ID = -1
    m_WhitePCE = True

    def __init__(self, id, iswhite):
       self.m_ID = id
       self.m_WhitePCE = iswhite
    
    def name():
        if self.m_ID == PCE_ID_KING: return 'K'
        if self.m_ID == PCE_ID_QUEEN: return 'Q'
        if self.m_ID == PCE_ID_ROOK: return 'R'
        if self.m_ID == PCE_ID_BISHOP: return 'B'
        if self.m_ID == PCE_ID_KNIGHT: return 'Kn'
        if self.m_ID == PCE_ID_PAWN: return 'P'

    def fullname():
        if self.m_ID == PCE_ID_KING: return 'King'
        if self.m_ID == PCE_ID_QUEEN: return 'Queen'
        if self.m_ID == PCE_ID_ROOK: return 'Rook'
        if self.m_ID == PCE_ID_BISHOP: return 'Bishop'
        if self.m_ID == PCE_ID_KNIGHT: return 'Knight'
        if self.m_ID == PCE_ID_PAWN: return 'Pawn'

    def value(id):
        if id == PCE_ID_KING: return 999
        if id == PCE_ID_QUEEN: return 9
        if id == PCE_ID_ROOK: return 6
        if id == PCE_ID_BISHOP: return 3.25
        if id == PCE_ID_KNIGHT: return 3
        if id == PCE_ID_PAWN: return 1
