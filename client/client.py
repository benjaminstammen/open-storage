from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import time

class Watcher:
    DIRECTORY_TO_WATCH = "/home/benjamin/Documents"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(
            event_handler,
            self.DIRECTORY_TO_WATCH,
            recursive=True,
        )
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Error")
            raise
        
        self.observer.join()

class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None
        elif event.event_type == 'created':
            print(f"Received created event - {event.src_path}")
        elif event.event_type == 'modified':
            print(f"Received modified event - {event.src_path}")

if __name__ == '__main__':
    w = Watcher()
    w.run()
