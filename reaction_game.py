import machine
import time
import random

pressed = False
fastest_button = None
led = machine.Pin(15, machine.Pin.OUT)
button1 = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
button2 = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)

def button_handler(pin):
    global pressed
    if not pressed:
        pressed = True
        global fastest_button
        fastest_button = pin

led.value(1)
time.sleep(random.uniform(5, 10))
led.value(0)

timer_start = time.ticks_ms()

button1.irq(trigger=machine.Pin.IRQ_RISING, handler=button_handler)
button2.irq(trigger=machine.Pin.IRQ_RISING, handler=button_handler)

while fastest_button is None:
    time.sleep(1)

if fastest_button is button1:
    print("Player 1 wins!")
elif fastest_button is button2:
    print("Player 2 wins!")
