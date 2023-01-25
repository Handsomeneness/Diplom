import pygame
from os import path

img_dir = path.join(path.dirname(__file__), 'img5')
snd_dir = path.join(path.dirname(__file__), 'snd4')

pygame.display.set_caption('Шире-уже')

FPS = 60
WIDTH = 900
HEIGHT = 575

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

shar_image = pygame.image.load(path.join(img_dir, 'шар.png'))
shar = shar_image.get_rect()
shar.topleft = (82, 176)

spiral_image = pygame.image.load(path.join(img_dir, 'спираль.png'))
spiral = spiral_image.get_rect()
spiral.topleft = (635, 182)

music_image = pygame.image.load(path.join(img_dir, "музыка2.png"))
music_button = music_image.get_rect()
music_button.topleft = (0, 525)
music_image.set_colorkey(BLACK)

background = pygame.image.load(path.join(img_dir, "2.png")).convert()
background_rect = background.get_rect()

pygame.mixer.music.load(path.join(snd_dir, 'Autumn Forest.mp3'))
pygame.mixer.music.set_volume(0.4)

pygame.mixer.music.play()

shire_uzhe_sound = pygame.mixer.Sound(path.join(snd_dir,'Что шире.mp3'))
shire_uzhe_sound.play()

question_image = pygame.image.load(path.join(img_dir,'вопрос2.png')).convert()
question_button = question_image.get_rect()
question_button.topleft = (850,525)
question_image.set_colorkey(BLACK)

incorrect_sound = pygame.mixer.Sound(path.join(snd_dir, 'звук неправильного ответа.mp3'))
incorrect_sound.set_volume(0.35)

running = True
flPause = False
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            if shar.collidepoint(pos):
                print("Получилось")
                pygame.mixer.music.stop()
                shire_uzhe_sound.stop()
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
                import Diplom.sedobnoe_nesedobnoe

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
                shire_uzhe_sound.stop()
                incorrect_sound.stop()
                shire_uzhe_sound.play()

    screen.blit(background, background_rect)

    screen.blit(shar_image, shar)
    screen.blit(spiral_image, spiral)
    screen.blit(music_image, music_button)
    screen.blit(question_image, question_button)

    pygame.display.flip()

pygame.quit()
