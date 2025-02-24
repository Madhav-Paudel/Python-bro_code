# Alarm clock 
import pygame
import datetime
import time

def set_time(alarm_clock):
    print(f"Alarm Set for {alarm_clock}")
    sound_file = "music.mp4"
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        if current_time == alarm_clock:
            print("WAKE UP!")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)

            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)
                
            is_running = False

        time.sleep(1)



if __name__=="__main__":
    alarm_clock=input("Enter the alarm time (HH:MM:SS)")
    set_time(alarm_clock)







