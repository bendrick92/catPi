from datetime import datetime
from servo_manager import ServoManager
from camera_manager import CameraManager
from image import Image


class Event(object):

    def __init__(self):
        self.id = 0
        self.feed_amount = 0
        self.event_time = ''
        self.has_run = 'false'
        self.images = []
        self.servo_man = ServoManager()
        self.camera_man = CameraManager()

    def add_image(self, image):
        self.images.append(image)

    def clear_images(self):
        self.images = []

    def try_execute(self):
        if self.has_run == 'false' and self.event_time <= datetime.now():
            self.execute()
        self.servo_man.cleanup()    # Cleanup even if servo is not activated

    def execute(self):
        try:
            #self.servo_man.run()
            image_file_names = self.camera_man.take_picture_series(3)
            self.clear_images()
            for image_file_name in image_file_names:
                image = Image()
                image.file_name = image_file_name
                self.add_image(image)
            self.has_run = 'true'
        except:
            self.clear_images()
            self.has_run = 'false'

    def serialize_to_json_string(self):
        json_string = '{"event_time": "' + self.event_time.strftime('%Y-%m-%dT%H:%M:%S.%fZ') + '", "id": "' + str(self.id) + '", "feed_amount": "' + str(self.feed_amount) + '", "has_run": "' + str(self.has_run) + '", "images": ['
        for index, image in enumerate(self.images):
            json_string += image.serialize_to_json_string()
            if index != len(self.images) - 1:
                json_string += ', '
        json_string += ']}'
        return str(json_string)