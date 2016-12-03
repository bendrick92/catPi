from catpi import CatPi
import time


wait_time = 10

while True:
    catpi = CatPi()
    catpi.run('schedule.json')
    time.sleep(wait_time * 60)