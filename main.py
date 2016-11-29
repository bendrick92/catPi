from catpi import CatPi
import time


catpi = CatPi()

while True:
    catpi.run('schedule.json')
    time.sleep(300) # Wait 5 minutes