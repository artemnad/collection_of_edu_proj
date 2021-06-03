# регулярные выражения 

import re

str = "Hello, here is some spam for you2!"

result = re.match("H ello", str)  # ищет с начала строки
if result != None:
    print(result.group(0))
else:
    print("Not found!")

result = re.search("o", str)  # ищет с начала строки
if result != None:
    print(result.group(0))
else:
    print("Not found!")

result = re.findall("o", str)
print(result)

# спецсимволы
# \w - любая цифра или буква
# \s - любой пробельный символ (\S - любой непробельный символ)
# \d - любая цифра от 0 до 9
# . - любой символ
# ? - 0 или 1 вхождение шаблона слева
# + - 1 и более вхождений шалона слева
# * - 0 или более вхождений шалона слева
# ^ - начало строки
# $ - конец строки

result = re.findall(".", str)
# print(result)

# получить массив слов 
result = re.findall("\w+", str)
print(result)

# получить первое и последнее слово
result = re.findall("^\w+", str)
print(result)

result = re.findall("\w+!$", str)
print(result)

# получить первые два символа каждого слова
result = re.findall("\b\w\w", str)
print(result)

# получить домены эл. почты
str2 = "makare95@mail.ru, spam@spam.com, lol@try.org"
result = re.findall("@(\w+\.\w+)", str2)
print(result)

# получить дату из строки
str3 = "84394 01-05-2006 rire 6891568489752156 = = 09-09-1987"
result = re.findall("\d{2}-\d{2}-\d{4}", str3)
print(result)

# получить слова, начинающиеся с гласной
result = re.findall("\b[aeiouyAEIOUY]\w*", str)
print(result)

# получить все телефонные номера
str4 = "8(912)4567891 4i38095 kdfos uoiwertf uewi +7(912)4567891 8(912)4567891"
result = re.findall("\+?[7-8]\(\d{3}\)\d{7}", str4)
print(result)

# разбить строку по нескольким разделителям
str5 = "spam ham; spuam, haum!"
result = re.split("[\s;,u!]", str5)
print(result)

result = re.sub("[\s;,u!]", ' ', str5)
print(result)

str6 = "123456"
result = re.findall("\d{2}", str6)
print(result)

# print(dir(re))
