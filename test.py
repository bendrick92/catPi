import json
from datetime import datetime

current_timestamp = datetime.now()
print('Task begun at ' + str(current_timestamp))

with open('schedule.json') as schedule_file:
    schedule_data = json.load(schedule_file)
    schedule_file.close()

for i in schedule_data['events']:
    id = i['id']
    feed_amount = i['feed_amount']
    event_time = datetime.strptime(i['event_time'], '%Y-%m-%dT%H:%M:%S.%fZ')
    has_run = i['has_run']

    print('Evaluating event ' + id + '...')
    if has_run == 'false' and event_time <= current_timestamp:
        print('Executing event ' + id + '...')
        try:
            # TODO: Run event 
            i['has_run'] = 'true'
            print('Event ' + id + ' executed successfully!')
        except:
            print('An error occurred - Skipping event ' + id + '...')
    else:
        skip_message = 'Skipping event ' + id + ' - '
        if has_run == 'true':
            skip_message += 'Has already been run!'
        elif event_time > current_timestamp:
            skip_message += 'Set to run at ' + str(event_time)

        print(skip_message)

print('EOF reached')
print('Writing changes...')

try:
    with open('schedule.json', 'w+') as schedule_file:
        schedule_file.write(json.dumps(schedule_data))
        schedule_file.close()

    print('Changes written to file successfully!')
except:
    print('An error occurred - Changes not written to file')
