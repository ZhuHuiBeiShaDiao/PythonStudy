# https://api.github.com/repos/ZhuHuiBeiShaDiao/PythonStudy
# https://api.pushover.net/1/messages.json?token=xxx&user=xxx&message=hello!&title=title!&url=www.baidu.com

import requests
import time
from datetime import datetime

#2019-04-08T13:51:20Z
def getpushinfo():
    url = 'https://api.github.com/repos/ZhuHuiBeiShaDiao/PythonStudy'
    prelastupdatetime = None
    r = requests.get(url).json()
    precurrentdatatime = r['updated_at']
    print(precurrentdatatime)
    while True:
        if not prelastupdatetime:
            prelastupdatetime = precurrentdatatime

        if prelastupdatetime < precurrentdatatime:
            return r

        r = requests.get(url).json()
        precurrentdatatime = r['updated_at']
        time.sleep(10)

def makemsg(data):
    updatetime = data['updated_at']
    url = data['html_url']
    title = data['name']
    temp = 'token={token}&user={user}&message={msg}&title={title}&url={url}'
    query = temp.format(
        token = 'xxxxxxxxxxxxxxxxxxxxx',
        user = 'xxxxxxxxxxxxxxxxxxxxx',
        msg = updatetime,
        title = title,
        url = url
    )
    pushurl = 'https://api.pushover.net/1/messages.json?'
    fullurl = pushurl + query
    return fullurl

def push_it(msg):
    requests.post(msg)
    print('Done')

r = getpushinfo()
msg = makemsg(r)
push_it(msg)


