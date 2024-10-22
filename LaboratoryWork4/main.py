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
        second_side = while_input_integer("Введите 2-ую сторону треугольника:", 1)
        self.b = second_side
    def input_third_side(self):
        third_side = while_input_integer("Введите 3-ю сторону треугольника:", 1)
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
    task_is_work = True
    triangle = Triangle(0, 0, 0)
    first_size, second_side, third_side = 0, 0, 0
    while task_is_work:
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
            task_is_work = False


class Room:
    width, height, length = 0, 0, 0
    count_windows, height_window, width_window = 0, 0, 0
    count_doors, height_door, width_door = 0, 0, 0
    def __init__(self, width = 0, height = 0, length = 0):
        self.width, self.height, self.length = width, height, length
    def input_width(self):
        width = while_input_integer("Введите ширину комнаты:", 1)
        self.width = width
    def input_height(self):
        height = while_input_integer("Введите высоту комнаты:", 1)
        self.height = height
    def input_length(self):
        length = while_input_integer("Введите длину комнаты:", 1)
        self.length = length
    def get_square_wall(self):
        square_doors = self.count_doors * self.height_door * self.width_door
        square_windows = self.count_windows * self.height_window * self.width_window
        square_walls = (self.width + self.length) * self.height * 2
        return square_walls - square_doors - square_windows
    def input_count_windows(self):
        count_windows = while_input_integer("Введите кол-во окон:", 0)
        self.count_windows = count_windows
    def input_width_window(self):
        width_window = while_input_integer("Введите ширину окна:", 1)
        self.width_window = width_window
    def input_height_window(self):
        heigth_windows = while_input_integer("Введите высоту окна:", 1)
        self.height_window = heigth_windows
    def input_count_doors(self):
        count_doors = while_input_integer("Введите кол-во дверей:", 0)
        self.count_doors = count_doors
    def input_width_door(self):
        width_door = while_input_integer("Введите ширину двери:", 1)
        self.width_door = width_door
    def input_height_door(self):
        heigth_door = while_input_integer("Введите высоту двери:", 1)
        self.height_door = heigth_door
def second_task():
    print("""-------------------------------------------------------------------------
# Задание 2:
# Требуется написать программу, которая вычисляет общую площадь стены
# комнаты, которую необходимо оклеить обоями. При этом окна, двери, пол и
# потолок оклеивать не нужно. – 3 балла
-------------------------------------------------------------------------""")
    task_is_work = True
    room = Room()
    while task_is_work:
        number = while_input_integer("+---------------------------------+\n\
|              Меню               |\n\
+---------------------------------+\n\
|1. Ввести ширину комнаты         |\n\
|2. Ввести высоту комнаты         |\n\
|3. Ввести длину комнаты          |\n\
|4. Ввести кол-во окон            |\n\
|5. Ввести ширину окон            |\n\
|6. Ввести высоту окон            |\n\
|7. Ввести кол-во дверей          |\n\
|8. Ввести ширину дверей          |\n\
|9. Ввести высоту дверей          |\n\
|10. Узнать свободную площадь стен|\n\
+---------------------------------+\n\
|0. Выход                         |\n\
+---------------------------------+\n\
Введите значение:", 0, 10)
        if number == 1:
            room.input_width()
        elif number == 2:
            room.input_height()
        elif number == 3:
            room.input_length()
        elif number == 4:
            room.input_count_windows()
        elif number == 5:
            room.input_width_window()
        elif number == 6:
            room.input_height_window()
        elif number == 7:
            room.input_count_doors()
        elif number == 8:
            room.input_width_door()
        elif number == 9:
            room.input_height_door()
        elif number == 10:
            square = room.get_square_wall()
            if square > 0:
                print("Площадь:", square)
            else:
                print("Неверно указаны данные!")
        else:
            task_is_work = False

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