from machine import Pin, ADC
import time

leds = []
for i in range(10):
    leds.append(Pin(i, Pin.OUT))

dial = ADC(28)
half_time = Pin(14, Pin.IN, Pin.PULL_DOWN)

# converts ADC output to how long a beat is in seconds
def bpm_conversion(value):
    bpm = 220 * (value / 65535) + 30
    if half_time.value() == 1:
        return 60 / bpm
    else:
        return 30 / bpm

# 4ppqn
def delay_time():
    # running this line four times to improve responsiveness
    time.sleep(bpm_conversion(dial.read_u16()) / 4)
    time.sleep(bpm_conversion(dial.read_u16()) / 4)
    time.sleep(bpm_conversion(dial.read_u16()) / 4)
    time.sleep(bpm_conversion(dial.read_u16()) / 4)

# Next I need to put 10 pins into an array and stop copy-pasting
while True:
    for led in leds:
        led.value(1)
        delay_time()
        led.value(0)

