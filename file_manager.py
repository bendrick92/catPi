import glob
import os
from local_file import LocalFile


class FileManager(object):

    logs_dir = 'logs/'
    imgs_dir = 'imgs/'
    vids_dir = 'vids/'

    def get_logs_as_bytes(self):
        logs_as_bytes = []
        logs = glob.glob(self.logs_dir + '*.log')
        for log in logs:
            file_name = os.path.basename(log)
            with open(self.logs_dir + file_name, 'rb') as log_file:
                file_data = log_file.read()
                logs_as_bytes.append(file_data)
        return logs_as_bytes

    def get_imgs_as_bytes(self):
        imgs_as_bytes = []
        imgs = glob.glob(self.imgs_dir + '*.jpg')
        for img in imgs:
            file_name = os.path.basename(img)
            with open(self.imgs_dir + file_name, 'rb') as img_file:
                file_data = img_file.read()
                imgs_as_bytes.append(file_data)
        return imgs_as_bytes

    def get_logs_as_local_files(self):
        files = []
        logs = glob.glob(self.logs_dir + '*.log')
        for log in logs:
            file_name = os.path.basename(log)
            file_data = ''
            with open(self.logs_dir + file_name, 'rb') as log_file:
                file_data = log_file.read()
            new_file = LocalFile()
            new_file.file_name = file_name
            new_file.data = file_data
            files.append(new_file)
        return files
            
    def get_imgs_as_local_files(self):
        files = []
        imgs = glob.glob(self.imgs_dir + '*.jpg')
        for img in imgs:
            file_name = os.path.basename(img)
            file_data = ''
            with open(self.imgs_dir + file_name, 'rb') as img_file:
                file_data = img_file.read()
            new_file = LocalFile()
            new_file.file_name = file_name
            new_file.data = file_data
            files.append(new_file)
        return files