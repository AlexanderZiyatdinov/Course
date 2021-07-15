import math
'''
math - библиотека с мат. функциями
distance - расстояние до цели
velocity - начальная скорость
'''


def bad_piggies(distance: float, velocity: float) -> float:
    if distance < 0:
        raise ValueError
    if velocity <= 0:
        raise ValueError
    angle: float = ... # ╰( ͡° ͜ʖ ͡° )つ──☆*:・ﾟ
    return angle


if __name__ == "__main__":
    distance: float = float(input())
    velocity: float = float(input())
    print(bad_piggies(distance, velocity))
