import pygame
import random
from os import path

img_dir = path.join(path.dirname(__file__), 'img4')
snd_dir = path.join(path.dirname(__file__), 'snd2')

pygame.display.set_caption('Кто издал звук')

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
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

goat_image = pygame.image.load(path.join(img_dir, 'коза2.png')).convert()
cow_image = pygame.image.load(path.join(img_dir, 'корова2.png')).convert()
cat_image = pygame.image.load(path.join(img_dir, 'кот.png')).convert()
rooster_image = pygame.image.load(path.join(img_dir, 'петух2.png')).convert()
pig_image = pygame.image.load(path.join(img_dir, 'свинья.png')).convert()
dog_image = pygame.image.load(path.join(img_dir, 'собака.png')).convert()

goat_image.set_colorkey(WHITE)
cow_image.set_colorkey(WHITE)
cat_image.set_colorkey(WHITE)
rooster_image.set_colorkey(WHITE)
pig_image.set_colorkey(WHITE)
dog_image.set_colorkey(WHITE)

background_image = pygame.image.load(path.join(img_dir, 'ферма2.jpg'))
background = background_image.get_rect()

goat = goat_image.get_rect()
goat.topleft = (200,275)
cow = cow_image.get_rect()
cow.topleft = (500,325)
cat = cat_image.get_rect()
cat.topleft = (0,200)
rooster = rooster_image.get_rect()
rooster.topleft = (200,80)
pig = pig_image.get_rect()
pig.topleft = (150,450)
dog = dog_image.get_rect()
dog.topleft = (675,450)


music_image = pygame.image.load(path.join(img_dir, "музыка2.png"))
music_button = music_image.get_rect()
music_button.topleft = (0, 550)
music_image.set_colorkey(BLACK)

pygame.mixer.music.load(path.join(snd_dir, 'Farm.ogg'))
pygame.mixer.music.set_volume(0.4)

pygame.mixer.music.play()

goat_sound = pygame.mixer.Sound(path.join(snd_dir, 'Коза.mp3'))
cow_sound = pygame.mixer.Sound(path.join(snd_dir, 'Корова.mp3'))
cat_sound = pygame.mixer.Sound(path.join(snd_dir, 'Кот.mp3'))
rooster_sound = pygame.mixer.Sound(path.join(snd_dir, 'Петух.mp3'))
pig_sound = pygame.mixer.Sound(path.join(snd_dir, 'Свинья.mp3'))
dog_sound = pygame.mixer.Sound(path.join(snd_dir, 'Собака.mp3'))
random_sound = 0

kto_izdal_zvuk_sound = pygame.mixer.Sound(path.join(snd_dir,'Кто издал звук.mp3'))
kto_izdal_zvuk_sound.play()

question_image = pygame.image.load(path.join(img_dir,'вопрос2.png')).convert()
question_button = question_image.get_rect()
question_button.topleft = (750,550)
question_image.set_colorkey(BLACK)

nazmi_image = pygame.image.load(path.join(img_dir, 'Нажми2.png')).convert()
nazmi_button = nazmi_image.get_rect()
nazmi_button.topleft = (325, 400)
nazmi_image.set_colorkey(BLACK)

incorrect_sound = pygame.mixer.Sound(path.join(snd_dir, 'звук неправильного ответа.mp3'))
incorrect_sound.set_volume(0.35)

running = True
flPause = False
while running:
    global button
    clock.tick(FPS)

    screen = pygame.display.set_mode((WIDTH, HEIGHT))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.mixer.music.stop()
            pygame.mixer.stop()
            running = False
            import Diplom.Main_Menu3

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            if nazmi_button.collidepoint(pos):
                pygame.mixer.stop()
                animal_sounds = [goat_sound, cow_sound, cat_sound, rooster_sound, pig_sound, dog_sound]
                random_sound = random.choice(animal_sounds)
                random_sound.play()

            if goat.collidepoint(pos) and random_sound == goat_sound:
                print("Получилось")
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
            if cow.collidepoint(pos) and random_sound == cow_sound:
                print("Получилось")
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
            if cat.collidepoint(pos) and random_sound == cat_sound:
                print("Получилось")
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
            if rooster.collidepoint(pos) and random_sound == rooster_sound:
                print("Получилось")
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
            if pig.collidepoint(pos) and random_sound == pig_sound:
                print("Получилось")
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
            if dog.collidepoint(pos) and random_sound == dog_sound:
                print("Получилось")
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



            if music_button.collidepoint(pos):
                flPause = not flPause
                if flPause:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()

            if question_button.collidepoint(pos):
                kto_izdal_zvuk_sound.stop()
                incorrect_sound.stop()
                kto_izdal_zvuk_sound.play()



    screen.blit(background_image, background)
    screen.blit(goat_image, goat)
    screen.blit(cow_image, cow)
    screen.blit(cat_image, cat)
    screen.blit(rooster_image, rooster)
    screen.blit(pig_image, pig)
    screen.blit(dog_image, dog)
    screen.blit(music_image, music_button)
    screen.blit(question_image, question_button)
    screen.blit(nazmi_image, nazmi_button)






    pygame.display.flip()
    screen.fill(WHITE)
pygame.quit()
