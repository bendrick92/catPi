from catpi import CatPi
import time


while True:
    catpi = CatPi()
    catpi.run('schedule.json')
    time.sleep(300) # Wait 5 minutes