from selenium import webdriver
import time

url = 'https://weibo.com/3097328157/HbTGtsFxr?type=comment#_rnd1554812305931'
def StartChrome():
    driver = webdriver.Chrome()
    driver.start_client()
    return driver

def FindInfo(driver):
    sel = 'span > span.line.S_line1 > span > em:nth-child(2)' #firefox
    elems = driver.find_elements_by_css_selector(sel)
    return [int(el.text) for el in elems[1:]]


while True:
    driver = StartChrome()
    driver.get(url)
    time.sleep(5)
    info = FindInfo(driver)

    try:
        forwar,comm,fire = info
    except ValueError:
        continue

    if forwar > 1000:
        print(f'forwar:{forwar}')
        print(f'comment:{comm}')
        print(f'fire:{fire}')
        break

    time.sleep(20)

print('Done')
