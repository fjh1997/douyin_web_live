from scripts import watcher, webdriver

if __name__ == '__main__':
    webdriver.lunch()

    w = watcher.Watcher(directory='/Users/geng/douyin_live')
    w.run()
