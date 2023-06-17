import Board, Drawing

X, Y = Drawing.X, Drawing.Y

class Piece:
    list_of_figures = []
    list_of_moves = []

    def __init__(self, x, y, kolor):
        self.x = x
        self.y = y
        self.kolor = kolor

    def get_xy(self):
        return (self.x, self.y)

    def get_kolor(self):
        return self.kolor

    def draw_piece():
        pass

    def was_selected(self,XY):
        if self.x == XY[0] and self.y == XY[1]:
           return True

    def possible_moves(self):
        pass

    def move(self, XY):
        self.x = XY[0]
        self.y = XY[1]

    def fake_move(self, XY):
        self.x = XY[0]
        self.y = XY[1]


class Pawn(Piece):
    def __init__(self, x, y, kolor):
        super().__init__(x, y, kolor)
        self.first_move = True
        self.passant = False

    def draw_piece(self):
        Drawing.draw_pawn(self.kolor, (self.x,self. y))

    def get_passant(self):
        return self.passant

    def set_passant(self):
        self.passant = False

    def possible_moves(self):

        list = []
        x, y = self.x, self.y

        if self.kolor == "B":

            if not Board.is_occupied(self.list_of_figures, (x, y + Y/8)):
                if self.first_move and not Board.is_occupied(self.list_of_figures, (x, y + 2*Y/8)):
                    list.append((x, y + 2*Y/8))
                list.append((x, y + Y/8))

            if Board.to_capture(self.list_of_figures, (x + X/8, y + Y/8), self.kolor):
                list.append((x + X/8, y + Y/8))
            if Board.to_capture(self.list_of_figures, (x - X/8, y + Y/8), self.kolor):
                list.append((x - X/8, y + Y/8))

            for figura in self.list_of_figures:
                if figura.get_xy() == (x + X/8, y):
                    if type(figura) == Pawn and figura.get_passant() and figura.get_kolor() != self.kolor:
                        list.append((x+X/8,y+Y/8))
            for figura in self.list_of_figures:
                if figura.get_xy() == (x - X/8, y):
                    if type(figura) == Pawn and figura.get_passant() and figura.get_kolor() != self.kolor:
                        list.append((x-X/8,y+Y/8))
        
        if self.kolor == "W":

            if not Board.is_occupied(self.list_of_figures, (x, y - Y/8)):
                if self.first_move and not Board.is_occupied(self.list_of_figures, (x, y - 2*Y/8)):
                    list.append((x, y - 2*Y/8))
                list.append((x, y - Y/8))

            if Board.to_capture(self.list_of_figures, (x + X/8, y - Y/8), self.kolor):
                list.append((x + X/8, y - Y/8))
            if Board.to_capture(self.list_of_figures, (x - X/8, y - Y/8), self.kolor):
                list.append((x - X/8, y - Y/8))

            for figura in self.list_of_figures:
                if figura.get_xy() == (x + X/8, y):
                    if type(figura) == Pawn and figura.get_passant() and figura.get_kolor() != self.kolor:
                        list.append((x+X/8,y-Y/8))
            for figura in self.list_of_figures:
                if figura.get_xy() == (x - X/8, y):
                    if type(figura) == Pawn and figura.get_passant() and figura.get_kolor() != self.kolor:
                        list.append((x-X/8,y-Y/8))

        return list
    #wersja dla obracanej planszy
    '''
    def possible_moves(self):

        list = []
        x, y = self.x, self.y

        if not Board.is_occupied(self.list_of_figures, (x, y - Y/8)):
            if self.first_move and not Board.is_occupied(self.list_of_figures, (x, y - 2*Y/8)):
                list.append((x, y - 2*Y/8))
            list.append((x, y - Y/8))

        if Board.to_capture(self.list_of_figures, (x + X/8, y - Y/8), self.kolor):
            list.append((x + X/8, y - Y/8))
        if Board.to_capture(self.list_of_figures, (x - X/8, y - Y/8), self.kolor):
            list.append((x - X/8, y - Y/8))

        for figura in self.list_of_figures:
            if figura.get_xy() == (x + X/8, y):
                if type(figura) == Pawn and figura.get_passant() and figura.get_kolor() != self.kolor:
                    list.append((x+X/8,y-Y/8))
        for figura in self.list_of_figures:
            if figura.get_xy() == (x - X/8, y):
                if type(figura) == Pawn and figura.get_passant() and figura.get_kolor() != self.kolor:
                    list.append((x-X/8,y-Y/8))
                    
        return list
    '''
    def move(self, XY):
        if self.first_move:
            self.passant = True
        self.first_move = False
        
        if XY[0] == self.x + X/8 and XY[1] == self.y + Y/8 and not Board.is_occupied(self.list_of_figures, XY):
            for figura in self.list_of_figures:
                if figura.get_xy() == (XY[0], XY[1]-Y/8):
                    self.list_of_figures.remove(figura)
        if XY[0] == self.x - X/8 and XY[1] == self.y + Y/8 and not Board.is_occupied(self.list_of_figures, XY):
            for figura in self.list_of_figures:
                if figura.get_xy() == (XY[0], XY[1]-Y/8):
                    self.list_of_figures.remove(figura)
        if XY[0] == self.x + X/8 and XY[1] == self.y - Y/8 and not Board.is_occupied(self.list_of_figures, XY):
            for figura in self.list_of_figures:
                if figura.get_xy() == (XY[0], XY[1]+Y/8):
                    self.list_of_figures.remove(figura)
        if XY[0] == self.x - X/8 and XY[1] == self.y - Y/8 and not Board.is_occupied(self.list_of_figures, XY):
            for figura in self.list_of_figures:
                if figura.get_xy() == (XY[0], XY[1]+Y/8):
                    self.list_of_figures.remove(figura)

        super().move(XY)


