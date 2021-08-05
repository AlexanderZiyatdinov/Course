```python
from random import randrange
from Figures import Platform, Ball, Block
from pygame import Rect
import pygame

# TODO 1 Дописать функцию ниже: (Это самое сложное исправление)


def change_direction(dx, dy, ball: Rect, figure: Rect):
    """Функция, которая проверяет не случилось ли столкновения
    Между шаром и каким-то другим объектом (напр. платформой или блоком)
    Если такое столкновение произошло, то необходимо поменять направление
    dx и dy

    :param  float dx: Направление по x
    :param  float dy: Направление по y
    :param  Rect ball: Объект - шар
    :param  Rect figure: Объект, с которым сталкивается шар
    """
    if dx > 0:
        delta_x = ball.right - figure.left
    else:
        delta_x = figure.right - ball.left

    if dy > 0:
        delta_y = ball.bottom - figure.top
    else:
        delta_y = figure.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    elif delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy


# Глобальные переменные и константы
# TODO 2 Хмм, кажется тут какой-то баг. Почему-то высота слишком огромная
WIDTH = 1200  # Ширина
HEIGHT = 720  # Высота
FPS = 60  # Количество отрисовываемых кадров в секунду

# Платформа
platform = Platform(WIDTH // 2 - 330 // 2, HEIGHT - 35, 330, 35)

# Шар
ball_radius = 20
ball_position = int(ball_radius * 2 ** 0.5)
ball = Ball(WIDTH // 2 - 330 // 2, HEIGHT - 35, ball_radius, ball_radius)


# Блоки
# TODO 3 Надо создать блоки по следующим правилам:
# Создать 4 ряда блоков
# В каждом ряду по 10 блоков
# Размер каждого блока 100 на 50
# Верхний левый блок создается самым первым в точке (10, 10)
# y (top),  x (left)
# Последующие блоки должны создаваться так:
# Блок в том же ряду смещен на 120 пикселей от предыдущего вправо
# Блок в том же столбце смещен на 70 пикселей от прерыдущего вниз

# Пример: чтобы создать блок, который находится в точке left: 100 top:200
# размером 70 на 50, надо написать
# Block(100, 200, 70, 50)
blocks = [Block(10 + 120 * i, 10 + 70 * j, 100, 50)
          for i in range(10) for j in range(4)]  # comprehensions..

# Цвета блоков
blocks_colors = [(randrange(30, 256), randrange(30, 256), randrange(30, 256))
                 for i in range(10) for j in range(4)]

# Настройки и необходимые переменные
dx, dy = 1, -1  # Коэффициенты движения
pygame.init()  # Инициализация игры
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()  # Таймер обновления состояний игры
# Устанавливаем фон. Можете поставить свою картинку :)
background_image = pygame.image.load('background.png').convert()

while True:  # Основноый цикл программы
    for event in pygame.event.get():  # Для каждого очередного события
        if event.type == pygame.QUIT:  # Если был нажат выход
            exit()  # То выйти
    # Иначе продолжаем работу
    sc.blit(background_image, (0, 0))  # Устанавливаем картинку на фон

    # Отрисовка игры
    # Отрисовка блоков
    [pygame.draw.rect(sc, blocks_colors[color], block) for color, block in
     enumerate(blocks)]

    # Отрисовка платформы и выбор цвета платформы
    # TODO 4 установите цвет 'darkorange' для платформы
    pygame.draw.rect(sc, pygame.Color('darkorange'), platform)

    # Отрисовка шара
    pygame.draw.circle(sc, pygame.Color('white'), ball.center, ball_radius)

    # Изменение положения шара в пространстве
    ball.x += ball.speed * dx
    ball.y += ball.speed * dy

    # Проверка столкновения шара со стенами
    if ball.centerx < ball_radius or ball.centerx > WIDTH - ball_radius:
        dx = -dx

    if ball.centery < ball_radius:
        dy = -dy

    # Проверка столкновения шара с платформой
    if ball.colliderect(platform) and dy > 0:  # Если шар врезался в платформу
        dx, dy = change_direction(dx, dy, ball, platform)  # Меняем направление

    # Проверка столкновения шара с блоком
    block = ball.collidelist(blocks)  # Специальный флаг, который симв. столкн.
    if block != -1:
        # Меняем направление и удаляем блок, в который попал шар
        dx, dy = change_direction(dx, dy, ball, blocks.pop(block))
        # TODO 5 Понизить ускорение шара после попадания в блок в 10 раз.
        FPS += 2  # Ускоряем игру

    # Обработка конца игры
    if ball.bottom > HEIGHT:
        print("ИГРА ОКОНЧЕНА")
        exit()
    elif not blocks:
        print("ВЫ ПОБЕДИЛИ!")
        exit()

    # Контроль и управление
    key = pygame.key.get_pressed()

    # TODO 6 Поправить управление.
    #  При нажатии ← платформа должна ехать влево и не выезжать за окно
    #  При нажатии → платформа должна ехать право и не выезжать за окно

    # Если нажата клавиша ←
    if key[pygame.K_LEFT] and platform.left > 0:
        platform.left -= platform.speed
    # Если нажата клавиша →
    if key[pygame.K_RIGHT] and platform.right < WIDTH:
        platform.right += platform.speed

    # Обновление состояния игры
    pygame.display.flip()
    clock.tick(FPS)

```

