from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
import os
import time

list_photo = []

def findAllImg(url):
    html_img = urlopen(url)
    imgobj = BeautifulSoup(html_img, 'html.parser')

    imgNum = imgobj.select('div.ptitle > em')[0].text
    currentNum = imgobj.select('div.ptitle > span')[0].text

    nextimg_html = imgobj.select('div.pic-next-img > a')[0].get('href')

    down_img_addr = imgobj.select('div.paper-down > a')[0].get('href')
    down_img_addr = down_img_addr.strip('?down')

    print(imgNum)
    print(currentNum)
    print(nextimg_html)
    print(down_img_addr)

    list_photo.append(down_img_addr)

    if imgNum != currentNum:
        findAllImg(nextimg_html)

def dumpAllPhoto(title):
    path = './' + title
    if not os.path.exists(path):  # 检测是否有image目录没有则创建
        os.makedirs(path)

    for url in list_photo:
        filepath = path + '/' + url[url.rfind('/') + 1:]

        file = urlopen(url)
        fp = open(filepath, 'wb')
        data = file.read()
        print(filepath)
        fp.write(data)
        fp.close()

def findinfo(url, max, curr):

    if not curr < max:
        return

    html = urlopen(url)
    bsobj = BeautifulSoup(html, 'html.parser')

    next_page = bsobj.select('a.next')[0].get('href')
    Objs = bsobj.select('div.list_cont.Left_list_cont > div > div > div > ul > li > a')

    for obj in Objs:
        name = obj.get('title')
        link = obj.get('href')

        print(name)
        print(link)

        findAllImg(link)
        dumpAllPhoto(name)
        list_photo.clear()

    findinfo(next_page, max, curr++)

url_one = 'http://www.win4000.com/wallpaper_0_0_0_1.html'
#
# html = requests.get(url, headers=headers)
#
# bsobj = BeautifulSoup(html, 'html.parser')

findinfo(url_one)