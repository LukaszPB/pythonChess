import Drawing, Board, Pieces
import pygame, sys

Y = Drawing.Y

def main():
    clock = pygame.time.Clock()

    list_of_figures = Pieces.Piece.list_of_figures
    list_of_figures = Board.start(list_of_figures)

    Drawing.draw(list_of_figures)
    
    list_of_possible_moves = []
    round = "W"
    selected = False
    x = False
    
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:

                click = Board.pole(pygame.mouse.get_pos())

                for figura in list_of_figures:
                    if figura.was_selected(click) and figura.get_kolor() == round:
                        Drawing.draw(list_of_figures)

                        list_of_possible_moves = figura.possible_moves()

                        #Usunięcie nielegalnych ruchów po szachu
                        test_moves = []
                        for move in list_of_possible_moves:
                            test_moves.append(move)
                        
                        for move in test_moves:

                            pozycja = figura.get_xy()
                            test_list = []
                            for piece in list_of_figures:
                                test_list.append(piece)

                            for piece in test_list:
                                if piece.get_xy() == move:
                                    test_list.remove(piece)
                            figura.fake_move(move)

                            if Board.check(test_list,round):
                                list_of_possible_moves.remove(move)
                            
                            figura.fake_move(pozycja)
                        #koniec
                            
                        select_figur = figura
                        selected = True

                        XY = figura.get_xy()
                            
                        for XY in list_of_possible_moves:
                            if Board.to_capture(list_of_figures, XY, figura.kolor): Drawing.draw_captures(XY)
                            else: Drawing.draw_moves(XY)
                    
                if selected and list_of_possible_moves.count(click) > 0:

                    select_figur.move(click)

                    for figura in list_of_figures:
                        if figura.get_xy() == click and figura != select_figur:
                            list_of_figures.remove(figura)
                    
                    XY = select_figur.get_xy()

                    if type(select_figur) == Pieces.Pawn and (XY[1] == 0 or XY[1] == 7*Y/8):
                        list_of_figures.append(Pieces.Queen(XY[0],XY[1],select_figur.get_kolor()))
                        list_of_figures.remove(select_figur)

                    if x:
                        passant.set_passant()
                        x = False
                    if type(select_figur) == Pieces.Pawn and select_figur.get_passant():
                        x = True
                        passant = select_figur

                    Drawing.draw(list_of_figures)

                    if round == "W":
                        round = "B"
                    else: 
                        round = "W"

                    #Sprawdzić czy jest szach
                    if Board.check(list_of_figures,round):
                        Drawing.draw_check(Board.king_pointer(list_of_figures,round).get_xy())
                        
                    #Sprawdzić czy gra dobiegła końca
                    if Board.draw(list_of_figures,round):
                        if Board.check(list_of_figures,round):
                            Drawing.draw_win(round)
                            main()
                        else:
                            Drawing.draw_draw()
                            main()
                   
                    selected = False

                    #wersja dla obracanej planszy
                    '''
                    Board.turn(list_of_figures)
                    pygame.time.delay(100)
                    '''
                

if __name__ == "__main__":
    main()