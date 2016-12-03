import json
from datetime import datetime
from event import Event
from image import Image


class Schedule(object):
    
    def __init__(self):
        self.events = []
            
    def load_events_from_data(self, data):
        if data is not None:
            json_data = json.loads(data)
            for e in json_data['events']:
                event = Event()
                event.id = int(e['id'])
                event.feed_amount = int(e['feed_amount'])
                event.event_time = datetime.strptime(e['event_time'], '%Y-%m-%dT%H:%M:%S.%fZ')
                event.has_run = e['has_run']
                for i in e['images']:
                    image = Image()
                    image.file_name = i['file_name']
                    event.add_image(image)

                self.add_event(event)

    def add_event(self, event):
        self.events.append(event)

    def has_events(self):
        if len(self.events) > 0:
            return True
        else:
            return False

    def serialize_to_json_string(self):
        json_string = '{"events": ['
        for index, event in enumerate(self.events):
            json_string += event.serialize_to_json_string()
            if index != len(self.events) - 1:
                json_string += ', '
        json_string += ']}'
        return str(json_string)

    def serialize_to_bytes(self):
        return str.encode(self.serialize_to_json_string())

    def evaluate_events(self):
        if self.has_events():
            for event in self.events:
                event.try_execute()