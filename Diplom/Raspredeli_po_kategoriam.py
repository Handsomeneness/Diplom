import pygame
from os import path

img_dir = path.join(path.dirname(__file__), 'img8')
snd_dir = path.join(path.dirname(__file__), 'snd7')

pygame.display.set_caption('Распредели по категориям')

FPS = 60
WIDTH = 1100
HEIGHT = 900

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

glass_arrow_image = pygame.image.load(path.join(img_dir, 'стекло.jpg')).convert()
glass_arrow = glass_arrow_image.get_rect()
glass_arrow.topleft = (20, 50)
glass_arrow_image.set_colorkey(WHITE)

plastic_arrow_image = pygame.image.load(path.join(img_dir, 'пластик.jpg')).convert()
plastic_arrow = plastic_arrow_image.get_rect()
plastic_arrow.topleft = (200, 50)
plastic_arrow_image.set_colorkey(WHITE)

organic_arrow_image = pygame.image.load(path.join(img_dir, 'органика.jpg')).convert()
organic_arrow = organic_arrow_image.get_rect()
organic_arrow.topleft = (380, 50)
organic_arrow_image.set_colorkey(WHITE)

paper_arrow_image = pygame.image.load(path.join(img_dir, 'бумага.jpg')).convert()
paper_arrow = paper_arrow_image.get_rect()
paper_arrow.topleft = (560, 50)
paper_arrow_image.set_colorkey(WHITE)

metal_arrow_image = pygame.image.load(path.join(img_dir, 'металл.jpg')).convert()
metal_arrow = metal_arrow_image.get_rect()
metal_arrow.topleft = (740, 50)
metal_arrow_image.set_colorkey(WHITE)

electronics_arrow_image = pygame.image.load(path.join(img_dir, 'электроника.jpg')).convert()
electronics_arrow = electronics_arrow_image.get_rect()
electronics_arrow.topleft = (920, 50)
electronics_arrow_image.set_colorkey(WHITE)

glass_garbage_image = pygame.image.load(path.join(img_dir, 'стекло2.jpg')).convert()
glass_garbage = glass_garbage_image.get_rect()
glass_garbage.topleft = (20, 350)
glass_garbage_image.set_colorkey(WHITE)

plastic_garbage_image = pygame.image.load(path.join(img_dir, 'пластик2.jpg')).convert()
plastic_garbage = plastic_garbage_image.get_rect()
plastic_garbage.topleft = (200, 350)
plastic_garbage_image.set_colorkey(WHITE)

organic_garbage_image = pygame.image.load(path.join(img_dir, 'органика2.jpg')).convert()
organic_garbage = organic_garbage_image.get_rect()
organic_garbage.topleft = (380, 350)
organic_garbage_image.set_colorkey(WHITE)

paper_garbage_image = pygame.image.load(path.join(img_dir, 'бумага2.jpg')).convert()
paper_garbage = paper_garbage_image.get_rect()
paper_garbage.topleft = (560, 350)
paper_garbage_image.set_colorkey(WHITE)

metal_garbage_image = pygame.image.load(path.join(img_dir, 'металл2.jpg')).convert()
metal_garbage = metal_garbage_image.get_rect()
metal_garbage.topleft = (740, 350)
metal_garbage_image.set_colorkey(WHITE)

electronics_garbage_image = pygame.image.load(path.join(img_dir, 'электроника2.jpg')).convert()
electronics_garbage = electronics_garbage_image.get_rect()
electronics_garbage.topleft = (920, 350)
electronics_garbage_image.set_colorkey(WHITE)

banana_image = pygame.image.load(path.join(img_dir, 'банан2.png')).convert()
banana = banana_image.get_rect()
banana.topleft = (70, 650)
banana_image.set_colorkey(WHITE)

glasses_image = pygame.image.load(path.join(img_dir, 'очки2.png')).convert()
glasses = glasses_image.get_rect()
glasses.topleft = (80, 750)
glasses_image.set_colorkey(WHITE)

can_image = pygame.image.load(path.join(img_dir, 'банка2.png')).convert()
can = can_image.get_rect()
can.topleft = (250, 640)
can_image.set_colorkey(WHITE)

fish_image = pygame.image.load(path.join(img_dir, 'рыба2.png')).convert()
fish = fish_image.get_rect()
fish.topleft = (230, 750)
fish_image.set_colorkey(WHITE)

