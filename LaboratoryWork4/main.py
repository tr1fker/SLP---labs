# Задание 2:
# Требуется написать программу, которая вычисляет общую площадь стены
# комнаты, которую необходимо оклеить обоями. При этом окна, двери, пол и
# потолок оклеивать не нужно. – 3 балла
# Задание 3:
# Создать классы Circle (круг), Square (квадрат), Rectangle (прямоугольник) для
# описания плоских геометрических фигур. Переопределить метод нахождения
# площади фигуры. – 3 балла
# Задание 4:
# Придумать класс самостоятельно, реализовать в нем методы экземпляра
# класса, статические, методы, методы класса. – 1 – 3 балла
import math
import sys

def input_integer():
    try:
        number = int(input())
        return number
    except ValueError:
        print("Введено некорректное значение!")
    return None

def while_input_integer(CONDITION, min = -sys.maxsize - 1, max = sys.maxsize):
    success_input = False
    number = None
    while not success_input:
        print(CONDITION, end="")
        number = input_integer()
        if number != None:
            if number >= min and number <= max:
                success_input = True
            else:
                print("Вы вышли за границу!")
    return number
class Triangle:
    a, b, c = 0, 0, 0
    def __init__(self, a = 0, b = 0, c = 0):
        self.a, self.b, self.c = a, b, c
    def call(self, a = 0, b = 0, c = 0):
        self.a, self.b, self.c = a, b, c
    def is_instance(self):
        if self.a == 0 or self.b == 0 or self.c == 0:
            return False
        max_side = max(self.a, max(self.b, self.c))
        return True if max_side < self.a + self.b + self.c - max_side else False
    def get_perimeter(self):
        if not self.is_instance():
            print("Треугольник не существует!")
            return 0
        return self.a + self.b + self.c
    def input_first_side(self):
        first_side = while_input_integer("Введите 1-ую сторону треугольника:", 1)
        self.a = first_side
    def input_second_side(self):
        second_side = while_input_integer("Введите 1-ую сторону треугольника:", 1)
        self.b = second_side
    def input_third_side(self):
        third_side = while_input_integer("Введите 1-ую сторону треугольника:", 1)
        self.c = third_side
    def get_square(self):
        if not self.is_instance():
            print("Треугольник не существует!")
            return 0
        semiperimeter = self.get_perimeter() / 2
        return math.sqrt(semiperimeter * (semiperimeter - self.a) * (semiperimeter - self.b) * (semiperimeter - self.c))
def first_task():
    print("""---------------------------------------------------------------------
# Задание 1: Класс Triangle
# Создайте класс Triangle. В нём пропишите 3 (метода) функции. Первый
# метод: проверка на существование треугольника по данным сторонам.
# Второй метод : нахождение площади треугольника. Третий метод:
# нахождение периметра треугольника. – 1 балл
----------------------------------------------------------------------""")
    first_task_work = True
    triangle = Triangle(0, 0, 0)
    first_size, second_side, third_side = 0, 0, 0
    while first_task_work:
        number = while_input_integer("+---------------------------------------+\n\
|                  Меню                 |\n\
+---------------------------------------+\n\
|1. Изменить первую сторону.            |\n\
|2. Изменить вторую сторону.            |\n\
|3. Изменить третью сторону.            |\n\
|4. Проверить существует ли треугольник.|\n\
|5. Узнать площадь треугольника.        |\n\
|6. Узнать периметр треугольника.       |\n\
+---------------------------------------+\n\
|0. Выход.                              |\n\
+---------------------------------------+\n\
Введите значение(0-6):")
        if number == 1:
            triangle.input_first_side()
        elif number == 2:
            triangle.input_second_side()
        elif number == 3:
            triangle.input_third_side()
        elif number == 4:
            print("Треугольник " + ("" if triangle.is_instance() else "не ") + "существует!")
        elif number == 5:
            square = triangle.get_square()
            if square != 0:
                print("Площадь треугольника:", square)
        elif number == 6:
            perimeter = triangle.get_perimeter()
            if perimeter != 0:
                print("Периметр треугольника:", perimeter)
        else:
            first_task_work = False


def second_task():
    pass
def third_task():
    pass
def fourth_task():
    pass

def main():
    program_is_work = True
    while program_is_work:
        number = while_input_integer("Введите №(1-4) задания (0 - выход):", 0, 4)
        if number == 1:
            first_task()
        elif number == 2:
            second_task()
        elif number == 3:
            third_task()
        elif number == 4:
            fourth_task()
        else:
            program_is_work = False

main()