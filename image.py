class Image(object):

    img_dir = 'imgs/'

    def __init__(self):
        self.file_name = ''

    def get_file_name(self):
        return self.img_dir + self.file_name

    def serialize_to_json_string(self):
        return '{"file_name": "' + self.get_file_name() + '"}'