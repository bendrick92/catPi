import json
from datetime import datetime
from event import Event


class Schedule(object):
    
    def __init__(self):
        self.events = []
            
    def load_events_from_data(self, data):
        if data is not None:
            json_data = json.loads(data)
            for i in json_data['events']:
                event = Event()
                event.id = i['id']
                event.feed_amount = i['feed_amount']
                event.event_time = datetime.strptime(i['event_time'], '%Y-%m-%dT%H:%M:%S.%fZ')
                event.has_run = i['has_run']

                self.add_event(event)

    def add_event(self, event):
        self.events.append(event)

    def has_events(self):
        if len(self.events) > 0:
            return True
        else:
            return False

    def serialize_to_json(self):
        serialized_json = '{"events": ['
        for index, event in enumerate(self.events):
            serialized_json += event.serialize_to_json()
            if index != len(self.events) - 1:
                serialized_json += ', '
        serialized_json += ']}'
        return serialized_json

    def evaluate_events(self):
        if self.has_events():
            for event in self.events:
                event.try_execute()