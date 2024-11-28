from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
import psutil
import pygame
import time

class BatteryApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.status_label = Label(text="Checking battery status...")
        self.layout.add_widget(self.status_label)

        # Schedule battery check every 60 seconds
        Clock.schedule_interval(self.check_battery, 10)
        return self.layout

    def check_battery(self, *args):
        battery = psutil.sensors_battery()
        percent = battery.percent
        plugged = battery.power_plugged
        status_text = f"Battery at {percent}%. Plugged in: {plugged}"
        self.status_label.text = status_text

        if plugged and percent == 100:
            self.status_label.text = "Battery fully charged! Alarm triggered!"
            # Initialize pygame for alarm
            pygame.mixer.init()
            pygame.mixer.music.load('C:/Users/shiva/OneDrive/Desktop/Python/kcdf.mp3')
            pygame.mixer.music.play()

if __name__ == '__main__':
    BatteryApp().run()
