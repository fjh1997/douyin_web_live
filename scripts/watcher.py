import time
import concurrent.futures
import queue

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from messages.utils import unpackMsgBin

q = queue.Queue()

class Watcher:
    DIRECTORY_TO_WATCH = ""

    def __init__(self, directory):
        self.observer = Observer()
        self.DIRECTORY_TO_WATCH = directory

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()

        try:
            while True:
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    executor.submit(unpackMsgBin, q.get())
        except:
            self.observer.stop()

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            q.put(event.src_path)

