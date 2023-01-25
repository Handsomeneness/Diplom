import pygame
import random
from os import path

img_dir = path.join(path.dirname(__file__), 'img2')
snd_dir = path.join(path.dirname(__file__), 'snd3')

FPS = 60
WIDTH = 800
HEIGHT = 600

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

cheese_image = pygame.image.load(path.join(img_dir, "сыр.png"))
cheese_image.set_colorkey(WHITE)
salt_cucumbers_image = pygame.image.load(path.join(img_dir, "маринованные огурцы.png")).convert()
salt_cucumbers_image.set_colorkey(WHITE)
sausage_image = pygame.image.load(path.join(img_dir, "колбаса.png")).convert()
sausage_image.set_colorkey(WHITE)
jam_image = pygame.image.load(path.join(img_dir, "варенье.png")).convert()
jam_image.set_colorkey(WHITE)

cucumber_image = pygame.image.load(path.join(img_dir, "огурец2.png"))
cucumber_image.set_colorkey(WHITE)
milk_image = pygame.image.load(path.join(img_dir, "молоко.png")).convert()
milk_image.set_colorkey(WHITE)
meat_image = pygame.image.load(path.join(img_dir, "мясо2.png")).convert()
meat_image.set_colorkey(WHITE)
cherry_image = pygame.image.load(path.join(img_dir, "вишня.png")).convert()
cherry_image.set_colorkey(WHITE)

music_image = pygame.image.load(path.join(img_dir, "музыка2.png"))
music_image.set_colorkey(BLACK)

nadpis = pygame.image.load(path.join(img_dir, "Что_из_чего_приготовлено2.png")).convert()
nadpis.set_colorkey(BLACK)
nadpis_Rect = nadpis.get_rect()
nadpis_Rect.topleft = (280, 10)

background = pygame.image.load(path.join(img_dir, "пикник2.png")).convert()
background_rect = background.get_rect()

cheese = cheese_image.get_rect()
cheese.topleft = (100, 100)
salt_cucumbers = salt_cucumbers_image.get_rect()
salt_cucumbers.topleft = (250, 100)
sausage = sausage_image.get_rect()
sausage.topleft = (400, 100)
jam = jam_image.get_rect()
jam.topleft = (550, 100)
music_button = music_image.get_rect()
music_button.topleft = (0, 550)

x1 = 100
y1 = 400
x2 = 250
y2 = 400
x3 = 400
y3 = 400
x4 = 550
y4 = 400

x1_new = 0
y1_new = 0
x2_new = 0
y2_new = 0
x3_new = 0
y3_new = 0
x4_new = 0
y4_new = 0

cucumber = cucumber_image.get_rect()
cucumber.topleft = (x1, y1)
milk = milk_image.get_rect()
milk.topleft = (x2, y2)
meat = meat_image.get_rect()
meat.topleft = (x3, y3)
cherry = cherry_image.get_rect()
cherry.topleft = (x4, y4)

pygame.mixer.music.load(path.join(snd_dir, 'forest.mp3'))
pygame.mixer.music.set_volume(0.4)


pygame.display.set_caption('Что из чего приготовлено')

chto_iz_chego_prigotovleno_sound = pygame.mixer.Sound(path.join(snd_dir,'Что из чего приготовлено.mp3'))
chto_iz_chego_prigotovleno_sound.play()

question_image = pygame.image.load(path.join(img_dir,'вопрос2.png')).convert()
question_button = question_image.get_rect()
question_button.topleft = (750,550)
question_image.set_colorkey(BLACK)


pygame.mixer.music.play(loops=-1)

incorrect_sound = pygame.mixer.Sound(path.join(snd_dir, 'звук неправильного ответа.mp3'))
incorrect_sound.set_volume(0.35)

running = True
moving1 = False
moving2 = False
moving3 = False
moving4 = False
flPause = False