class Bishop(Piece):
    def __init__(self, x, y, kolor):
        super().__init__(x, y, kolor)


    def draw_piece(self):
        Drawing.draw_bishop(self.kolor, (self.x, self.y))

    
    def possible_moves(self):

        list = []

        x, y = self.x, self.y
        while x > 0 and y > 0:
            x -= X/8
            y -= Y/8
            if Board.to_capture(self.list_of_figures, (x,y), self.kolor):
                list.append((x,y))
                break
            elif Board.is_occupied(self.list_of_figures, (x,y)):
                break
            list.append((x,y))

        x, y = self.x, self.y
        while x > 0 and y < Y - Y/8:
            x -= X/8
            y += Y/8
            if Board.to_capture(self.list_of_figures, (x,y), self.kolor):
                list.append((x,y))
                break
            if Board.is_occupied(self.list_of_figures, (x,y)):
                break
            list.append((x,y))

        x, y = self.x, self.y
        while x < X - X/8 and y > 0:
            x += X/8
            y -= Y/8
            if Board.to_capture(self.list_of_figures, (x,y), self.kolor):
                list.append((x,y))
                break
            if Board.is_occupied(self.list_of_figures, (x,y)):
                break
            list.append((x,y))

        x, y = self.x, self.y
        while x < X - X/8 and y < Y - Y/8:
            x += X/8
            y += Y/8
            if Board.to_capture(self.list_of_figures, (x,y), self.kolor):
                list.append((x,y))
                break
            if Board.is_occupied(self.list_of_figures, (x,y)): 
                break
            list.append((x,y))
        
        return list
        

class Knight(Piece):
    def __init__(self, x, y, kolor):
        super().__init__(x, y, kolor)

    def draw_piece(self):
        Drawing.draw_knight(self.kolor, (self.x, self.y))
        
    def possible_moves(self):

        list = []
        x, y = self.x, self.y

        list_of_position = [(x+X/4,y+Y/8),(x+X/4,y-Y/8),(x-X/4,y+Y/8),(x-X/4,y-Y/8),(x+X/8,y+Y/4),(x+X/8,y-Y/4),(x-X/8,y+Y/4),(x-X/8,y-Y/4)]

        for XY in list_of_position:
            if (not Board.is_occupied(self.list_of_figures, XY) or Board.to_capture(self.list_of_figures, XY, self.kolor)) and XY[0] >= 0 and XY[0] <= X - X/8 and XY[1] >= 0 and XY[1] <= Y - Y/8:
                list.append(XY)
                
        return list


class Rook(Piece):
    def __init__(self, x, y, kolor):
        super().__init__(x, y, kolor)
        self.first_move = True

    def get_first_move(self):
        return self.first_move

    def draw_piece(self):
        Drawing.draw_rook(self.kolor, (self.x, self.y))

    def possible_moves(self):

        list = []

        x, y = self.x, self.y
        while x > 0:
            x -= X/8
            if Board.to_capture(self.list_of_figures, (x,y), self.kolor):
                list.append((x,y))
                break
            elif Board.is_occupied(self.list_of_figures, (x,y)):
                break
            list.append((x,y))

        x, y = self.x, self.y
        while y < Y - Y/8:
            y += Y/8
            if Board.to_capture(self.list_of_figures, (x,y), self.kolor):
                list.append((x,y))
                break
            if Board.is_occupied(self.list_of_figures, (x,y)):
                break
            list.append((x,y))

        x, y = self.x, self.y
        while y > 0:
            y -= Y/8
            if Board.to_capture(self.list_of_figures, (x,y), self.kolor):
                list.append((x,y))
                break
            if Board.is_occupied(self.list_of_figures, (x,y)):
                break
            list.append((x,y))

        x, y = self.x, self.y
        while x < X - X/8:
            x += X/8
            if Board.to_capture(self.list_of_figures, (x,y), self.kolor):
                list.append((x,y))
                break
            if Board.is_occupied(self.list_of_figures, (x,y)): 
                break
            list.append((x,y))
        
        return list

    def move(self, XY):
        super().move(XY)
        self.first_move = False
        

