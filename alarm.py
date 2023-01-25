import threading
import time
import pygame

import RPi.GPIO as GPIO

class Alarm:
    def __init__(self, led_pins, music):
        self.led_pins = led_pins
        self.music = music
        self.active = False
        pygame.mixer.music.load(self.music)

    def _raise_alarm(self):
        for pin in self.led_pins:
            GPIO.output(pin, 1)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(0.01)
        self.stop()

    def start(self):
        self.active = True
        t_alarm = threading.Thread(target=self._raise_alarm, daemon=True)
        t_alarm.start()

    def stop(self):
        self.active = False
        for pin in self.led_pins:
            GPIO.output(pin, 0)
        pygame.mixer.music.stop()
