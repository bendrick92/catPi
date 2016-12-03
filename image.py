class Image(object):

    def __init__(self):
        self.file_name = ''

    def serialize_to_json_string(self):
        return '{"file_name": "' + self.file_name + '"}'