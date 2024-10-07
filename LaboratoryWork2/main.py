import math

OPTIONS_BETWEEN_TYPES = ("\
+----------------+\n\
|  Выберите для  |\n\
|ввода тип данных|\n\
+----------------+\n\
|1. Список       |\n\
|2. Словарь      |\n\
|3. Число        |\n\
|4. Строка       |\n\
+----------------+\n\
|5. Выйти        |\n\
+----------------+\n\
Введите значение:")


def input_integer(CONDITION):
    while True:
        print(CONDITION, end = '')
        try:
            number = int(input())
            return number
        except ValueError:
            print("Введено некорректное значение!\nПовторите попытку!")

def input_integer_positive(CONDITION):
    while True:
        number = input_integer(CONDITION)
        if number > 0:
            return number
        else:
            print("Введено отрицательное значени!\nПовторите попытку!")

def task_first():
    print("-" * 40)
    first_number = input_integer("Введите 1-ое число:")
    print("-" * 40)
    second_number = input_integer("Введите 2-ое число:")
    buffer_first = first_number
    buffer_second = second_number
    print("-" * 40)
    if buffer_first < 1 and buffer_second < 1:
        print("Невозможно найти НОК двух чисел, т. к. два числа не являются натуральными!")
    elif buffer_first < 1 and buffer_second > 0:
        print("Невозможно найти НОК двух чисел, т. к. 1-ое число не натуральное!")
    elif buffer_first > 0 and buffer_second < 1:
        print("Невозможно найти НОК двух чисел, т.к. 2-ое число не натуральное!")
    else:
        while buffer_first != buffer_second:
            if buffer_first > buffer_second:
                buffer_second += second_number
            else:
                buffer_first += first_number
        print("НОК двух чисел:", buffer_first)

def get_argument(variable):
    if isinstance(variable, list):
        variable = set(variable)
        print("Список уникальных элементов:", variable)
        multi = 1
        for number in variable:
            multi *= number
        if multi < 0:
            print("Невозможно найти среднее геометрическое, т. к. произведение всех чисел отрицательное!")
        else:
            print("Среднее геометрическое всех чисел:", math.sqrt(multi))
    elif isinstance(variable, dict):
        print("Ключи:", list(variable.keys()))
    elif isinstance(variable, int):
        print("Кол-во разрядов:", len([i for i in str(variable)]))
    elif isinstance(variable, str):
        variable += " "
        length_line = len(variable)
        counter = 0
        left_index = 0
        right_index = 0
        while right_index < length_line:
            if variable[right_index] == ' ':
                if right_index != left_index:
                    if variable[left_index: right_index] == variable[left_index: right_index][::-1]:
                        counter += 1
                left_index = right_index + 1
            right_index += 1
        print("Количество полиндромов:", counter)
    else:
        print("Некорректное значение!")



def input_list():
    number = input_integer_positive("Введите кол-во элементов в списке:")
    new_list = [input_integer(f"Введите {i + 1} число:") for i in range(number)]
    return new_list

def input_dict():
    number = input_integer_positive("Введите кол-во элементов в словаре:")
    new_dict = {input(f"Введите {i + 1} ключ:"): input_integer(f"Введите {i + 1} значение ключа:") for i in range(number)}
    return new_dict

def task_second():
    while True:
        #choice = input_integer(OPTIONS_BETWEEN_TYPES)
        variable = eval(input("Введите строку:"))
        print(variable)
        # if choice == 1:
        #     variable = input_list()
        # elif choice == 2:
        #     variable = input_dict()
        # elif choice == 3:
        #     variable = input_integer("Введите число:")
        # elif choice == 4:
        #     variable = input("Введите строку:")
        # elif choice == 5:
        #     print("_" * 10 + "Успешный выход!" + "_" * 10)
        #     break
        # else:
        #     print("Введено некорректное значение!\nПовторите попытку!")
        #get_argument(variable)


def task_third():
    n = input_integer("Введите n:")
    m = input_integer("Введите m:")
    new_list = [' '.join(['.' if (column + stroke) % 2 == 0 else '*' for column in range(m)]) for stroke in range(n)]
    print("Двумерный массив:", *new_list, sep = "\n")

def task_fouth():
    try:
        number = int(input("Введите число:"))
        print("Успешный ввод числа:", number)
    except ValueError:
        print("Введено некорректное значение!")
    finally:
        print("Завершение функции.")

def main():
    menu_is_work = True
    while menu_is_work:
        print("-" * 40)
        option = input_integer("Введите №(1-4) задачи, '0' - выход:")
        if option == 0:
            print("_" * 10 + "Успешный выход!" + "_" * 10)
            menu_is_work = False
        elif option == 1:
            task_first()
        elif option == 2:
            task_second()
        elif option == 3:
            task_third()
        elif option == 4:
            task_fouth()
        else:
            print("Неверный диапазон!")
main()