import requests
import json

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

from config.helper import config
from store.mongo import MongoStore

def go(url):
    chrome_options = Options()
    chrome_options.add_argument('--proxy-server=%s' % config()['webdriver']['proxy'])
    # chrome_options.add_argument('--headless')

    proxy = Proxy()
    proxy.proxy_type = ProxyType.MANUAL
    proxy.http_proxy = config()['webdriver']['proxy']
    proxy.ssl_proxy = config()['webdriver']['proxy']

    capabilities = DesiredCapabilities.CHROME
    proxy.add_to_capabilities(capabilities)

    with webdriver.Chrome(options=chrome_options,
                            desired_capabilities=capabilities,
                            executable_path=config()['webdriver']['bin']
                            ) as driver:
        wait = WebDriverWait(driver, 10)

        driver.implicitly_wait(24 * 60 * 60)

        driver.get(url)

        first_result = wait.until(presence_of_element_located((By.ID, "RENDER_DATA")))
        json_str = requests.utils.unquote(first_result.get_attribute("textContent"))
        json_obj = json.loads(json_str)

        roomInfo = json_obj['initialState']['roomStore']['roomInfo']

        store = MongoStore()
        store.set_collection('room')
        store.insert_one({
            'roomId': roomInfo['roomId'],
            'web_rid': roomInfo['web_rid'],
            'title': roomInfo['room']['title'],
            'user_count_str': roomInfo['room']['user_count_str'],
            'cover': roomInfo['room']['cover']['url_list'][0],
            'admin_user_ids': roomInfo['room']['admin_user_ids'],
            'owner': roomInfo['room']['owner']
        })

        wait.until(presence_of_element_located((By.CLASS_NAME, "oSu9Aw19")))
        