import pygame
import random
from os import path

img_dir = path.join(path.dirname(__file__), 'img6')
snd_dir = path.join(path.dirname(__file__), 'snd5')

pygame.display.set_caption('Пазл-воробей')

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

x1 = 600
y1 = 20
x2 = 600
y2 = 220
x3 = 600
y3 = 420
x4 = 600
y4 = 620

x1_new = 0
y1_new = 0
x2_new = 0
y2_new = 0
x3_new = 0
y3_new = 0
x4_new = 0
y4_new = 0

first_image = pygame.image.load(path.join(img_dir, '1.1.jpg')).convert()
first = first_image.get_rect()
first.topleft = (x1, y1)
second_image = pygame.image.load(path.join(img_dir, '2.2.jpg')).convert()
second = second_image.get_rect()
second.topleft = (x2, y2)
third_image = pygame.image.load(path.join(img_dir, '3.3.jpg')).convert()
third = third_image.get_rect()
third.topleft = (x3, y3)
fourth_image = pygame.image.load(path.join(img_dir, '4.4.jpg')).convert()
fourth = fourth_image.get_rect()
fourth.topleft = (x4, y4)

music_image = pygame.image.load(path.join(img_dir, "музыка2.png"))
music_button = music_image.get_rect()
music_button.topleft = (0, 750)
music_image.set_colorkey(BLACK)

background = pygame.image.load(path.join(img_dir, "фон4.jpg")).convert()
background_rect = background.get_rect()

pygame.mixer.music.load(path.join(snd_dir, 'Autumn Forest.mp3'))
pygame.mixer.music.set_volume(0.4)

pygame.mixer.music.play()

pazl_vorobei_sound = pygame.mixer.Sound(path.join(snd_dir,'Собери пазл.mp3'))
pazl_vorobei_sound.play()

question_image = pygame.image.load(path.join(img_dir,'вопрос2.png')).convert()
question_button = question_image.get_rect()
question_button.topleft = (525,750)
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
    first_rect = pygame.draw.rect(screen, BLACK, (100, 100, 175, 166), 1)
    second_rect = pygame.draw.rect(screen, BLACK, (275, 100, 175, 166), 1)
    third_rect = pygame.draw.rect(screen, BLACK, (100, 266, 175, 166), 1)
    fourth_rect = pygame.draw.rect(screen, BLACK, (275, 266, 175, 166), 1)

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            running = False

        if first.x == 100 and first.y == 100 and second.x == 275 and second.y == 100 and third.x == 100 and third.y == 266 and fourth.x == 275 and fourth.y == 266:
            print("Получилось")
            pygame.mixer.music.stop()
            pazl_vorobei_sound.stop()
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
            import Diplom.Main_Menu5

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if first.x < event.pos[0] < first.x + 175 and first.y < event.pos[1] < first.y + 175:
                moving1 = True
            elif second.x < event.pos[0] < second.x + 175 and second.y < event.pos[1] < second.y + 175:
                moving2 = True
            elif third.x < event.pos[0] < third.x + 175 and third.y < event.pos[1] < third.y + 175:
                moving3 = True
            elif fourth.x < event.pos[0] < fourth.x + 175 and fourth.y < event.pos[1] < fourth.y + 175:
                moving4 = True

            if music_button.collidepoint(pos):
                flPause = not flPause
                if flPause:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()

            if question_button.collidepoint(pos):
                pazl_vorobei_sound.stop()
                incorrect_sound.stop()
                pazl_vorobei_sound.play()

        if event.type == pygame.MOUSEMOTION:
            if moving1:
                x1_new, y1_new = event.rel
                first.x, first.y = first.x + x1_new, first.y + y1_new
                if first.centerx == first_rect.centerx:
                    first.x = 100
                    first.y = 100
                    moving1 = False

            elif moving2:
                x2_new, y2_new = event.rel
                second.x, second.y = second.x + x2_new, second.y + y2_new
                if second.centerx == second_rect.centerx:
                    second.x = 275
                    second.y = 100
                    moving2 = False
            elif moving3:
                x3_new, y3_new = event.rel
                third.x, third.y = third.x + x3_new, third.y + y3_new
                if third.centerx == third_rect.centerx:
                    third.x = 100
                    third.y = 266
                    moving3 = False
            elif moving4:
                x4_new, y4_new = event.rel
                fourth.x, fourth.y = fourth.x + x4_new, fourth.y + y4_new
                if fourth.centerx == fourth_rect.centerx:
                    fourth.x = 275
                    fourth.y = 266
                    moving4 = False

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if first.x != 100 and first.y != 100:
                first.x = 600
                first.y = 20
            if second.x != 275 and second.y != 100:
                second.x = 600
                second.y = 220
            if third.x != 100 and third.y != 266:
                third.x = 600
                third.y = 420
            if fourth.x != 275 and fourth.y != 266:
                fourth.x = 600
                fourth.y = 620

            moving1 = False
            moving2 = False
            moving3 = False
            moving4 = False

    screen.blit(first_image, first)
    screen.blit(second_image, second)
    screen.blit(third_image, third)
    screen.blit(fourth_image, fourth)
    screen.blit(music_image, music_button)
    screen.blit(question_image, question_button)

    pygame.display.flip()
    screen.fill(WHITE)

pygame.quit()
