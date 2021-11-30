from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def lunch():
    chrome_options = Options()
    chrome_options.add_argument('--proxy-server=127.0.0.1:8080')
    chrome_options.add_argument('--headless')
    chrome_options.add_experimental_option('detach', True)

    driver = webdriver.Chrome(options=chrome_options)

    driver.get('https://live.douyin.com/515848215303')

