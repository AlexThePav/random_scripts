from watchdog.events import FileSystemEventHandler
from settings import DESTINATION_CHOICES, FOLDER_TO_TRACK, EXTENSIONS
import os

class DownloadsHandler(FileSystemEventHandler):
    def __init__(self):
        self.folder_to_track = FOLDER_TO_TRACK
        self.destination_choices = DESTINATION_CHOICES
        self.extensions = EXTENSIONS
    
    def move_to_folder(self, destination_folder, filename):
        folder_destination = self.destination_choices[destination_folder]
        src = self.folder_to_track + "/" + filename
        new_destination = folder_destination + "/" + filename
        os.rename(src, new_destination)

    def on_any_event(self, event):
        folder_destination = ""
        for filename in os.listdir(self.folder_to_track):
            if "crdownload" not in os.path.splitext(filename)[1]:
                if os.path.splitext(filename)[1] in self.extensions["pictures"]:
                    self.move_to_folder("pictures", filename)
                elif os.path.splitext(filename)[1] in self.extensions["music"]:
                    self.move_to_folder("music", filename)
                elif os.path.splitext(filename)[1] in self.extensions["videos"]:
                    self.move_to_folder("videos", filename)
                elif os.path.splitext(filename)[1] in self.extensions["documents"]:
                    self.move_to_folder("documents", filename)
                else:
                    pass
            else:
                pass