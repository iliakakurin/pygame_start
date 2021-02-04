# здесь подключаются модули
import pygame
import sys
from player_dino import *

# здесь определяются константы,
# классы и функции
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
# cactus = (x, y, w, h)
cactus = [Cactus(7 * W // 8, H // 2 - 2 * r, r, 2 * r)]
pl = Player(W // 8, H // 2 - r)
# здесь происходит инициация,
# создание объектов
pygame.init()
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

# если надо до цикла отобразить
# какие-то объекты, обновляем экран
pygame.display.update()

# главный цикл
while True:

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
                    pl.phase = 60
        # вверх 1073741906
        # вниз 1073741905
        # влево 1073741904
        # вправо 1073741903
        # пробел - 32



    # --------
    # изменение объектов
    # --------
    for cact in cactus:
        cact.x += cact.speed_x


    if pl.phase > 30:
        pl.speed_y = -3
    elif pl.phase > 0:
        pl.speed_y = 3
    elif pl.phase == 0:
        pl.speed_y = 0
    if pl.phase > 0:
        pl.phase -= 1
    pl.y += pl.speed_y


    sc.fill(WHITE)
    pygame.draw.circle(sc, YELLOW, (pl.x, pl.y), pl.size, 4)
    for cact in cactus:
        pygame.draw.rect(sc, PINK, (cact.x, cact.y, cact.w, cact.h))
    pygame.display.update()
