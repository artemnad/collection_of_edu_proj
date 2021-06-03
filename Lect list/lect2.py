# форматный вывод
print("%.3f" % 0.9873543)


# функции
gl = 100

def main(a, b, c):
    n = a + b
    m = b + c
    print(n, m)

main(1, 2, 3)

def main2(a, b, c = 5):
    n = a + b
    m = b + c
    print(n, m)
    
    
main2(1, 2)
main2(1, 2, 3)

def main3(a = 1, b = 2, c = 5):
    n = a + b
    m = b + c + gl
    print(n, m)
    
main3(1, 2)
main3(b = 1, a = 2)
main3()


# возвращаемые значения
def mult(a, b):
    return a * b

print(mult(90, 90))

def mult2(a, b, c):
    return [a * b, a * c, b * c]

print(mult2(3, 4, 5))

mult_arr = [mult, mult2]

print(mult_arr[0](90, 90))

m1, m2, m3 = mult2(3, 4, 5)
print(m1, m2, m3)


# массив функций 

def task1():
    print("task1")
    
def task2():
    print("task2")
    
def task3():
    print("task3")
    
tasks_arr = [task1, task2, task3]

n = int(input())
tasks_arr[n - 1]()


# рекурсия
def fact(n):
    if (n == 1) or (n == 0):
        return 1
    return n * fact(n - 1)

print(fact(12))


# словари
a = dict()
a = {}
a = {1: 'spam', 2: 89, 'p': 'pp'}
print(a[1], a[2], a['p'])

print(a.keys())
print(a.values())

for key in a.keys():
    print(key, a[key], sep=': ')
   
key = 2
if key in a.keys():
    print(a[key])
else:
    print("ERROR")
    
a = {1: 'spam', 2: 89, 'p': 'pp', 1: 'spammmm'}
print(a[1])


# множества
a = set()
#print(dir(a))
a.add(123)
a.add(321)
a.add(123)
a.add(321)
a.add(123)
print(a)
b = sorted(list(a))
print(b[0])

c = set()
c.add(123)
c.add(321)
c.add(132)
c.add(213)
c.add(231)
print(c)

print(a.union(c))
print(a.issubset(c))
print(c.difference(a))
print(a.intersection(c))

d = set()
d.add("spam")
d.add(43)
d.add(0)
print(d)

if a == a.intersection(c):
    print("EURIKA!")
    
print(sorted(c))


# эксперименты
def f(p):
    p()
    
def my_print():
    print("spam")
    
f(my_print)
# f(f) ошибка

# print(help({}.pop))
a = {1: 'spam', 2: 89, 'p': 'pp', 3: 90}
print(a)
print(a.pop(4, 90))
print(a)
print(a.popitem())
print(a)
