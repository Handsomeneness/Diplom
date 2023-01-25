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

gorilla_image = pygame.image.load(path.join(img_dir, "горилла4.png")).convert()
gorilla = gorilla_image.get_rect()
gorilla.x = random.randrange(50, 650)
gorilla.y = random.randrange(200, 300)
gorilla_image.set_colorkey(WHITE)

elefant_image = pygame.image.load(path.join(img_dir, "слон3.png")).convert()
elefant = elefant_image.get_rect()
elefant.x = random.randrange(150, 550)
elefant.y = random.randrange(250, 350)
elefant_image.set_colorkey(WHITE)

nadpis = pygame.image.load(path.join(img_dir, "Кто ближе2.png")).convert()
nadpis.set_colorkey(BLACK)
nadpis_Rect = nadpis.get_rect()
nadpis_Rect.topleft = (280, 30)

music_image = pygame.image.load(path.join(img_dir, "музыка2.png"))
music_button = music_image.get_rect()
music_button.topleft = (0, 550)
music_image.set_colorkey(BLACK)

background = pygame.image.load(path.join(img_dir, "джунгли2.jpg")).convert()
background_rect = background.get_rect()

pygame.mixer.music.load(path.join(snd_dir, 'Jungle Friends.mp3'))
pygame.mixer.music.set_volume(0.4)

incorrect_sound = pygame.mixer.Sound(path.join(snd_dir, 'звук неправильного ответа.mp3'))
incorrect_sound.set_volume(0.35)

kto_blizhe_sound = pygame.mixer.Sound(path.join(snd_dir,'Кто ближе.mp3'))
kto_blizhe_sound.play()

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
            if gorilla.collidepoint(pos) and gorilla.y > elefant.y:
                print("Получилось")
                pygame.mixer.music.stop()
                kto_blizhe_sound.stop()
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
                import Diplom.Blizhe_Dalshe3

            elif elefant.collidepoint(pos) and elefant.y > gorilla.y:
                print("Получилось")
                pygame.mixer.music.stop()
                kto_blizhe_sound.stop()
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
                import Diplom.Blizhe_Dalshe3
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
                kto_blizhe_sound.stop()
                incorrect_sound.stop()
                kto_blizhe_sound.play()

        if elefant.right > gorilla.left and \
                elefant.left < gorilla.right and \
                elefant.bottom > gorilla.top and \
                elefant.top < gorilla.bottom:
            elefant.x = random.randrange(150, 550)
            elefant.y = random.randrange(250, 350)
            gorilla.x = random.randrange(50, 650)
            gorilla.y = random.randrange(200, 300)



    screen.blit(background, background_rect)

    screen.blit(gorilla_image, gorilla)
    screen.blit(elefant_image, elefant)
    screen.blit(nadpis, nadpis_Rect)
    screen.blit(music_image, music_button)
    screen.blit(question_image, question_button)

    pygame.display.flip()

pygame.quit()
