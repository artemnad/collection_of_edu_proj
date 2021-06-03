import hashlib
import re
import requests
import os
import glob


my_num_task = int(input('Введите номер задачи: '))


def getCallSchedule():
    url = "http://math.csu.ru/?option=com_content&view=article&id=54&Itemid=64.html"
    resp = requests.get(url)
    data = resp.content.decode("utf-8")
    #print("data -> " + data)
    results = re.findall(r'<p.+</p>', data)
    results = re.findall(r'[а-яА-Я]+|[0-9]+:[0-9]+|[0-9]+', "".join(results))
    for res in results:
        print(res)


def getNews():
    url = "https://lenta.ru/rubrics/russia/moscow.html"
    resp = requests.get(url)
    data = resp.content.decode("utf-8")
    #print("data -> " + data)
    results = re.findall(r'\d{2}:\d{2}.{3,300}</a>', data)
    lastTenNews = " ".join(re.findall(r'[а-яА-Я]+|[0-9]{2}:[0-9]{2}|\d{2} [а-я]{3,9}', "".join(results[0:10])))
    print("last Ten News -> " + lastTenNews)
    paragraph = " ".join(re.findall(r'[а-яА-Я]+', "".join(results[0])))
    print("Paragraph -> " + paragraph)
    url = "https://lenta.ru/info.html"
    resp = requests.get(url)
    data = resp.content.decode("utf-8")
    email = re.findall(r'[a-zA-Z]{1,33}@.{1,33}[.]ru', data)
    print("Contact us -> " + email[0])
    chiefEditor = re.findall(r'[А-Я][а-я]{2,18}[ ][А-Я][а-я]{2,18}[ ][А-Я][а-я]{2,18}', data)
    print("Chief Editor -> " + chiefEditor[0])


def getMD5Hash(this_dir):
    my_txt = os.listdir(this_dir)
    my_txt = re.findall(r'[a-zA-Zа-яА-Я0-9]+[.]txt', " ".join(my_txt))
    #C:/Users/ArtemHardDesk/Desktop/work_buff/
    md5_hash = hashlib.md5()
    digest = ''
    for this_read in my_txt:
        a_file = open(this_dir + this_read, "rb")
        content = a_file.read()
        md5_hash.update(content)
        digest = digest + '\n' + md5_hash.hexdigest()
    return print(digest)


def getAllMD5Hash(this_dir):
    my_list = glob.glob(this_dir + r"/**/*.txt", recursive=True)
    print(my_list)
    # C:/Users/ArtemHardDesk/Desktop/work_buff/
    md5_hash = hashlib.md5()
    digest = ''
    for this_read in my_list:
        a_file = open(this_read, "rb")
        content = a_file.read()
        md5_hash.update(content)
        digest = digest + '\n' + md5_hash.hexdigest()
    return print(digest)


def myTask(i):
    if i == 1:
        return getCallSchedule()
    elif i == 2:
        return getNews()
    elif i == 3:
        my_num_qtask = int(input('Введите номер подзадачи: '))
        if my_num_qtask == 1:
            return getMD5Hash(input('Write cd -> '))
        elif my_num_qtask == 2:
            return getAllMD5Hash(input('Write cd -> '))


myTask(my_num_task)
