# https://api.github.com/search/repositories?q=hidedriver
# https://api.github.com/search/repositories?q=topic:

import requests


def getname():
    print("input search key")
    key = input()
    return key.split()

def check(names):
    for name in names:
        searchurl = 'https://api.github.com/search/repositories?q='
        resule = requests.get(searchurl + name).json()['items'][0]
        startnum = resule['stargazers_count']
        forknum = resule['forks']
        autoname = resule['owner']['login']

        print('AutorName:' + autoname)
        print('Start:'+ str(startnum))
        print('Fork:' + str(forknum))

        topic = 'https://api.github.com/search/repositories?q=topic:'
        topicresule = requests.get(topic + name).json()
        topicnum = topicresule['total_count']
        print('Topic:' + str(topicnum))

key = getname()
check(key)
