# div.d-flex > div.width-full --> OneInfo
# div.mb-1 > h3 > a --> project name and link
# div.width-full > p --> descr
# div.f6 > span.mr-3:nth-child(2) --> language
# relative-time -> time

from selenium import webdriver
import time
import csv
import os

url_discover = 'https://github.com/discover?utf8=%E2%9C%93&recommendations_after='
info_list = []



def StartChrome():
    driver = webdriver.Chrome()
    driver.start_client()
    return driver

def findinfo():
    cars_sel = 'div.d-flex > div.width-full'

    cars = driver.find_elements_by_css_selector(cars_sel)

    for car in cars:
        project_sel = 'div.mb-1 > h3 > a '
        link = car.find_element_by_css_selector(project_sel).get_attribute('href')

        projectname = link.replace('https://github.com/', '')


        descr_sel = 'div.width-full > p'
        try:
            descr = car.find_element_by_css_selector(descr_sel).text
        except:
            descr = 'NoDescr'

        language_sel = 'div.f6 > span.mr-3:nth-child(2)'
        try:
            language = car.find_element_by_css_selector(language_sel).text
        except:
            language = 'Unknow language'

        relativetime_sel = 'relative-time'

        relativetime = car.find_element_by_css_selector(relativetime_sel).get_attribute('title')

        print(projectname)
        print(link)
        print(descr)
        print(language)
        print(relativetime)

        info_list.append([projectname,link,descr,language,relativetime])

def getNextPage():
    global after
    after += 20
    url = url_discover + str(after)
    return url

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

def run(url, filename, maxcount):
    if after > maxcount:
        driver.quit()
    else:
        driver.get(url)
        time.sleep(3)
        findinfo()
        savetocsv(info_list, filename)
        info_list.clear()
        nextpage = getNextPage()
        run(nextpage, filename, maxcount)


after = 0
after_url = url_discover + str(after)
driver = StartChrome()
driver.get(after_url)
input()
run(after_url,'GitDisCover',200)

