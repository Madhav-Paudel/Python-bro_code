import time
import winsound
def counter(end,start=0):
    # frequency is set to 500Hz
    freq = 500
    # duration is set to 100 milliseconds             
    dur = 999
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("Time up!")
    winsound.Beep(freq, dur)

counter(5)
