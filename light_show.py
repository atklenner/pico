from machine import Pin, ADC
import time

led1 = Pin(0, Pin.OUT)
led2 = Pin(1, Pin.OUT)
led3 = Pin(2, Pin.OUT)
dial = ADC(28)
count = 0

def bpm_conversion(value):
    bpm = 220 * (value / 65535) + 30
    return 60 / bpm

def delay_time():
    time.sleep(bpm_conversion(dial.read_u16()))

# Next I need to put 10 pins into an array and stop copy-pasting
while True:
    led1.value(1)
    delay_time()
    led1.value(0)
    led2.value(1)
    time.sleep(bpm_conversion(dial.read_u16()))
    led2.value(0)
    led3.value(1)
    time.sleep(bpm_conversion(dial.read_u16()))
    led3.value(0)
    time.sleep(bpm_conversion(dial.read_u16()))

