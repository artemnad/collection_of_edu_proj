my_num_task = int(input('Введите номер задачи: '))


def splitString(my_string):
    return my_string[len(my_string) // 2 + len(my_string) % 2:] + my_string[:len(my_string) // 2 + len(my_string) % 2]


def searchCoincid(my_string):
    my_string = list(my_string)
    my_index = []
    for i in range(0, len(my_string)):
        if my_string[i] == 'f':
            my_index.append(i)
    if len(my_index) >= 2:
        return my_index[0], my_index[-1]
    elif len(my_index) == 1:
        return my_index[0]
    else:
        return


def outputPairs(list_numbers):
    list_numbers = list(map(int, list_numbers[:-2].split(' ')))
    for i in range(1, len(list_numbers)):
        if list_numbers[i - 1] * list_numbers[i] > 0:
            return list_numbers[i - 1], list_numbers[i]


def outputList(option, my_list):
    index = 0
    if option == 1:
        one = my_list
        for i in range(1, len(one)):
            if one[i - 1] != one[i]:
                index += 1
        return index
    if option == 2:
        max_num = int(my_list[0])
        for i in range(1, len(my_list)):
            n = int(my_list[i])
            if n > max_num:
                index = i
        return max_num, index
    if option == 3:
        this_list = []
        for i in range(0, len(my_list)):
            if my_list.count(i) == 1:
                this_list.append(i)
        return this_list


def findIndex(n, m):
    matrix = [[0 for j in range(m)] for i in range(n)]
    for i in range(0, n):
        for j in range(0, m):
            matrix[i][j] = int(input('Введите значение [i][j] ячейки: '))
    for i in range(0, n):
        for j in range(0, m):
            if matrix[i][j] == max(matrix):
                return i, j


def makeStar(n):
    star = [["."] * n for i in range(n)]
    for i in range(n):
        star[i][i] = "*"
        star[n - 1 - i][i] = "*"
        star[i][n // 2] = "*"
        star[n // 2][i] = "*"
    return '\n'.join([' '.join([str(i) for i in row]) for row in star])


def fib(n, a=0, b=1):
    if n == 0:
        return a
    else:
        return fib(n - 1, a + b, a)


def reverseSequence(n):
    if len(n) != 0:
        n = n[::-1]
        print(n[0])
        n = n[1:]
        n = n[::-1]
        return reverseSequence(n)
    return


def myTask(i):
    if i == 1:
        return splitString(str(input('Введите строку: '))),
    elif i == 2:
        return searchCoincid(str(input('Введите строку: '))),
    elif i == 3:
        return outputPairs(str(input('Введите список чисел: '))),
    elif i == 4:
        return outputList(int(input('Введите подзадание: ')), list(input('Введите список: '))),
    elif i == 5:
        return findIndex(int(input('Введите размер n: ')), int(input('Введите размер m: '))),
    elif i == 6:
        return makeStar(int(input('Введите число n: '))),
    elif i == 7:
        return fib(int(input('Введите число n: '))),
    elif i == 8:
        return reverseSequence(str(input('Введите последовательность: '))),


print(myTask(my_num_task))
