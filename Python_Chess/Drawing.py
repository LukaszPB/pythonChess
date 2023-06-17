import pygame, os

X, Y = 720, 600
BLACK = (0,0,0)
RED = (255,0,0)

SCREEN = pygame.display.set_mode((X,Y))

BOARD = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Chessboard.png")), (X,Y))

W_PAWN = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "wP.png")), (X/8,Y/8))
B_PAWN = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "bP.png")), (X/8,Y/8))
W_BISHOP = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "wB.png")), (X/8,Y/8))
B_BISHOP = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "bB.png")), (X/8,Y/8))
W_KNIGHT = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "wN.png")), (X/8,Y/8))
B_KNIGHT = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "bN.png")), (X/8,Y/8))
W_ROOK = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "wR.png")), (X/8,Y/8))
B_ROOK = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "bR.png")), (X/8,Y/8))
W_QUEEN = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "wQ.png")), (X/8,Y/8))
B_QUEEN = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "bQ.png")), (X/8,Y/8))
W_KING = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "wK.png")), (X/8,Y/8))
B_KING = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "bK.png")), (X/8,Y/8))

pygame.font.init()
FONT = pygame.font.SysFont("comicsans",75)

pygame.init()

def draw_pawn(Kolor, XY):
    if Kolor == "W":
        SCREEN.blit(W_PAWN, XY)
    if Kolor == "B":
        SCREEN.blit(B_PAWN, XY)

def draw_bishop(Kolor, XY):
    if Kolor == "W":
        SCREEN.blit(W_BISHOP, XY)
    if Kolor == "B":
        SCREEN.blit(B_BISHOP, XY)

def draw_knight(Kolor, XY):
    if Kolor == "W":
        SCREEN.blit(W_KNIGHT, XY)
    if Kolor == "B":
        SCREEN.blit(B_KNIGHT, XY)

def draw_rook(Kolor, XY):
    if Kolor == "W":
        SCREEN.blit(W_ROOK, XY)
    if Kolor == "B":
        SCREEN.blit(B_ROOK, XY)

def draw_queen(Kolor, XY):
    if Kolor == "W":
        SCREEN.blit(W_QUEEN, XY)
    if Kolor == "B":
        SCREEN.blit(B_QUEEN, XY)

def draw_king(Kolor, XY):
    if Kolor == "W":
        SCREEN.blit(W_KING, XY)
    if Kolor == "B":
        SCREEN.blit(B_KING, XY)

def draw(list):
    SCREEN.blit(BOARD, (0,0))
    
    for element in list:
        element.draw_piece()
    pygame.display.update()

def draw_moves(XY):
    pygame.draw.circle(SCREEN, BLACK, (XY[0] + X/16, XY[1] + Y/16),X/90)
    pygame.display.update()

def draw_captures(XY):
    pygame.draw.circle(SCREEN, BLACK, (XY[0] + X/16, XY[1] + Y/16),int(X/16),int(X/180))
    pygame.display.update()
def draw_check(XY):
    pygame.draw.rect(SCREEN, RED, (XY[0], XY[1], X/8, Y/8),3)
    pygame.display.update()
def draw_draw():
    napis = FONT.render("Draw",False,RED)
    SCREEN.blit(napis, (3*X/8, 3*Y/8))
    pygame.display.update()
    pygame.time.delay(3000)

#wersja dla obracanej planszy

def draw_win(kolor):
    if kolor == "B":
        napis = FONT.render("White Win",False,RED)
    else:
        napis = FONT.render("Black Win",False,RED)

    SCREEN.blit(napis, (X/4, 3*Y/8))
    pygame.display.update()
    pygame.time.delay(3000)
