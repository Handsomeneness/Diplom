import pygame
from os import path

img_dir = path.join(path.dirname(__file__), 'img7')
snd_dir = path.join(path.dirname(__file__), 'snd6')

pygame.display.set_caption('Найди лишнее')

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

rooster_image = pygame.image.load(path.join(img_dir, "петух2.png")).convert()
rooster = rooster_image.get_rect()
rooster_image.set_colorkey(BLACK)
rooster.topleft = (10, 200)

turkey_image = pygame.image.load(path.join(img_dir, "индюк2.png")).convert()
turkey = turkey_image.get_rect()
turkey_image.set_colorkey(WHITE)
turkey.topleft = (210, 220)

gus_image = pygame.image.load(path.join(img_dir, "гусь2.png")).convert()
gus = gus_image.get_rect()
gus_image.set_colorkey(WHITE)
gus.topleft = (425, 190)

starling_image = pygame.image.load(path.join(img_dir, "скворец2.png")).convert()
starling = starling_image.get_rect()
starling_image.set_colorkey(WHITE)
starling.topleft = (590, 230)

music_image = pygame.image.load(path.join(img_dir, "музыка2.png"))
music_button = music_image.get_rect()
music_button.topleft = (0, 550)
music_image.set_colorkey(BLACK)

background = pygame.image.load(path.join(img_dir, "фон2.jpg")).convert()
background_rect = background.get_rect()

pygame.mixer.music.load(path.join(snd_dir, 'Autumn Forest.mp3'))
pygame.mixer.music.set_volume(0.4)

pygame.mixer.music.play()

naidy_lishnee2_sound = pygame.mixer.Sound(path.join(snd_dir,'Найди лишнее.mp3'))
naidy_lishnee2_sound.play()

question_image = pygame.image.load(path.join(img_dir,'вопрос2.png')).convert()
question_button = question_image.get_rect()
question_button.topleft = (750,550)
question_image.set_colorkey(BLACK)

pygame.mixer.music.play(loops=-1)

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
            if starling.collidepoint(pos):
                print("Получилось")
                pygame.mixer.music.stop()
                naidy_lishnee2_sound.stop()
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
                import Diplom.Main_Menu4
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
                naidy_lishnee2_sound.stop()
                incorrect_sound.stop()
                naidy_lishnee2_sound.play()

    screen.blit(background, background_rect)

    screen.blit(rooster_image, rooster)
    screen.blit(turkey_image, turkey)
    screen.blit(gus_image, gus)
    screen.blit(starling_image, starling)

    screen.blit(music_image, music_button)
    screen.blit(question_image, question_button)

    pygame.display.flip()

pygame.quit()