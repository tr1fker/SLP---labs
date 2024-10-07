import sys

# 2. Создать текстовый файл (не программно). Построчно записать
# фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад больше 10 тысяч, вывести
# фамилии этих сотрудников. Выполнить подсчёт средней величины дохода
# сотрудников.
# Пример файла:~
# Иванов 23543.12
# Петров 13749.32– 3 балла
# 3. Сформировать (не программно) текстовый файл. В нём каждая
# строка должна описывать учебный предмет и наличие лекционных,
# практических и лабораторных занятий по предмету. Сюда должно входить и
# количество занятий. Необязательно, чтобы для каждого предмета были все
# типы занятий.
# Сформировать словарь, содержащий название предмета и общее
# количество занятий по нему. Вывести его на экран.
# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
#  Физика: 30(л) 10(лаб)
#  Физкультура: 30(пр)
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”:
# 30}– 3 балла
# 4. Создать вручную и заполнить несколькими строками текстовый
# файл, в котором каждая строка будет содержать данные о фирме: название,
# форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой
# компании, а также среднюю прибыль. Если фирма получила убытки, в расчёт
# средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и
# их прибылями, а также словарь со средней прибылью. Если фирма получила
# убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000},
# {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий
# файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit":
# 2000}]
# Подсказка: использовать менеджер контекста. – 1 балл (задача на
# оценку 10)


def first_task():
    print("""----------------------------------------------------------------------------
    Задача: Создать программный файл F1 в текстовом формате, записать в него
построчно данные, вводимые пользователем. Об окончании ввода данных будет 
свидетельствовать пустая строка. Скопировать из файла F1 в файл F2, все
строки, в которых более 2 слов. – 3 балл
----------------------------------------------------------------------------""")
    with open('Documents_task_1/F1.txt', 'w', encoding='utf-8') as file1:
        while True:
            line = input("Введите строку(пустая строка для завершения):")
            if line == "":
                print("Ввод завершен!")
                break
            file1.write(line + "\n")
            print("Данные успешно записаны!")
    with open('Documents_task_1/F1.txt', 'r', encoding='utf-8') as file1, open('Documents_task_1/F2.txt', 'w', encoding='utf-8') as file2:
        lines = file1.readlines()
        for line in lines:
            if line.count(' ') > 0:
                file2.write(line)
        print("Данные успешно скопированы во 2-ой файл!")


def second_task():
    print("""-------------------------------------------------------------------
    Создать текстовый файл (не программно). Построчно записать
фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад больше 10 тысяч, вывести
фамилии этих сотрудников. Выполнить подсчёт средней величины дохода
сотрудников.
-------------------------------------------------------------------
Пример файла:~
Иванов 23543.12
#Петров 13749.32– 3 балла
-------------------------""")
    with open("Documents_task_2/employees.txt", "w", encoding="utf-8") as file_employees:
        number = None
        while not number:
            number = input_integer_min("Введите кол-во сотрудников(0 - выход):", 0)
        if number == 0:
            print("---------------\n"
                  "Успешный выход!")
        else:
            for _employee in range(number):
                name = input(f"Введите фамилию {_employee + 1}-сотрудника:")
                salary = None
                while not salary:
                    salary = input_float(f"Введите зарплату {_employee + 1}-сотрудника:")
                file_employees.write(name + " " + str(salary) + "\n")
            print("----------------\n"
                  "Успешная запись!\n"
                  "----------------")
    with open("Documents_task_2/employees.txt", "r", encoding="utf-8") as file_employees:
        lines = file_employees.readlines()
        number_employees = len(lines)
        sum_salary = 0
        list_has_good_employee = False
        for line in lines:
            name, salary = line.split()
            salary = float(salary)
            if salary >= 10000:
                list_has_good_employee = True
                break
        if list_has_good_employee:
            print("Сотрудники с окладом > 10000:")
            for line in lines:
                name, salary = line.split()
                salary = float(salary)
                sum_salary += salary
                if salary > 10000:
                    print(name)
        else:
            print("В файле нет сотрудников с окладом > 10000!")
        print("Средняя зарплата сотрудников:", sum_salary / number_employees)




def third_task():
    pass
def fourth_task():
    pass

def input_float(CONDITION_INPUT_INTEGER):
    try:
        line = float(input(CONDITION_INPUT_INTEGER))
        return line
    except ValueError:
        print("------------------------------\n"
              "Введено некорректное значение!")
    return None

def input_integer(CONDITION_INPUT_INTEGER):
    try:
        line = int(input(CONDITION_INPUT_INTEGER))
        return line
    except ValueError:
        print("------------------------------\n"
              "Введено некорректное значение!")
    return None


def input_integer_minmax(CONDITION_INPUT_INTEGER, min_limit, max_limit):
    choice = input_integer(CONDITION_INPUT_INTEGER)
    if choice != None:
        if choice >= min_limit and choice <= max_limit:
            return choice
        else:
            print("Выход за границу!")
    return None


def input_integer_min(CONDITION_INPUT_INTEGER, min_limit):
    choice = input_integer(CONDITION_INPUT_INTEGER)
    if choice != None:
        if choice >= min_limit:
            return choice
        else:
            print("Выход за границу!")
    return None


MENU_TEXT = ("-----------------------------------\n"
             "Введите №(1-4) задача, '0' - выход:")


def main():
    program_is_work = True
    while (program_is_work):
        choice = input_integer_minmax(MENU_TEXT, 0, 4)
        if choice == 0:
            print("---------------\n"
                  "Успешный выход!")
            program_is_work = False
        elif choice == 1:
            first_task()
        elif choice == 2:
            second_task()
        elif choice == 3:
            third_task()
        elif choice == 4:
            fourth_task()
        else:
            print("Повторите попытку!")


main()