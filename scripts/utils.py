import requests

from config.helper import config

def getUserinfo(uid):
    try:
        r = requests.get(config()['api']['userinfo'] + str(uid))
        return r.json()
    except:
        pass