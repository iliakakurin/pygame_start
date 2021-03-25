# здесь подключаются модули
import pygame
import sys
from player_dino import *

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
W = 600
H = 400



r = 30
vx = -1
g = 10
v0 = -10
# cactus = (x, y, w, h)
#pl = Player(W // 8, H // 2 - r - 40)

# здесь происходит инициация,
# создание объектов
pygame.init()
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
player_surf = pygame.image.load('player 2.png')
cactus_surf = pygame.image.load('cactus.png')
player_surf.set_colorkey((255, 255, 255))
cactus_surf.set_colorkey((255,255,255))

pl = Player(W // 8 - 50, H // 2 - 91, player_surf)
cactus = Cactus(7 * W // 8, H // 2, cactus_surf)
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
            print(i)
            if i.key == 32:
                if pl.phase == 0:
                    pl.phase = 121
                    pl.speed_y = v0

    cactuses.update(g, FPS, H)

    if counter % (3 * FPS) == 0:
        new_cactus = Cactus(7 * W // 8, H // 2, cactus_surf)
        #cactus.append(new_cactus)
        cactuses.add(new_cactus)

    pl.update(g,FPS,H)

    if pl.phase > 0:
        pl.phase -= 1
        pl.speed_y += g / FPS
        pl.y += 30 * pl.speed_y / FPS
    if pl.phase == 0:
        pl.speed_y = 0
        pl.y = H // 2 - r

    sc.fill(WHITE)
    pygame.draw.line(sc, BLACK, (0, H // 2), (W, H // 2))
    sc.blit(pl.image, pl.rect)

    cactuses.draw(sc)
    pygame.display.update()
