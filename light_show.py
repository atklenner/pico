from machine import Pin, ADC
import time

led1 = Pin(0, Pin.OUT)
led2 = Pin(1, Pin.OUT)
led3 = Pin(2, Pin.OUT)
dial = ADC(28)
half_time = Pin(14, Pin.IN, Pin.PULL_DOWN)

# converts ADC output to how long a beat is in seconds
def bpm_conversion(value):
    bpm = 220 * (value / 65535) + 30
    if half_time.value() == 1:
        return 120 / bpm
    else:
        return 60 / bpm

# 4ppqn
def delay_time():
    # running this line four times to improve responsiveness
    time.sleep(bpm_conversion(dial.read_u16()) / 4)
    time.sleep(bpm_conversion(dial.read_u16()) / 4)
    time.sleep(bpm_conversion(dial.read_u16()) / 4)
    time.sleep(bpm_conversion(dial.read_u16()) / 4)

# Next I need to put 10 pins into an array and stop copy-pasting
while True:
    led1.value(1)
    delay_time()
    led1.value(0)
    led2.value(1)
    delay_time()
    led2.value(0)
    led3.value(1)
    delay_time()
    led3.value(0)

