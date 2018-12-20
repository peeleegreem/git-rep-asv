__author__ = 'Вертипрахов Александр Сергеевич'

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math
from typing import Dict


class Point:
    def __init__(self, a: int, b: int):
        self.x = a
        self.y = b

class Line:
    def get_lenght(self, p1: Point, p2: Point) -> float:
        leng = math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)
        if leng != 0.0:
            return leng
        else:
            raise RuntimeError('Сторона с заданными координатами не существует, потому что длина равна нулю')

class Triangle:
    def __init__(self, a1: int, b1: int, a2: int, b2: int, a3: int, b3: int):
        self._point1 = Point(a1, b1)
        self._point2 = Point(a2, b2)
        self._point3 = Point(a3, b3)
        side = Line()
        self._side1 = side.get_lenght(self._point1, self._point2)
        self._side2 = side.get_lenght(self._point3, self._point2)
        self._side3 = side.get_lenght(self._point3, self._point1)

    def _check_triangle_exists(self) -> bool:
        return self._get_square() != 0.0

    def _get_square(self) -> float:
        perimeter = self.get_perimeter()
        return math.sqrt(perimeter*(perimeter-self._side1)*(perimeter-self._side2)*(perimeter-self._side3))

    def get_square(self) -> float:
        if not self._check_triangle_exists():
            raise RuntimeError('Треугольник с заданными координатами не существует, потому что площадь равна нулю')

        perimeter = self.get_perimeter()
        return math.sqrt(perimeter*(perimeter-self._side1)*(perimeter-self._side2)*(perimeter-self._side3))

    def get_perimeter(self) -> float:
        if not self._check_triangle_exists:
            raise RuntimeError('Треугольник с заданными координатами не существует')
        return self._side1 + self._side2 + self._side3

    def get_hight(self, side_num: float) -> float:
        if not self._check_triangle_exists:
            raise RuntimeError('Треугольник с заданными координатами не существует')
        if side_num == 1:
            side = self._side1
        elif side_num == 2:
            side = self._side2
        else:
            side = self._side3
        return self._get_square() * 2 / side

t = Triangle(11, 22, 33, 44, 55, 66)
print(f'Площадь равна {t.get_square()}')
print(f'Периметр равен {t.get_perimeter()}')
print(f'Высота с основанием стороны равна {t.get_hight(1)}')

"""
Ниже код Задача-2
"""

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class EqualTrapezioid:
    def __init__(self, a1: int, b1: int, a2: int, b2: int, a3: int, b3: int, a4: int, b4: int):
        self._point1 = Point(a1, b1)
        self._point2 = Point(a2, b2)
        self._point3 = Point(a3, b3)
        self._point4 = Point(a4, b4)
        self._line = Line()
        sides = self._get_sides()
        self._size_a = sides.get('a')
        self._size_b = sides.get('b')
        self._size_c = sides.get('c')

    def check_trapezioid_equal(self):
        diagonal1 = self._line.get_lenght(self._point1, self._point3)
        diagonal2 = self._line.get_lenght(self._point4, self._point2)
        return diagonal1 == diagonal2

    def _get_sides(self) -> Dict:
        if not self.check_trapezioid_equal():
            raise RuntimeError('Построить трапецию с заданными координатами невозможно')

        side1 = self._line.get_lenght(self._point1, self._point2)
        side2 = self._line.get_lenght(self._point3, self._point2)
        side3 = self._line.get_lenght(self._point3, self._point4)
        side4 = self._line.get_lenght(self._point4, self._point1)

        if side1 == side2:
            return {'a': side3, 'b': side4, 'c': side1}
        elif side1 == side3:
            return {'a': side2, 'b': side4, 'c': side1}
        elif side1 == side4:
            return {'a': side2, 'b': side3, 'c': side1}
        elif side2 == side3:
            return {'a': side1, 'b': side4, 'c': side2}
        elif side2 == side4:
            return {'a': side1, 'b': side3, 'c': side2}
        else:
            return {'a': side1, 'b': side2, 'c': side3}

    def get_side_lengths(self) -> list:
        return [str(self._size_c), str(self._size_a), str(self._size_b), str(self._size_c)]

    def get_square(self) -> float:
        if not self.check_trapezioid_equal():
            raise RuntimeError('Построить трапецию с заданными координатами невозможно')
        return (self._size_a + self._size_b)* math.sqrt(4*self._size_c**2 - (self._size_a - self._size_b)**2) / 4

    def get_perimeter(self) -> float:
        return self._size_a + self._size_b + 2 * self._size_c

tr = EqualTrapezioid(1, 1, 2, 2, 4, 2, 5, 1)
print(f'Является ли фигура равнобочной трапецией? {tr.check_trapezioid_equal()}')
print(f'Площадь равна {tr.get_square()}')
print(f'Периметр равен {tr.get_perimeter()}')
print('Длины сторон равны: {}'.format(', '.join(tr.get_side_lengths())))
