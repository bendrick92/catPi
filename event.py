from datetime import datetime

class Event(object):

    def __init__(self):
        id = 0
        feed_amount = 0
        event_time = ''
        has_run = 'false'

    def try_execute(self):
        if self.has_run == 'false' and self.event_time <= datetime.now():
            self.execute()

    def execute(self):
        try:
            # TODO: Run event
            self.has_run = 'true'
        except:
            self.has_run = 'false'

    def serialize_to_json(self):
        return '{ "event_time": "' + self.event_time.strftime('%Y-%m-%dT%H:%M:%S.%fZ') + '", "id": "' + str(self.id) + '", "feed_amount": "' + str(self.feed_amount) + '", "has_run": "' + str(self.has_run) + '"}'