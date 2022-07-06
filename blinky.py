import machine
import time

led_external = machine.Pin(15, machine.Pin.OUT)
led_onboard = machine.Pin(25, machine.Pin.OUT)
led_onboard.toggle()
while True:
    led_external.toggle()
    led_onboard.toggle()
    time.sleep(1)

