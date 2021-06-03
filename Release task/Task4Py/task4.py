import re


print("Task number 3 is launched through the console.")
my_num_task = int(input('Введите номер задачи: '))


def givePhoneNumbers(my_string):
    result = re.findall(r"[+]?[7-8][(]\d{3}[)]\d{7}", my_string)
    if len(result) != 0:
        print(result)
    else:
        print("Not found!")


def solveProgram():
    my_dict = {}
    print('Введите вашу программу: ')
    while True:  # считываем с клавиатуры и записываем в словарь
        pattern = input()
        my_key = re.findall(r"print[(]\w+[)]", pattern) or re.findall(r"^\w+", pattern)
        my_value = re.sub(r"(^\w+[ ]?[=][ ]?)|print[(]|^\w+|[)]|([;])", "", pattern)
        my_dict["".join(my_key)] = my_value
        if "".join(re.findall(r";", pattern)) != ';':
            break
    for key in my_dict:  # ищем предыдущие ключи в значении по текущему ключу
        if "".join(re.findall(r"(?!print)|[a-zA-Z]+", my_dict[key])) in my_dict:
            my_key = "".join(re.findall(r"[a-zA-Z]+", my_dict[key]))
            my_value = re.sub(r"[a-zA-Z]+", "".join(my_dict[my_key]), my_dict[key])
            my_dict[key] = my_value
    for key in my_dict:  # решаем уравнения
        try:
            my_dict[key] = eval(my_dict[key])
        except ZeroDivisionError:
            print('division by zero')
        if "".join(re.findall("print", key)):
            print(my_dict[key])


def myTask(i):
    if i == 1:
        return givePhoneNumbers(str(input('Введите вашу строку: ')))
    elif i == 2:
        return solveProgram()


myTask(my_num_task)
