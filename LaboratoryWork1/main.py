

def task_first():
    print("Задача: Дано натуральное число. Напишите программу, которая определяет, является ли последовательность его цифр при просмотре справа налево упорядоченной по убыванию. – 1 балл")
    number = input("Введите значение:")
    print(sorted(list(number)) == list(number))

def task_second():
    print("Задача: Посчитать, сколько пар (стоят рядом) верхнего и нижнего регистра находится в веденном с клавиатуры слове. (Пример HjkLM- 1 пара нижнего, 1 пара верхнего), а также сколько гласных букв в слове. – 2 балла")
    glas = "AEIOUYaeiouy"
    line = input("Введите слово:")
    length_line, counter_lower, counter_upper = len(line) - 1, 0, 0
    print("Кол-во гласных:", sum([(0, 1)[letter in glas] for letter in line]))
    while length_line > 0:
        if line[length_line].isupper() and line[length_line - 1].isupper():
            counter_upper += 1
            length_line -= 1
        elif line[length_line].islower() and line[length_line - 1].islower():
            counter_lower += 1
            length_line -= 1
        length_line -= 1
    print("Кол-во пар верхнего регистра:", counter_upper)
    print("Кол-во пар нижнего регистра:", counter_lower)

def task_third():
    length_list = int(input("Введите кол-во элементов списка:"))
    current_list = [int(input(f"Введите {_el + 1} элемент:")) for _el in range(length_list)]
    print("Сумма положительных элементов:", sum([el if el > 0 else 0 for el in current_list]))
    zero_finded, sum_after_zero = False, 0
    new_list = []
    for el in current_list:
        if el >= 0:
            new_list.append(el)
        if el == 0:
            zero_finded = True
        elif zero_finded:
            sum_after_zero += el
    print("Сумма элементов после 1-ого нуля: %d" % sum_after_zero if zero_finded else "Сумму посчитать нельзя")
    print("Новый список:", new_list)

def task_fourth():
    print("Задача: Отсортируйте словарь по значению в порядке возрастания и убывания. – 2 балла")
    counter_pair = int(input("Введите кол-во пар в словаре:"))
    current_list = [(input(f"Введите название {_el + 1} ключа:"), int(input(f"Введите значение {_el + 1} ключа:"))) for _el in range(counter_pair)]
    for _step in range(counter_pair - 1):
        for ind in range(0, counter_pair - _step - 1):
            if current_list[ind][1] > current_list[ind + 1][1]:
                current_list[ind], current_list[ind + 1] = current_list[ind + 1], current_list[ind]
    print("По возрастанию: ", dict(current_list))
    print("По убыванию: ", dict(current_list[::-1]))

def task_fifth():
    print("Задача: Реализуйте программу «Кондитерская», которая будет включать\nв себя шесть пунктов меню. У вас есть словарь, где ключ – название\nпродукции (торт, пирожное, маффин и т.д.). Значение – список,\nкоторый содержит состав, цену (за 100гр) и кол-во (в граммах). \n1. Просмотр описания: название – описание \n2. Просмотр цены: название – цена. \n3. Просмотр количества: название – количество. \n4. Всю информацию. \n5. Покупка\nВ пункте «Покупка» необходимо совершить покупку, с\nклавиатуры вводите название продукции и его кол-во, n – выход из\nпрограммы. Посчитать цену выбранных товаров и сколько товаров\nосталось в изначальном списке – 2 балла")
    counter_productions = int(input("Введите кол-во продукции:"))
    productions = dict([(input(f"Введите название {_el + 1} продукции:"), [
        input("Введите описание продукции:"), int(input("Цена за 100г:")), int(input("Кол-во г.:"))
    ]) for _el in range(counter_productions)])
    menu_is_work = True
    while menu_is_work:
        choice = int(input("1 - Просмотр описания: навазние - описание\n2 - Просмотр цены: название - цена\n3 - Просмотр количества: название количество\n4 - Вся информация\n5 - Покупка\nВведите значение: "))
        if choice == 1:
            for key, value in productions.items():
                print(key, "описание -", value[0])
        elif choice == 2:
            for key, value in productions.items():
                print(key, "цена за 100г -", value[1])
        elif choice == 3:
            for key, value in productions.items():
                print(key, "кол-во г. -", value[2])
        elif choice == 4:
            for key, value in productions.items():
                print(key, "\nОписание -", value[0], "\nЦена за 100г -", value[1], "\nКол-во г. -", value[2])
        elif choice == 5:
            price = 0
            inShop = True
            while inShop:
                production = input("Введите продукцию которую хотите купить или '0' - выход:")
                if production == "0":
                    inShop = False
                else:
                    for key, value in productions.items():
                        if key == production:
                            production_is_finded = True
                            weight = int(input("Введите кол-во г. для покупки:"))
                            if weight <= value[2]:
                                value[2] -= weight
                                price += weight / 100 * value[1]
                            else:
                                print("Нехватка товара!")
                            break
                    else:
                        print("Данной продукции не существует!")
            print("Потрачено -", price)
        else:
            menu_is_work = False

def task_sixth():
    print("Задача: Дан кортеж целых чисел. Вывести на экран первый и последний элемент кортежа. – 1 балл")
    korteg = tuple([int(input(f"Введите {_el + 1} число: ")) for _el in range(int(input("Введите кол-во чисел в кортеже:")))])
    print("Первый элемент:", korteg[0], "\nПоследний элемент:", korteg[-1])

def main():
    program_is_work = True
    while program_is_work:
        choice = int(input("Введите номер задачи(1-6):"))
        if choice == 1:
            task_first()
        elif choice == 2:
            task_second()
        elif choice == 3:
            task_third()
        elif choice == 4:
            task_fourth()
        elif choice == 5:
            task_fifth()
        elif choice == 6:
            task_sixth()
        else:
            program_is_work = False

main()