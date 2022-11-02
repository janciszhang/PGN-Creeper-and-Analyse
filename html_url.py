# -*- coding: utf-8 -*-
"""
获取url链接到迅雷批量下载
"""
import requests as rq
from bs4 import BeautifulSoup as bs
import re


def gethtml(rooturl, encoding="utf-8"):
    # 默认解码方式utf-8
    response = rq.get(rooturl)
    response.encoding = encoding
    html = response.text
    return html  # 返回链接的html内容


def getherf(html):
    # 使用BeautifulSoup函数解析传入的html
    soup = bs(html, features="lxml")
    allnode_of_a = soup.find_all("a")
    result = [_.get("href") for _ in allnode_of_a]
    # print(result)
    return result


def filterurl(result):
    # result参数：get到的所有a标签内herf的内容
    # 对列表中每个元素进行筛选
    urls = r"http://(.+)"  # 匹配模式: 所有http://开头的链接
    # urls = [re.match(urlptn, str(_)) for _ in result]  # 正则筛选
    # urls = [_ for _ in result if str(_).endswith('.zip')]
    # print(len(urls))
    # while None in urls:
    #     urls.remove(None)  # 移除表中空元素
    # urls = [_.group() for _ in urls]  # group方法获得re.match()返回值中的字符
    # # print(urls)
    return urls


html = gethtml("https://lms.monash.edu/mod/book/view.php?id=8900010")
result = getherf(html)
# print(result)
urls = filterurl(result)
print(urls)
# f = open("pgn_urls.txt", 'w')
# for i in range(len(urls)):
#     f.write(f"https://www.pgnmentor.com/{urls[i]}\n")
# print(len(urls))