class Queen(Piece):
    def __init__(self, x, y, kolor):
        super().__init__(x, y, kolor)

    def draw_piece(self):
        Drawing.draw_queen(self.kolor, (self.x, self.y))

    def possible_moves(self):

        list = []

        x, y = self.x, self.y
        while x > 0:
            x -= X/8
            if Board.to_capture(self.list_of_figures, (x,y), self.kolor):
                list.append((x,y))
                break
            elif Board.is_occupied(self.list_of_figures, (x,y)):
                break
            list.append((x,y))

        x, y = self.x, self.y
        while y < Y - Y/8:
            y += Y/8
            if Board.to_capture(self.list_of_figures, (x,y), self.kolor):
                list.append((x,y))
                break
            if Board.is_occupied(self.list_of_figures, (x,y)):
                break
            list.append((x,y))

        x, y = self.x, self.y
        while y > 0:
            y -= Y/8
            if Board.to_capture(self.list_of_figures, (x,y), self.kolor):
                list.append((x,y))
                break
            if Board.is_occupied(self.list_of_figures, (x,y)):
                break
            list.append((x,y))

        x, y = self.x, self.y
        while x < X - X/8:
            x += X/8
            if Board.to_capture(self.list_of_figures, (x,y), self.kolor):
                list.append((x,y))
                break
            if Board.is_occupied(self.list_of_figures, (x,y)): 
                break
            list.append((x,y))

        x, y = self.x, self.y
        while x > 0 and y > 0:
            x -= X/8
            y -= Y/8
            if Board.to_capture(self.list_of_figures, (x,y), self.kolor):
                list.append((x,y))
                break
            elif Board.is_occupied(self.list_of_figures, (x,y)):
                break
            list.append((x,y))

        x, y = self.x, self.y
        while x > 0 and y < Y -Y/8:
            x -= X/8
            y += Y/8
            if Board.to_capture(self.list_of_figures, (x,y), self.kolor):
                list.append((x,y))
                break
            if Board.is_occupied(self.list_of_figures, (x,y)):
                break
            list.append((x,y))

        x, y = self.x, self.y
        while x < X- X/8 and y > 0:
            x += X/8
            y -= Y/8
            if Board.to_capture(self.list_of_figures, (x,y), self.kolor):
                list.append((x,y))
                break
            if Board.is_occupied(self.list_of_figures, (x,y)):
                break
            list.append((x,y))

        x, y = self.x, self.y
        while x < X - X/8 and y < Y - Y/8:
            x += X/8
            y += Y/8
            if Board.to_capture(self.list_of_figures, (x,y), self.kolor):
                list.append((x,y))
                break
            if Board.is_occupied(self.list_of_figures, (x,y)): 
                break
            list.append((x,y))
        
        return list


class King(Piece):
    def __init__(self, x, y, kolor):
        super().__init__(x, y, kolor)
        self.first_move = True

    def draw_piece(self):
        Drawing.draw_king(self.kolor, (self.x, self.y))

    def possible_moves(self):
        x, y = self.x, self.y
        
        list = []
        list_of_position = [(x+X/8,y),(x+X/8,y+Y/8),(x+X/8,y-Y/8),(x-X/8,y),(x-X/8,y+Y/8),(x-X/8,y-Y/8),(x,y+Y/8),(x,y-Y/8)]

        for XY in list_of_position:
            if (not Board.is_occupied(self.list_of_figures, XY) or Board.to_capture(self.list_of_figures, XY, self.kolor)) and XY[0] >= 0 and XY[0] <= X - X/8 and XY[1] >= 0 and XY[1] <= Y - Y/8:
                list.append(XY)

        if self.first_move:
            if Board.right_castle(self.list_of_figures, self.kolor):
                list.append((3*X/4,y))
            if Board.left_castle(self.list_of_figures, self.kolor):
                list.append((X/4,y))
                
        return list

    def move(self, XY):
        super().move(XY)
        if self.first_move:
            if XY == (3*X/4,0):
                for figura in self.list_of_figures:
                    if figura.get_xy() == (7*X/8,0):
                        figura.move((5*X/8,0))
            if XY == (3*X/4,7*Y/8):
                for figura in self.list_of_figures:
                    if figura.get_xy() == (7*X/8,7*Y/8):
                        figura.move((5*X/8,7*Y/8))
            if XY == (X/4,0):
                for figura in self.list_of_figures:
                    if figura.get_xy() == (0,0):
                        figura.move((3*X/8,0))
            if XY == (X/4,7*Y/8):
                for figura in self.list_of_figures:
                    if figura.get_xy() == (0,7*Y/8):
                        figura.move((3*X/8,7*Y/8))
        self.first_move = False
