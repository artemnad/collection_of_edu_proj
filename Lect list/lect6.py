# requests - модуль для генерации http(https)-запросов
import requests
import re

# url = "http://alg.imm.uran.ru/dezagraphs/dezatab.html"
# resp = requests.get(url)
# data = resp.content.decode("utf-8")
# results = re.findall("<li>.*</li>", data)
# for res in results:
    # print(res)
    
# url = "http://alg.imm.uran.ru/dezagraphs/deza.php"
# resp = requests.get(url)
# data = resp.content.decode("utf-8")
# results = re.findall("<td>&nbsp;\d+&nbsp;</td> <td>&nbsp;\d+&nbsp;</td> <td>&nbsp;\d+&nbsp;</td> <td>&nbsp;\d+&nbsp;</td>", data)
# for res in results:
    # res = res.replace("<td>", "")
    # res = res.replace("</td>", "")
    # res = res.replace("&nbsp;", "")
    # v, k, b, a = res.split()
    # params = {"v": v, "k": k, "b": b, "a": a, "form": "txt"}
    # headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    # resp = requests.get(url, params=params, headers=headers)
    # data = resp.content.decode("utf-8")
    # print(v, k, b, a)
    # print(data)
    
url = "https://yandex.ru/news/?clid=9403"
resp = requests.get(url)
data = resp.content.decode("utf-8")
print(data)