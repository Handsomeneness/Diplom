import pygame
from os import path

img_dir = path.join(path.dirname(__file__), 'img9')

pygame.display.set_caption('Главное меню')

FPS = 60
WIDTH = 800
HEIGHT = 800

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

Blizhe_Dalshe = pygame.image.load(path.join(img_dir, "Ближе-Дальше.jpg")).convert()
Blizhe_Dalshe_Rect = Blizhe_Dalshe.get_rect()
Blizhe_Dalshe_Rect.topleft = (50, 50)

Chto_iz_chego_prigotovleno = pygame.image.load(path.join(img_dir, "Что_из_чего_приготовлено.jpg")).convert()
Chto_iz_chego_prigotovleno_Rect = Chto_iz_chego_prigotovleno.get_rect()
Chto_iz_chego_prigotovleno_Rect.topleft = (300, 50)

Kto_izdal_zvuk = pygame.image.load(path.join(img_dir, "Кто_издал_звук.jpg")).convert()
Kto_izdal_zvuk_Rect = Kto_izdal_zvuk.get_rect()
Kto_izdal_zvuk_Rect.topleft = (550, 50)

Naidy_lishnee = pygame.image.load(path.join(img_dir, "Найди_лишнее.jpg")).convert()
Naidy_lishnee_Rect = Naidy_lishnee.get_rect()
Naidy_lishnee_Rect.topleft = (50, 300)

Pazl_vorobei = pygame.image.load(path.join(img_dir, "Пазл.jpg")).convert()
Pazl_vorobei_Rect = Pazl_vorobei.get_rect()
Pazl_vorobei_Rect.topleft = (300, 300)

Raspredeli_po_kategoriam = pygame.image.load(path.join(img_dir, "Распредели_по_категориям.jpg")).convert()
Raspredeli_po_kategoriam_Rect = Raspredeli_po_kategoriam.get_rect()
Raspredeli_po_kategoriam_Rect.topleft = (550, 300)

SPACEWAR = pygame.image.load(path.join(img_dir, "Космовойны.jpg")).convert()
SPACEWAR_Rect = SPACEWAR.get_rect()
SPACEWAR_Rect.topleft = (50, 550)

Vishe_nisze = pygame.image.load(path.join(img_dir, "Выше-ниже.jpg")).convert()
Vishe_nisze_Rect = Vishe_nisze.get_rect()
Vishe_nisze_Rect.topleft = (300, 550)



running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if Blizhe_Dalshe_Rect.collidepoint(pos):
                import Diplom.Blizhe_Dalshe
            elif Chto_iz_chego_prigotovleno_Rect.collidepoint(pos):
                import Diplom.Chto_iz_chego_prigotovleno
            elif Kto_izdal_zvuk_Rect.collidepoint(pos):
                import Diplom.Kto_izdal_zvuk
            elif Naidy_lishnee_Rect.collidepoint(pos):
                import Diplom.Naidy_lishnee
            elif Pazl_vorobei_Rect.collidepoint(pos):
                import Diplom.pazl_vorobei
            elif Raspredeli_po_kategoriam_Rect.collidepoint(pos):
                import Diplom.Raspredeli_po_kategoriam
            elif SPACEWAR_Rect.collidepoint(pos):
                import Diplom.SPACEWAR
            elif Vishe_nisze_Rect.collidepoint(pos):
                import Diplom.vishe_nisze



    screen.fill(WHITE)
    screen.blit(Blizhe_Dalshe, Blizhe_Dalshe_Rect)
    screen.blit(Chto_iz_chego_prigotovleno, Chto_iz_chego_prigotovleno_Rect)
    screen.blit(Kto_izdal_zvuk, Kto_izdal_zvuk_Rect)
    screen.blit(Naidy_lishnee, Naidy_lishnee_Rect)
    screen.blit(Pazl_vorobei, Pazl_vorobei_Rect)
    screen.blit(Raspredeli_po_kategoriam, Raspredeli_po_kategoriam_Rect)
    screen.blit(SPACEWAR, SPACEWAR_Rect)
    screen.blit(Vishe_nisze, Vishe_nisze_Rect)

    pygame.display.flip()

pygame.quit()