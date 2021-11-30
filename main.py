import sys

from scripts import watcher, webdriver

if __name__ == '__main__':
    webdriver.lunch(sys.argv[1])

    w = watcher.Watcher(directory='/Users/geng/douyin_live')
    w.run()
