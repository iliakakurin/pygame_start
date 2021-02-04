class Player():
    # задаем сами всем одинаково
    size = 30       # размер игрока
    speed_y = 0     # скорость по вертикали
    phase = 0       # фаза прыжка

    def __init__(self, x_pos, y_pos):
        # определяются при создании
        self.x = x_pos          # координата х
        self.y = y_pos          # координата у


# создать класс препятствия
class Cactus():
    speed_x = -1

    def __init__(self, x_pos, y_pos, width, height):
        self.x = x_pos
        self.y = y_pos
        self.w = width
        self.h = height
