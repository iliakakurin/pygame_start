# здесь подключаются модули
import pygame
import sys
from player_dino import *

pygame.init()
pygame.mixer.init()
W = 600
H = 400
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
score = 0

def update_score():
    pg.display.set_caption(str(Cactus.score))

# здесь определяются константы,
# классы и функции
counter = 0
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
FPS = 60




r = 30
vx = -4
g = 10
v0 = -10
# cactus = (x, y, w, h)
#pl = Player(W // 8, H // 2 - r - 40)

# здесь происходит инициация,
# создание объектов


player_surf = pygame.image.load('player 2.png')
cactus_surf = pygame.image.load('cactus.png')
cactus_surf2 = pygame.image.load('car1.png')
player_surf.set_colorkey((255, 255, 255))
cactus_surf.set_colorkey((255, 255, 255))

mask = pygame.mask.from_surface(player_surf)
mask.invert()
# player_surf = mask.to_surface(player_surf)

cactus_surf_list = [cactus_surf, cactus_surf2]

death_sound = pygame.mixer.Sound('death.mp3')
death_sound.set_volume(0.5)


pl = Player(W // 8 - 50, H // 2 - 91, player_surf)
cactus = Cactus(7 * W // 8, H // 2, cactus_surf_list)
cactuses = pg.sprite.Group()
cactuses.add(cactus)

# если надо до цикла отобразить
# какие-то объекты, обновляем экран
pygame.display.update()

# главный цикл
while True:
    counter += 1
    # задержка
    clock.tick(FPS)

    # цикл обработки событий
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        if i.type == pygame.KEYDOWN:
            #print(i)
            if i.key == 32:
                if pl.phase == 0:
                    pl.phase = 126
                    pl.speed_y = v0

    cactuses.update(g, FPS, H)

    if counter % (3 * FPS) == 0:
        new_cactus = Cactus(7 * W // 8, H // 2, cactus_surf_list)
        #cactus.append(new_cactus)
        cactuses.add(new_cactus)

    pl.update(g,FPS,H)

    if pl.phase > 0:
        pl.phase -= 1
        pl.speed_y += g / FPS
        if pl.speed_y < 0:
            pl.y += 30 * (pl.speed_y + 1) / FPS
        else:
            pl.y += 30 * pl.speed_y / FPS
    if pl.phase == 0:
        pl.speed_y = 0
        pl.y = H // 2 - r
    #print(pl.speed_y, pl.rect.y)
    for c in cactuses:
        offset = (pl.rect.x + 10 - c.rect.x), (pl.rect.y + 25 - c.rect.y)
        overlap = mask.overlap(c.mask, offset)
        print(offset)
        if overlap:
            death_sound.play()
            print('WASTED')
            pygame.time.delay(2000)
            pygame.quit()
            sys.exit()

    # if pygame.sprite.spritecollideany(pl, cactuses):
    #     death_sound.play()
    #     print('WASTED')
    #     pygame.time.delay(2000)
    #     pygame.quit()
    #     sys.exit()
    update_score()

    sc.fill(WHITE)
    pygame.draw.line(sc, BLACK, (0, H // 2), (W, H // 2))
    sc.blit(pl.image, pl.rect)

    cactuses.draw(sc)
    pygame.display.update()

# TODO сами:
# TODO: 1) увеличивать скорость кактусов
# 2) приседание
# 3) птицы
# 4) счет
# 5) фоновая музыка
# 6) переменный промежуток меджу появлением кактусов