bottle_image = pygame.image.load(path.join(img_dir, 'бутылка2.png')).convert()
bottle = bottle_image.get_rect()
bottle.topleft = (435, 620)
bottle_image.set_colorkey(WHITE)

pan_image = pygame.image.load(path.join(img_dir, 'сковорода2.png')).convert()
pan = pan_image.get_rect()
pan.topleft = (435, 720)
pan_image.set_colorkey(WHITE)

hanger_image = pygame.image.load(path.join(img_dir, 'вешалка2.png')).convert()
hanger = hanger_image.get_rect()
hanger.topleft = (590, 630)
hanger_image.set_colorkey(WHITE)

phone_image = pygame.image.load(path.join(img_dir, 'телефон2.png')).convert()
phone = phone_image.get_rect()
phone.topleft = (635, 730)
phone_image.set_colorkey(WHITE)

newspaper_image = pygame.image.load(path.join(img_dir, 'газета2.png')).convert()
newspaper = newspaper_image.get_rect()
newspaper.topleft = (800, 630)
newspaper_image.set_colorkey(WHITE)

triangle_image = pygame.image.load(path.join(img_dir, 'треугольник2.png')).convert()
triangle = triangle_image.get_rect()
triangle.topleft = (800, 750)
triangle_image.set_colorkey(WHITE)

box_image = pygame.image.load(path.join(img_dir, 'коробка2.png')).convert()
box = box_image.get_rect()
box.topleft = (970, 630)
box_image.set_colorkey(WHITE)

camera_image = pygame.image.load(path.join(img_dir, 'фотоаппарат2.png')).convert()
camera = camera_image.get_rect()
camera.topleft = (980, 735)
camera_image.set_colorkey(WHITE)

music_image = pygame.image.load(path.join(img_dir, "музыка2.png"))
music_button = music_image.get_rect()
music_button.topleft = (0, 850)
music_image.set_colorkey(BLACK)


pygame.mixer.music.load(path.join(snd_dir, 'Autumn Forest.mp3'))
pygame.mixer.music.set_volume(0.4)


raspredeli_po_kategoriyam_sound = pygame.mixer.Sound(path.join(snd_dir,'Распредели по категориям.mp3'))
raspredeli_po_kategoriyam_sound.play()

question_image = pygame.image.load(path.join(img_dir,'вопрос2.png')).convert()
question_button = question_image.get_rect()
question_button.topleft = (1050,850)
question_image.set_colorkey(BLACK)

pygame.mixer.music.play(loops=-1)

incorrect_sound = pygame.mixer.Sound(path.join(snd_dir, 'звук неправильного ответа.mp3'))
incorrect_sound.set_volume(0.35)


x1_new = 0
y1_new = 0
x2_new = 0
y2_new = 0
x3_new = 0
y3_new = 0
x4_new = 0
y4_new = 0
x5_new = 0
y5_new = 0
x6_new = 0
y6_new = 0
x7_new = 0
y7_new = 0
x8_new = 0
y8_new = 0
x9_new = 0
y9_new = 0
x10_new = 0
y10_new = 0
x11_new = 0
y11_new = 0
x12_new = 0
y12_new = 0

running = True
moving1 = False
moving2 = False
moving3 = False
moving4 = False
moving5 = False
moving6 = False
moving7 = False
moving8 = False
moving9 = False
moving10 = False
moving11 = False
moving12 = False
flPause = False

