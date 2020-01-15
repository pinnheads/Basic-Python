#to check if the current minute is odd or not
from datetime import datetime
import time
import random
odds = []
for i in range(0,60):
    if(i%2!=0):
        odds.append(i)
for k in range(5):
    right_this_minute = datetime.today().minute
    wait_time = random.randint(0,60)
    if right_this_minute in odds:
        print("This minute seems a little odd.")
    else: 
        print("Not an odd minute.")
    time.sleep(wait_time)