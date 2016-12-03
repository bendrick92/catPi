#from log_manager import LogManager
from secret_keys import SecretKeys
from dropbox_manager import DropboxManager
from schedule import Schedule
import time
import os
from file_manager import FileManager


class CatPi:

    #log_man = LogManager()

    def __init__(self):
        self.dropbox_man = DropboxManager(SecretKeys.dropbox_access_token)
        self.schedule = Schedule()
        self.file_man = FileManager()

    #@log_man.log_event_decorator('Loading from file', 'INFO')
    def load_json(self, file_name):
        try:
            self.schedule = Schedule()  # To prevent duplication of JSON
            data = self.dropbox_man.download_file_to_data(file_name)
            self.schedule.load_events_from_data(data)
            if self.schedule.has_events():
                return 'Events successfully loaded from JSON!'
            else:
                return 'No events were loaded'
        except Exception as e:
            return 'An error occurred: ' + str(e)

    #@log_man.log_event_decorator('Evaluating events', 'INFO')
    def evaluate_json(self):
        try:
            if self.schedule.has_events():
                self.schedule.evaluate_events()
                return 'Events evaluated successfully!'
            else:
                return 'There were no events to evaluate'
        except Exception as e:
            return 'An error occurred: ' + str(e)

    #@log_man.log_event_decorator('Writing changes to file', 'INFO')
    def save_json(self, file_name):
        try:
            if self.schedule.has_events():
                data = self.schedule.serialize_to_bytes()
                self.dropbox_man.upload_data_to_file(file_name, data)
                return 'Changes were saved successfully!'
        except Exception as e:
            return 'An error occurred: ' + str(e)

    #@log_man.log_event_decorator('Syncing local files to cloud', 'INFO')
    def sync_data(self):
        try:
            #logs = self.file_man.get_logs_as_local_files()
            #for log in logs:
            #    self.dropbox_man.upload_data_to_file(self.file_man.logs_dir + log.file_name, log.data)
            imgs = self.file_man.get_imgs_as_local_files()
            for img in imgs:
                self.dropbox_man.upload_data_to_file(self.file_man.imgs_dir + img.file_name, img.data)
        except Exception as e:
            return 'An error occurred: ' + str(e)


    def run(self, file_name):
        self.load_json(file_name)
        self.evaluate_json()
        self.save_json(file_name)
        self.sync_data()