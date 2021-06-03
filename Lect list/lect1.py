# работа с числами 
a = 76597754679834738957032849083240897325893470965439807589437598436
b = 7878
# print(a ** b)
print(a + b)
print(a / b)
print(a // b)
print(a % b)
print(a ^ b) # xor


# if, elif, else
a = int(input())
if (8 < a < 100):
    print("100")
elif (a < 1000):
    if (a > 234):
        print("234")
    else:
        print("123")
else:
    print("PYTHON")


# for, range
a = range(-5, 10, 3)
a = ['Spam', 'Ham', 123, [56, 90]]
# a = 'spam'
for i in range(len(a)):
    print(i, ':', a[i])


# while
a = 5
while(a > 0):
    print(a)
    a = a - 1 # a -= 1


# массивы
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(arr)
# срезы
print(arr[2:5])
print(arr[3:])
print(arr[:7])
print(arr[::-1]) # в обратном порядке
print(arr[0], arr[len(arr)-1], sep=', ')
print(arr[-1], arr[-10])


# вложенные массивы
a = []
for i in range(10):
    b = []
    for j in range(10):
        b.append(j)
    a.append(b)
print(a[0][-1])


# работа с массивами
a = ['0', '1', '2', '3']
a = [int(i) for i in a]
print(a[1] + a[3])

b = ['0', '1', '2', '3']
print(" spam ".join(b))

b = ['0', '1', '988', '2', '3', '10']
print(sorted(b))

b = [0, 1, 988, 2, 3, 10]
print(sorted(b))


# работа со строками
a = "Hello, World!"
print(a.replace('l', 'L'))
# вывод всех доступных методов
# print(dir(a))

print(a.find('ld'))

print(a.split(', '))

print(a.count('l'))

print(a[::-1])

print(ord(a[0]), chr(1055)) # код символа и символ по коду


# пример
a = "A wiki is run using wiki software, otherwise known as a wiki engine. A wiki engine is a type of content management system, but it differs from most other such systems, including blog software, in that the content is created without any defined owner or leader, and wikis have little inherent structure, allowing structure to emerge according to the needs of the users. There are dozens of different wiki engines in use, both standalone and part of other software, such as bug tracking systems. Some wiki engines are open source, whereas others are proprietary. Some permit control over different functions (levels of access); for example, editing rights may permit changing, adding, or removing material. Others may permit access without enforcing access control. Other rules may be imposed to organize content.".lower()
points =",.?!:;()-"
for point in points:
    a = a.replace(point, '')
print(a.split(' '))
