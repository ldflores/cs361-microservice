import time
import os
import random

startTime = os.path.getmtime('random-number.txt')

## Should change depending on the number of teams.
NUM_TEAMS = 20 

print('Generate Random Initialized...')

while True: 
    if os.path.getmtime('random-number.txt') > startTime:
        with open('random-number.txt', 'r+') as f:
            if (f.readline() == 'run'):
                f.seek(0)
                f.truncate(0)
                value = str(random.randint(1, NUM_TEAMS))
                f.write(value)
                print(f'Succesfully wrote value: {value}') 
        startTime = os.path.getmtime('random-number.txt')
        break

    time.sleep(10)

        
