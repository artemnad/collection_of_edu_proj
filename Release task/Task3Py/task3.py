import re

my_num_task = int(input('Введите номер задачи: '))


def guessNum(my_file):
    temp = None
    file = open(my_file, 'r')
    n = int(file.readline())
    right = set(range(1, n + 1))
    for line in file:
        if "YES" in line:
            right &= temp
        elif "NO" in line:
            right -= temp
        elif "HELP" not in line:
            temp = set(map(int, line.split()))
    return ' '.join(map(str, sorted(right)))


def findLang(my_file):
    file = open(my_file, 'r')
    n = int(file.readline())
    array_i = []
    for i in range(0, n):
        m = int(file.readline())
        array_j = set(map(lambda s: s[:-1], (file.readline() for j in range(0, m))))
        array_i.append(array_j)
    print(array_i)
    union_lang = set.intersection(* array_i)
    all_lang = set.union(* array_i)
    return len(union_lang), sorted(union_lang), len(all_lang), sorted(all_lang)


def latinDict(my_file):
    file = open(my_file, 'r')
    n = file.readline()
    my_dict = {}
    for line in file:
        words = line.strip().split(' - ')
        eng = words[0]
        latin = words[1].split(', ')
        for key in latin:
            if key in my_dict:
                my_dict[key].append(eng)
            else:
                my_dict[key] = [eng]
    for key in my_dict:
        my_dict[key].sort()
    print(str(len(my_dict)))
    for latin in sorted(my_dict):
        print(latin, ' - ', ', '.join(my_dict[latin]))


def supercomputer(my_file):
    file = open(my_file, 'r')
    my_dict = {}
    n = file.readline()
    for i in range(int(n)):
        name, *operations = str(file.readline()).split()
        my_dict[name] = operations
    n = file.readline()
    for i in range(int(n)):
        operation, name = str(file.readline()).split()
        if operation == 'read':
            if 'R' in my_dict[name]:
                print('OK')
            else:
                print('Access denied')
        elif operation == 'write':
            if 'W' in my_dict[name]:
                print('OK')
            else:
                print('Access denied')
        elif operation == 'execute':
            if 'X' in my_dict[name]:
                print('OK')
            else:
                print('Access denied')


def myTask(i):
    if i == 1:
        return guessNum(str(input('Введите название теста.txt: ')))
    elif i == 2:
        return findLang(str(input('Введите название теста.txt: ')))
    elif i == 3:
        return latinDict(str(input('Введите название теста.txt: ')))
    elif i == 4:
        return supercomputer(str(input('Введите название теста.txt: ')))


print(myTask(my_num_task))
