from watchdog.observers import Observer
from settings import FOLDER_TO_TRACK

from helpers.watchdog_handlers import DownloadsHandler

import json
import time

def run_watch_downloads():
    event_handler = DownloadsHandler()
    observer = Observer()
    observer.schedule(event_handler, FOLDER_TO_TRACK, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()