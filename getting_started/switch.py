import machine
import time

green_button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
red_button = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_DOWN)
led_green = machine.Pin(15, machine.Pin.OUT)
led_red = machine.Pin(13, machine.Pin.OUT)

while True:
    if green_button.value() == 1:
        led_green.value(1)
        time.sleep(1)
    if red_button.value() == 1:
        led_red.value(0)
        time.sleep(1)
    led_green.value(0)
    led_red.value(1)
