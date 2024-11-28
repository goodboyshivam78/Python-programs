import psutil
import pygame
import time
import os
import sys
import keyboard

def check_battery():
    # Get battery information
    battery = psutil.sensors_battery()
    # percent = 100
    percent = battery.percent
    plugged = battery.power_plugged

    # Initialize pygame mixer
    pygame.mixer.init()

    # Load the song (replace with your file path)
    pygame.mixer.music.load('C:/Users/shiva/OneDrive/Desktop/Python/kcdf.mp3')

    # Check if battery is full and plugged in
    if plugged and percent == 100:
        print("Battery fully charged! Alarm triggered!")
        # Play the song
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            if keyboard.read_event():  # Check if any key is pressed
                print("Key pressed! Stopping the music...")
                pygame.mixer.music.stop()  # Stop the music
                break  # Exit the loop and terminate the program
                #sys.exit()
            time.sleep(1)  # Check every second

        # Alarm sound (for Windows, it can be different for other OS)
        #os.system("echo '\a'")   Triggers a beep sound
    else:
        print(f"Battery at {percent}%. Plugged in: {plugged}")

def main():
    while True:
        check_battery()
        time.sleep(60)  # Check every 60 seconds

if __name__ == "__main__":
    main()
