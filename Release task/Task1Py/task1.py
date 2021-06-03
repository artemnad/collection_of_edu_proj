import math
import random

my_num_task = int(input('Введите номер задачи: '))


def makeTime(minutes):
    hour = minutes // 60
    minutes = minutes - hour * 60
    return hour, minutes


def moveChess(figure, cagex1, cagey1, cagex2, cagey2):
    switch = {
        1: lambda: bool(cagex1 == cagex2 or cagey1 == cagey2),
        2: lambda: bool((cagex1 - cagex2 == 1 or cagex1 - cagex2 == -1 or cagex1 - cagex2 == 0)
                        and (cagey1 - cagey2 == 1 or cagey1 - cagey2 == -1 or cagey1 - cagey2 == 0)),
        3: lambda: bool(abs(cagex1 - cagex2) == abs(cagey1 - cagey2)),
        4: lambda: bool(abs(cagex1 - cagex2) <= 1 and abs(cagey1 - cagey2) or cagex1 == cagex2 or cagey1 == cagey2),
        5: lambda: bool(((cagex1 - 1 == cagex2 or cagex1 + 1 == cagex2)
                         and (cagey1 - 2 == cagey2 or cagey1 + 2 == cagey2))
                        or ((cagex1 - 2 == cagex2 or cagex1 + 2 == cagex2)
                            and (cagey1 - 1 == cagey2 or cagey1 + 1 == cagey2)))
    }
    if switch.get(figure) == 1:
        return 'YES'
    else:
        return 'NO'


def moveSnail(h, a, b):
    return math.ceil(h / (a - b))


def makeWatch(option, h, m, s, alphaZ):
    switch = {
        1: lambda: ("%.3f" % (30 * h + m / 2 + s / 120)),
        2: lambda: ((alphaZ * 12) % 360),
        3: lambda: (int(alphaZ // 30), int((alphaZ - (alphaZ // 30) * 30) // 0.5),
                    int((alphaZ - ((alphaZ // 30) * 30 + ((alphaZ - (alphaZ // 30) * 30) // 0.5) * 0.5)) // (1 / 120))),
    }
    return switch.get(option)


def findFact(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact


def moveLadder(n):
    for i in range(n):
        for j in range(1, i + 2):
            print(j, end='')
        print()
    return 'END'


def findCard(n):
    this_number = random.randint(1, n - 1)
    for i in range(1, n + 1):
        if i == this_number:
            continue
        print(i)
    return 'missing: ', this_number


def myTask(i):
    if i == 1:
        return makeTime(int(input('Введите минуты: '))),
    elif i == 2:
        return moveChess(int(input('Введите номер подзадания: ')), int(input('Введите параметр X1: ')),
                         int(input('Введите параметр Y1: ')), int(input('Введите параметр X2: ')),
                         int(input('Введите параметр Y2: '))),
    elif i == 3:
        return moveSnail(int(input('Введите высоту H: ')), int(input('Введите подъем за день A: ')),
                         int(input('Введите спуск за ночь B: '))),
    elif i == 4:
        return makeWatch(int(input('Введите номер подзадания: ')), int(input('Введите параметр h (если надо): ')),
                         int(input('Введите параметр m (если надо): ')), int(input('Введите параметр s (если надо): ')),
                         int(input('Введите угол alpha (если надо): '))),
    elif i == 5:
        return findFact(int(input('Введите n: '))),
    elif i == 6:
        return moveLadder(int(input('Введите n: '))),
    elif i == 7:
        return findCard(int(input('Введите n: '))),


print(myTask(my_num_task))
