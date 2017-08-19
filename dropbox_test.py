from secret_keys import SecretKeys
from dropbox_manager import DropboxManager


dropbox_manager = DropboxManager(SecretKeys.dropbox_access_token)
print dropbox_manager.download_file_to_data('schedule.json')