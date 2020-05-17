##Timer for sprinklers
import time

mintt=input("How many seconds do you want to time?:")
timer=int(mintt)
while(timer != 0 ):
 timer=timer-1
 time.sleep(1)
 print(timer)
