import sys
import threading
from urllib.parse import urlparse

from scripts import watcher, webdriver

if __name__ == '__main__':
    if len(sys.argv) == 1 or not urlparse(sys.argv[1]).scheme:
        print('Invalid url provided, please check...')
        sys.exit(1)

    t = threading.Thread(target=webdriver.go, args=(sys.argv[1],))
    t.start()

    w = watcher.Watcher(directory=config()['watchdog']['dir'])
    w.run()
    
