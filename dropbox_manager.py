import dropbox
import datetime


class DropboxManager:

    def __init__(self, access_token):
        self.dbx = dropbox.Dropbox(access_token)

    def download_file_to_data(self, file_name):
        try:
            md, res = self.dbx.files_download('/' + file_name)
            return res.content
        except dropbox.exceptions.ApiError as e:
            # TODO: Print errors to log
            return None

    def upload_data_to_file(self, file_name, data):
        try:
            write_mode = dropbox.files.WriteMode.overwrite
            modified_date = datetime.datetime.now()
            res = self.dbx.files_upload(data, '/' + file_name, write_mode, client_modified=modified_date, mute=True)
            return res
        except dropbox.exceptions.ApiError as e:
            # TODO: Print errors to log
            return None