while running:
    clock.tick(FPS)
    screen.blit(background, background_rect)
    milk_rect = pygame.draw.rect(screen, BLACK, (100, 225, 103, 103), 2)
    cucumber_rect = pygame.draw.rect(screen, BLACK, (250, 225, 103, 103), 2)
    meat_rect = pygame.draw.rect(screen, BLACK, (400, 225, 103, 103), 2)
    cherry_rect = pygame.draw.rect(screen, BLACK, (550, 225, 103, 103), 2)

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            running = False

        if cucumber.x == 252 and cucumber.y == 227 and milk.x == 102 and milk.y == 227 and meat.x == 402 and meat.y == 227 and cherry.x == 552 and cherry.y == 227:
            print("Получилось")
            pygame.mixer.music.stop()
            chto_iz_chego_prigotovleno_sound.stop()
            sc = pygame.display.set_mode((500, 300))
            clock = pygame.time.Clock()
            start_time = pygame.time.get_ticks()
            f = pygame.font.Font(None, 100)

            molodec_image = pygame.image.load(path.join(img_dir, "Смайлик2.png"))
            molodec = molodec_image.get_rect()
            molodec.topleft = (150, 50)
            molodec_sound = pygame.mixer.Sound(path.join(snd_dir, 'Молодец.mp3'))
            molodec_sound.play()

            sc.blit(molodec_image, molodec)
            r = True
            while r == True:
                sc.fill((255, 255, 255))
                for i in pygame.event.get():
                    if i.type == pygame.QUIT:
                        exit()

                clock.tick(FPS)

                if start_time and pygame.time.get_ticks() - start_time > 2000:
                    r = False
                sc.blit(molodec_image, molodec)
                pygame.display.update()
            import Diplom.Main_Menu2


        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if cucumber.x < event.pos[0] < cucumber.x + 100 and cucumber.y < event.pos[1] < cucumber.y + 100:
                 moving1 = True
            elif milk.x < event.pos[0] < milk.x + 100 and milk.y < event.pos[1] < milk.y + 100:
                moving2 = True
            elif meat.x < event.pos[0] < meat.x + 100 and meat.y < event.pos[1] < meat.y + 100:
                moving3 = True
            elif cherry.x < event.pos[0] < cherry.x + 100 and cherry.y < event.pos[1] < cherry.y + 100:
                moving4 = True

            if music_button.collidepoint(pos):
                flPause = not flPause
                if flPause:
                    pygame.mixer.music.pause()
                else:
                     pygame.mixer.music.unpause()

            if question_button.collidepoint(pos):
                chto_iz_chego_prigotovleno_sound.stop()
                incorrect_sound.stop()
                chto_iz_chego_prigotovleno_sound.play()

        if event.type == pygame.MOUSEMOTION:
            if moving1:
                x1_new, y1_new = event.rel
                cucumber.x, cucumber.y = cucumber.x + x1_new, cucumber.y + y1_new
                if cucumber.centerx == cucumber_rect.centerx:
                    cucumber.x = 252
                    cucumber.y = 227
                    moving1 = False
            elif moving2:
                x2_new, y2_new = event.rel
                milk.x, milk.y = milk.x + x2_new, milk.y + y2_new
                if milk.centerx == milk_rect.centerx:
                    milk.x = 102
                    milk.y = 227
                    moving2 = False
            elif moving3:
                x3_new, y3_new = event.rel
                meat.x, meat.y = meat.x + x3_new, meat.y + y3_new
                if meat.centery == meat_rect.centery:
                    meat.x = 402
                    meat.y = 227
                    moving3 = False
            elif moving4:
                x4_new, y4_new = event.rel
                cherry.x, cherry.y = cherry.x + x4_new, cherry.y + y4_new
                if cherry.centery == cherry_rect.centery:
                    cherry.x = 552
                    cherry.y = 227
                    moving4 = False


        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if cucumber.x != 252 and cucumber.y != 227:
                cucumber.x = 100
                cucumber.y = 400
            if milk.x != 102 and milk.y != 227:
                milk.x = 250
                milk.y = 400
            if meat.x != 402 and meat.y != 227:
                meat.x = 400
                meat.y = 400
            if cherry.x != 552 and cherry.y != 227:
                cherry.x = 550
                cherry.y = 400

            moving1 = False
            moving2 = False
            moving3 = False
            moving4 = False





    screen.blit(cheese_image, cheese)
    screen.blit(salt_cucumbers_image, salt_cucumbers)
    screen.blit(sausage_image, sausage)
    screen.blit(jam_image, jam)
    screen.blit(cucumber_image, cucumber)
    screen.blit(milk_image, milk)
    screen.blit(meat_image, meat)
    screen.blit(cherry_image, cherry)
    screen.blit(music_image, music_button)
    screen.blit(nadpis, nadpis_Rect)
    screen.blit(question_image, question_button)

    pygame.display.flip()
    screen.fill(WHITE)



pygame.quit()
