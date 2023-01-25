import pygame
import random
from os import path

img_dir = path.join(path.dirname(__file__), 'img3')
snd_dir = path.join(path.dirname(__file__), 'snd3')

pygame.display.set_caption('Ближе-дальше')

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

corsack_image = pygame.image.load(path.join(img_dir, "корсак3.png")).convert()
corsack = corsack_image.get_rect()
corsack.x = random.randrange(50, 600)
corsack.y = random.randrange(375, 400)
corsack_image.set_colorkey(WHITE)

lion_image = pygame.image.load(path.join(img_dir, "лев4.png")).convert()
lion = lion_image.get_rect()
lion.x = random.randrange(50, 600)
lion.y = random.randrange(450, 500)
lion_image.set_colorkey(WHITE)

nadpis = pygame.image.load(path.join(img_dir, "Кто дальше2.png")).convert()
nadpis.set_colorkey(BLACK)
nadpis_Rect = nadpis.get_rect()
nadpis_Rect.topleft = (280, 30)

music_image = pygame.image.load(path.join(img_dir, "музыка2.png"))
music_button = music_image.get_rect()
music_button.topleft = (0, 550)
music_image.set_colorkey(BLACK)

background = pygame.image.load(path.join(img_dir, "пустыня2.jpg")).convert()
background_rect = background.get_rect()

pygame.mixer.music.load(path.join(snd_dir, 'Desert.mp3'))
pygame.mixer.music.set_volume(0.4)

incorrect_sound = pygame.mixer.Sound(path.join(snd_dir, 'звук неправильного ответа.mp3'))
incorrect_sound.set_volume(0.35)

kto_dalshe_sound = pygame.mixer.Sound(path.join(snd_dir,'Кто дальше.mp3'))
kto_dalshe_sound.play()

question_image = pygame.image.load(path.join(img_dir,'вопрос2.png')).convert()
question_button = question_image.get_rect()
question_button.topleft = (750,550)
question_image.set_colorkey(BLACK)

pygame.mixer.music.play()

pygame.mixer.music.play(loops=-1)

running = True
flPause = False
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if corsack.collidepoint(pos) and corsack.y < lion.y:
                print("Получилось")
                pygame.mixer.music.stop()
                kto_dalshe_sound.stop()
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
                running = False
                import Diplom.Main_Menu
            elif lion.collidepoint(pos) and lion.y < corsack.y:
                print("Получилось")
                pygame.mixer.music.stop()
                kto_dalshe_sound.stop()
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
                running = False
                import Diplom.Main_Menu
            else:
                incorrect_sound.play()
            if music_button.collidepoint(pos):
                incorrect_sound.stop()
                flPause = not flPause
                if flPause:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()

            if question_button.collidepoint(pos):
                kto_dalshe_sound.stop()
                incorrect_sound.stop()
                kto_dalshe_sound.play()

        if lion.right > corsack.left and \
                lion.left < corsack.right and \
                lion.bottom > corsack.top and \
                lion.top < corsack.bottom:
            lion.x = random.randrange(50, 600)
            lion.y = random.randrange(375, 400)
            corsack.x = random.randrange(50, 600)
            corsack.y = random.randrange(450, 500)

    screen.blit(background, background_rect)

    screen.blit(corsack_image, corsack)
    screen.blit(lion_image, lion)
    screen.blit(nadpis, nadpis_Rect)
    screen.blit(music_image, music_button)
    screen.blit(question_image, question_button)

    pygame.display.flip()

pygame.quit()
