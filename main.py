import sys
from urllib.parse import urlparse

from scripts import watcher, webdriver
from config.helper import config

if __name__ == '__main__':
    if len(sys.argv) == 1 or not urlparse(sys.argv[1]).scheme:
        print('Invalid url provided, please check...')
        sys.exit(1)

    webdriver.go(sys.argv[1])

    w = watcher.Watcher(directory=config()['watchdog']['dir'])
    w.run()
