# Because pygame is a PITA
import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

import pygame
import requests
import RPi.GPIO as GPIO
import threading
import time

from alarm import Alarm

button_pin = 4
led_pin = 17
music_file = "fanfare.mp3"
endpoint_url = "http://localhost:8000/endpoint"
check_interval = 10

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led_pin, GPIO.OUT)


def get_message_id():
    res = requests.get(endpoint_url)
    res.raise_for_status()
    return res.json()["value"]


def main():
    pygame.mixer.init()

    alarm = Alarm([led_pin], music_file)
    last_message_id = get_message_id()

    while True:

        time.sleep(check_interval)

        new_message_id = get_message_id()
        if new_message_id != last_message_id:
            print("START ALARM")
            alarm.start()
            last_message_id = new_message_id
            GPIO.add_event_detect(button_pin, GPIO.FALLING)

            while alarm.active:
                if GPIO.event_detected(4):
                    print("STOP ALARM")
                    alarm.stop()

            GPIO.remove_event_detect(button_pin)


if __name__ == "__main__":
    main()
