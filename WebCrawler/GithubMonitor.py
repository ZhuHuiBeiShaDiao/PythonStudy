import requests
import  webbrowser
import  time

api = 'https://api.github.com/repos/ZhuHuiBeiShaDiao/NewHideDriverEx'
url = 'https://github.com/ZhuHuiBeiShaDiao/NewHideDriverEx'
last_update = '2019-04-07T18:02:11Z'

url_json = requests.get(api).json()
curr_update = url_json['updated_at']
print(curr_update)

while True:
    if not last_update:
        last_update = curr_update
    if last_update < curr_update:
        webbrowser.open(url)
    time.sleep(600)