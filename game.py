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
WIDTH = 600
HEIGHT = 400

# здесь происходит инициация,
# создание объектов
pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
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
    sc.fill(WHITE)
    # обновление экрана
    pygame.display.update()
