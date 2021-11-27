from scripts import watcher


if __name__ == '__main__':
    w = watcher.Watcher(directory='/Users/geng/charles/autosaved')
    w.run()