import Pieces, Drawing

X, Y = Drawing.X, Drawing.Y

def start(list):
    
    list.clear()

    x,y = 0,0
    list.append(Pieces.Rook(x,y,"B"))
    x += X/8
    list.append(Pieces.Knight(x,y,"B"))
    x += X/8
    list.append(Pieces.Bishop(x,y,"B"))
    x += X/8
    list.append(Pieces.Queen(x,y,"B"))
    x += X/8
    list.append(Pieces.King(x,y,"B"))
    x += X/8
    list.append(Pieces.Bishop(x,y,"B"))
    x += X/8
    list.append(Pieces.Knight(x,y,"B"))
    x += X/8
    list.append(Pieces.Rook(x,y,"B"))

    x,y = 0,Y/8*7
    list.append(Pieces.Rook(x,y,"W"))
    x += X/8
    list.append(Pieces.Knight(x,y,"W"))
    x += X/8
    list.append(Pieces.Bishop(x,y,"W"))
    x += X/8
    list.append(Pieces.Queen(x,y,"W"))
    x += X/8
    list.append(Pieces.King(x,y,"W"))
    x += X/8
    list.append(Pieces.Bishop(x,y,"W"))
    x += X/8
    list.append(Pieces.Knight(x,y,"W"))
    x += X/8
    list.append(Pieces.Rook(x,y,"W"))

    x,y = 0,Y/8
    for i in range(8):
        list.append(Pieces.Pawn(x,y,"B"))
        x += X/8

    x,y = 0,Y/8*6
    for i in range(8):
        list.append(Pieces.Pawn(x,y,"W"))
        x += X/8

    return list


def pole(XY):
    y = 0
    for i in range(8):
        x = 0
        for j in range(8):
            if XY[0] >= x and XY[0] <= x + X/8 and XY[1] >= y and XY[1] <= y + Y/8:
                return (x,y)
            x += X/8
        y += Y/8


def is_occupied(list, XY):
    for figura in list:
        if figura.get_xy() == XY:
            return True
    return False


def to_capture(list, XY, kolor):
    for figura in list:
        if figura.get_xy() == XY and figura.get_kolor() != kolor:
            return True
    return False

def in_board(XY):
    if XY[0] >= 0 and XY[0] < X and XY[1] >= 0 and XY[1] < Y:
        return True
    else:
        return False

def is_right_rook_good(list,kolor):
    if kolor == "W":
        for figura in list:
            XY = figura.get_xy()
            if XY[0] == 7*X/8 and XY[1] == 7*Y/8 and figura.get_first_move():
                return True

    if kolor == "B":
        for figura in list:
            XY = figura.get_xy()
            if XY[0] == 7*X/8 and XY[1] == 0 and figura.get_first_move():
                return True
    
    return False

def is_left_rook_good(list,kolor):
    if kolor == "W":
        for figura in list:
            XY = figura.get_xy()
            if XY[0] == 0 and XY[1] == 7*Y/8 and figura.get_first_move():
                return True

    if kolor == "B":
        for figura in list:
            XY = figura.get_xy()
            if XY[0] == 0 and XY[1] == 0 and figura.get_first_move():
                return True
    
    return False

def right_castle(list, kolor):
    if kolor == "W":
        XY = (7*X/8,7*Y/8)
    else:
        XY = (7*X/8,0)

    king = king_pointer(list, kolor)

    if is_occupied(list, (5*X/8,XY[1])) or is_occupied(list, (6*X/8,XY[1])) or not is_right_rook_good(list,kolor):
        return False

    king.fake_move((5*X/8,XY[1]))
    if check(list, kolor):
        king.fake_move((X/2,XY[1]))
        return False
    else:
        king.fake_move((X/2,XY[1]))

    king.fake_move((6*X/8,XY[1]))
    if check(list, kolor):
        king.fake_move((X/2,XY[1]))
        return False
    else:
        king.fake_move((X/2,XY[1]))
        return True
      
