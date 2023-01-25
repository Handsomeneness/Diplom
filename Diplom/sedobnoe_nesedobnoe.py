import pygame
from os import path

img_dir = path.join(path.dirname(__file__), 'img5')
snd_dir = path.join(path.dirname(__file__), 'snd4')

pygame.display.set_caption('Съедобное-несъедобное')

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

ananas_image = pygame.image.load(path.join(img_dir, 'ананас.png'))
ananas = ananas_image.get_rect()
ananas.topleft = (125, 200)

gitara_image = pygame.image.load(path.join(img_dir, 'гитара.png'))
gitara = gitara_image.get_rect()
gitara.topleft = (545, 205)

music_image = pygame.image.load(path.join(img_dir, "музыка2.png"))
music_button = music_image.get_rect()
music_button.topleft = (0, 525)
music_image.set_colorkey(BLACK)

background = pygame.image.load(path.join(img_dir, "3.png")).convert()
background_rect = background.get_rect()

pygame.mixer.music.load(path.join(snd_dir, 'Autumn Forest.mp3'))
pygame.mixer.music.set_volume(0.4)

pygame.mixer.music.play()

sedobnoe_nesedobnoe_sound = pygame.mixer.Sound(path.join(snd_dir,'Что нельзя скушать.mp3'))
sedobnoe_nesedobnoe_sound.play()

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

            if gitara.collidepoint(pos):
                print("Получилось")
                pygame.mixer.music.stop()
                sedobnoe_nesedobnoe_sound.stop()
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
                import Diplom.Main_Menu8

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
                sedobnoe_nesedobnoe_sound.stop()
                incorrect_sound.stop()
                sedobnoe_nesedobnoe_sound.play()

    screen.blit(background, background_rect)

    screen.blit(ananas_image, ananas)
    screen.blit(gitara_image, gitara)
    screen.blit(music_image, music_button)
    screen.blit(question_image, question_button)

    pygame.display.flip()

pygame.quit()