while running:
    clock.tick(FPS)

    glass_rect = pygame.draw.rect(screen, BLACK, (60, 200, 100, 100), 1)
    plastic_rect = pygame.draw.rect(screen, BLACK, (237, 200, 100, 100), 1)
    organic_rect = pygame.draw.rect(screen, BLACK, (417, 200, 100, 100), 1)
    paper_rect = pygame.draw.rect(screen, BLACK, (597, 200, 100, 100), 1)
    metal_rect = pygame.draw.rect(screen, BLACK, (777, 200, 100, 100), 1)
    electronics_rect = pygame.draw.rect(screen, BLACK, (957, 200, 100, 100), 1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.mixer.music.stop()
            pygame.mixer.stop()
            running = False
            import Diplom.Main_Menu6

        if banana.x == 425 and banana.y == 390 and glasses.x == 60 and glasses.y == 380 and can.x == 790 and can.y == 380 and fish.x == 425 and fish.y == 490 and bottle.x == 60 and bottle.y == 480 and pan.x == 790 and pan.y == 480 and hanger.x == 250 and hanger.y == 380 and phone.x == 970 and phone.y == 380 and newspaper.x == 610 and newspaper.y == 380 and triangle.x == 250 and triangle.y == 480 and box.x == 610 and box.y == 480 and camera.x == 970 and camera.y == 480:
            print("Получилось")
            pygame.mixer.music.stop()
            raspredeli_po_kategoriyam_sound.stop()
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
            import Diplom.Main_Menu6
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            if banana.x < event.pos[0] < banana.x + 100 and banana.y < event.pos[1] < banana.y + 100:
                moving1 = True
            elif glasses.x < event.pos[0] < glasses.x + 100 and glasses.y < event.pos[1] < glasses.y + 100:
                moving2 = True
            elif can.x < event.pos[0] < can.x + 100 and can.y < event.pos[1] < can.y + 100:
                moving3 = True
            elif fish.x < event.pos[0] < fish.x + 100 and fish.y < event.pos[1] < fish.y + 100:
                moving4 = True
            elif bottle.x < event.pos[0] < bottle.x + 100 and bottle.y < event.pos[1] < bottle.y + 100:
                moving5 = True
            elif pan.x < event.pos[0] < pan.x + 100 and pan.y < event.pos[1] < pan.y + 100:
                moving6 = True
            elif hanger.x < event.pos[0] < hanger.x + 100 and hanger.y < event.pos[1] < hanger.y + 100:
                moving7 = True
            elif phone.x < event.pos[0] < phone.x + 100 and phone.y < event.pos[1] < phone.y + 100:
                moving8 = True
            elif newspaper.x < event.pos[0] < newspaper.x + 100 and newspaper.y < event.pos[1] < newspaper.y + 100:
                moving9 = True
            elif triangle.x < event.pos[0] < triangle.x + 100 and triangle.y < event.pos[1] < triangle.y + 100:
                moving10 = True
            elif box.x < event.pos[0] < box.x + 100 and box.y < event.pos[1] < box.y + 100:
                moving11 = True
            elif camera.x < event.pos[0] < camera.x + 100 and camera.y < event.pos[1] < camera.y + 100:
                moving12 = True

            if music_button.collidepoint(pos):
                flPause = not flPause
                if flPause:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()

            if question_button.collidepoint(pos):
                raspredeli_po_kategoriyam_sound.stop()
                incorrect_sound.stop()
                raspredeli_po_kategoriyam_sound.play()

        if event.type == pygame.MOUSEMOTION:
            if moving1:
                x1_new, y1_new = event.rel
                banana.x, banana.y = banana.x + x1_new, banana.y + y1_new
                if banana.centerx == organic_rect.centerx:
                    banana.x = 425
                    banana.y = 390
                    moving1 = False

            elif moving2:
                x2_new, y2_new = event.rel
                glasses.x, glasses.y = glasses.x + x2_new, glasses.y + y2_new
                if glasses.centerx == glass_rect.centerx:
                    glasses.x = 60
                    glasses.y = 380
                    moving2 = False

            elif moving3:
                x3_new, y3_new = event.rel
                can.x, can.y = can.x + x3_new, can.y + y3_new
                if can.centery == metal_rect.centery:
                    can.x = 790
                    can.y = 380
                    moving3 = False

            elif moving4:
                x4_new, y4_new = event.rel
                fish.x, fish.y = fish.x + x4_new, fish.y + y4_new
                if fish.centery == organic_rect.centery:
                    fish.x = 425
                    fish.y = 490
                    moving4 = False

            elif moving5:
                x5_new, y5_new = event.rel
                bottle.x, bottle.y = bottle.x + x5_new, bottle.y + y5_new
                if bottle.centerx == glass_rect.centerx:
                    bottle.x = 60
                    bottle.y = 480
                    moving5 = False

            elif moving6:
                x6_new, y6_new = event.rel
                pan.x, pan.y = pan.x + x6_new, pan.y + y6_new
                if pan.centerx == metal_rect.centerx:
                    pan.x = 790
                    pan.y = 480
                    moving6 = False

            elif moving7:
                x7_new, y7_new = event.rel
                hanger.x, hanger.y = hanger.x + x7_new, hanger.y + y7_new
                if hanger.centery == plastic_rect.centery:
                    hanger.x = 250
                    hanger.y = 380
                    moving7 = False

            elif moving8:
                x8_new, y8_new = event.rel
                phone.x, phone.y = phone.x + x8_new, phone.y + y8_new
                if phone.centery == electronics_rect.centery:
                    phone.x = 970
                    phone.y = 380
                    moving8 = False

            elif moving9:
                x9_new, y9_new = event.rel
                newspaper.x, newspaper.y = newspaper.x + x9_new, newspaper.y + y9_new
                if newspaper.centerx == paper_rect.centerx:
                    newspaper.x = 610
                    newspaper.y = 380
                    moving9 = False

            elif moving10:
                x10_new, y10_new = event.rel
                triangle.x, triangle.y = triangle.x + x10_new, triangle.y + y10_new
                if triangle.centerx == plastic_rect.centerx:
                    triangle.x = 250
                    triangle.y = 480
                    moving10 = False

            elif moving11:
                x11_new, y11_new = event.rel
                box.x, box.y = box.x + x11_new, box.y + y11_new
                if box.centery == paper_rect.centery:
                    box.x = 610
                    box.y = 480
                    moving11 = False

            elif moving12:
                x12_new, y12_new = event.rel
                camera.x, camera.y = camera.x + x12_new, camera.y + y12_new
                if camera.centery == electronics_rect.centery:
                    camera.x = 970
                    camera.y = 480
                    moving12 = False

        if event.type == pygame.MOUSEBUTTONUP:
            if banana.x != 425 and banana.y != 390:

                banana.x = 70
                banana.y = 650

            if glasses.x != 60 and glasses.y != 380:

                glasses.x = 80
                glasses.y = 750

            if can.x != 790 and can.y != 380:

                can.x = 250
                can.y = 640

            if fish.x != 425 and fish.y != 490:

                fish.x = 230
                fish.y = 750

            if bottle.x != 60 and bottle.y != 480:

                bottle.x = 435
                bottle.y = 620

            if pan.x != 790 and pan.y != 480:

                pan.x = 435
                pan.y = 720

            if hanger.x != 250 and hanger.y != 380:

                hanger.x = 590
                hanger.y = 630

            if phone.x != 970 and phone.y != 380:

                phone.x = 635
                phone.y = 730

            if newspaper.x != 610 and newspaper.y != 380:

                newspaper.x = 800
                newspaper.y = 630

            if triangle.x != 250 and triangle.y != 480:

                triangle.x = 800
                triangle.y = 750

            if box.x != 610 and box.y != 480:

                box.x = 970
                box.y = 630

            if camera.x != 970 and camera.y != 480:

                camera.x = 980
                camera.y = 735

            moving1 = False
            moving2 = False
            moving3 = False
            moving4 = False
            moving5 = False
            moving6 = False
            moving7 = False
            moving8 = False
            moving9 = False
            moving10 = False
            moving11 = False
            moving12 = False

    screen.blit(glass_arrow_image, glass_arrow)
    screen.blit(plastic_arrow_image, plastic_arrow)
    screen.blit(organic_arrow_image, organic_arrow)
    screen.blit(paper_arrow_image, paper_arrow)
    screen.blit(metal_arrow_image, metal_arrow)
    screen.blit(electronics_arrow_image, electronics_arrow)



    screen.blit(glass_garbage_image, glass_garbage)
    screen.blit(plastic_garbage_image, plastic_garbage)
    screen.blit(organic_garbage_image, organic_garbage)
    screen.blit(paper_garbage_image, paper_garbage)
    screen.blit(metal_garbage_image, metal_garbage)
    screen.blit(electronics_garbage_image, electronics_garbage)

    screen.blit(banana_image, banana)
    screen.blit(glasses_image, glasses)
    screen.blit(can_image, can)
    screen.blit(fish_image, fish)
    screen.blit(bottle_image, bottle)
    screen.blit(pan_image, pan)
    screen.blit(hanger_image, hanger)
    screen.blit(phone_image, phone)
    screen.blit(newspaper_image, newspaper)
    screen.blit(triangle_image, triangle)
    screen.blit(box_image, box)
    screen.blit(camera_image, camera)

    screen.blit(music_image, music_button)
    screen.blit(question_image, question_button)

    pygame.display.flip()
    screen.fill(WHITE)

pygame.quit()
