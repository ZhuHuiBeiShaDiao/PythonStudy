# https://weibo.com/oldhei?is_all=1

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
import os

def StartChrome():
    driver = webdriver.Chrome()
    driver.start_client()
    return driver

def send_down():
    page = driver.find_element_by_tag_name('html')

    for i in range(15):
        page.send_keys(Keys.END)
        time.sleep(0.6)

def findNextPage():
    next_sel = 'a.page.next'
    next_page = driver.find_elements_by_css_selector(next_sel)

    if next_page:
        return next_page[0].get_attribute('href')

def findAllPageInfo():
    car_sel = 'div.WB_feed_detail'
    cars = driver.find_elements_by_css_selector(car_sel)

    info_list = []

    for car in cars:
        content_sel = 'div.WB_text.W_f14'
        time_sel = 'div.WB_from.S_txt2'
        link_sel = 'div.WB_from.S_txt2 > a:nth-child(1)'

        content = car.find_element_by_css_selector(content_sel).text
        time = car.find_element_by_css_selector(time_sel).text
        link = car.find_element_by_css_selector(link_sel).get_attribute('href')

        print(content)
        print(time)
        print(link)
        info_list.append([content,time,link])

    return info_list

# csv - utf8
def savetocsv(info_list,name):
    full_path = './' + name + '.csv'

    if os.path.exists(full_path):
        with open(full_path, 'a',encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(info_list)
            print('Done')
    else:
        with open(full_path, 'w+',encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(info_list)
            print('Done')

def run(base, name):
    driver.get(base)
    time.sleep(2)
    send_down()
    time.sleep(2)
    info_list = findAllPageInfo()
    savetocsv(info_list,name)
    next_page = findNextPage()
    if next_page:
        run(next_page,name)
    else:
        driver.quit()

base = 'https://weibo.com/oldhei?is_all=1'
driver = StartChrome()
input()
run(base, 'oldhei')