def left_castle(list, kolor):
    if kolor == "W":
        XY = (7*X/8,7*Y/8)
    else:
        XY = (7*X/8,0)

    king = king_pointer(list, kolor)

    if is_occupied(list, (3*X/8,XY[1])) or is_occupied(list, (2*X/8,XY[1])) or is_occupied(list, (X/8,XY[1])) or not is_left_rook_good(list,kolor):
        return False

    king.fake_move((3*X/8,XY[1]))
    if check(list, kolor):
        king.fake_move((X/2,XY[1]))
        return False
    else:
        king.fake_move((X/2,XY[1]))

    king.fake_move((2*X/8,XY[1]))
    if check(list, kolor):
        king.fake_move((X/2,XY[1]))
        return False
    else:
        king.fake_move((X/2,XY[1]))

    king.fake_move((X/8,XY[1]))
    if check(list, kolor):
        king.fake_move((X/2,XY[1]))
        return False
    else:
        king.fake_move((X/2,XY[1]))
        return True
#wersja dla obracanej planszy
'''
def is_right_rook_good(list,kolor):
    for figura in list:
        XY = figura.get_xy()
        if XY[0] == 7*X/8 and XY[1] == 7*Y/8 and figura.get_first_move():
            return True
    
    return False

def is_left_rook_good(list,kolor):
    
    for figura in list:
        XY = figura.get_xy()
        if XY[0] == 0 and XY[1] == 7*Y/8 and figura.get_first_move():
            return True
    
    return False

def right_castle(list, kolor):
    
    XY = (7*X/8,7*Y/8)

    king = king_pointer(list, kolor)

    if is_occupied(list, (5*X/8,XY[1])) or is_occupied(list, (6*X/8,XY[1])) or not is_right_rook_good(list,kolor):
        return False

    king.fake_move((5*X/8,XY[1]))
    if check(list, kolor):
        king.fake_move((X/2,XY[1]))
        return False
    else:
        king.fake_move((X/2,XY[1]))

    king.fake_move((6*X/8,XY[1]))
    if check(list, kolor):
        king.fake_move((X/2,XY[1]))
        return False
    else:
        king.fake_move((X/2,XY[1]))
        return True
      
def left_castle(list, kolor):
   
    XY = (7*X/8,7*Y/8)

    king = king_pointer(list, kolor)

    if is_occupied(list, (3*X/8,XY[1])) or is_occupied(list, (2*X/8,XY[1])) or is_occupied(list, (X/8,XY[1])) or not is_left_rook_good(list,kolor):
        return False

    king.fake_move((3*X/8,XY[1]))
    if check(list, kolor):
        king.fake_move((X/2,XY[1]))
        return False
    else:
        king.fake_move((X/2,XY[1]))

    king.fake_move((2*X/8,XY[1]))
    if check(list, kolor):
        king.fake_move((X/2,XY[1]))
        return False
    else:
        king.fake_move((X/2,XY[1]))

    king.fake_move((X/8,XY[1]))
    if check(list, kolor):
        king.fake_move((X/2,XY[1]))
        return False
    else:
        king.fake_move((X/2,XY[1]))
        return True
'''

def king_pointer(list,kolor):
    for figura in list:
        if type(figura) == Pieces.King and figura.get_kolor() == kolor:
            return figura

def check(list, kolor):
    for figura in list:
        if figura.get_kolor() != kolor:
            for move in figura.possible_moves():
                if move == king_pointer(list, kolor).get_xy():
                    return True
    return False

def draw(list,kolor):

    for figura in list:
        if figura.get_kolor() == kolor:
            test_moves = []
            possible_moves = figura.possible_moves()
            for move in possible_moves:
                test_moves.append(move)
                            
            for move in test_moves:
                pozycja = figura.get_xy()
                test_list = []

                for piece in list:
                    test_list.append(piece)

                for piece in test_list:
                    if piece.get_xy() == move:
                        test_list.remove(piece)
                figura.fake_move(move)

                if check(test_list,kolor):
                    possible_moves.remove(move)
                              
                figura.fake_move(pozycja)
            if len(possible_moves) > 0:
                return False
    return True

def turn(list):
    for figur in list:
        XY = figur.get_xy()
        for i in range(8):
            if XY[1] == i*Y/8:
                figur.fake_move((XY[0], int(7*Y/8-i*Y/8)))
    