# здесь подключаются модули
import pygame
import sys

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
cactus = [7 * W // 8, H // 2 - r, r, r]
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


    # --------
    # изменение объектов
    # --------
    cactus[0] = cactus[0] + vx


    sc.fill(WHITE)
    pygame.draw.circle(sc, YELLOW, (W // 8, H // 2 - r), r, 4)
    pygame.draw.rect(sc, PINK, (cactus[0], cactus[1], cactus[2], cactus[3]), 4)
    pygame.draw.line(sc, BLACK, (0, H // 2), (W, H // 2))
    # обновление экрана
    pygame.display.update()

    # нарисовать в pygame шаблон для игры - схематично изобразить дорогу, динозаврика, кактусы
    # добавить прыжки, приседания, пересечения Д и К, 
