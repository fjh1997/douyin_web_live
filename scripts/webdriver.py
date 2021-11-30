from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.proxy import Proxy, ProxyType

from config.helper import config

def go(url):
    chrome_options = Options()
    chrome_options.add_argument('--proxy-server=%s' % config()['webdriver']['proxy'])
    # chrome_options.add_argument('--headless')
    chrome_options.add_experimental_option('detach', True)

    proxy = Proxy()
    proxy.proxy_type = ProxyType.MANUAL
    proxy.http_proxy = config()['webdriver']['proxy']
    proxy.ssl_proxy = config()['webdriver']['proxy']

    capabilities = DesiredCapabilities.CHROME
    proxy.add_to_capabilities(capabilities)

    driver = webdriver.Chrome(options=chrome_options, desired_capabilities=capabilities, executable_path=config()['webdriver']['bin'])

    driver.get(url)
