from machine import Pin, ADC
from random import randint
from time import sleep

# initialize all pins
NUMBER_OF_LEDS = 10
leds = []
for i in range(NUMBER_OF_LEDS):
    leds.append(Pin(i, Pin.OUT))

dial = ADC(28)
half_time = Pin(14, Pin.IN, Pin.PULL_DOWN)
reset_button = Pin(13, Pin.IN, Pin.PULL_DOWN)
current_pin = 0
reverse = False

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
    sleep(bpm_conversion(dial.read_u16()) / 4)
    sleep(bpm_conversion(dial.read_u16()) / 4)
    sleep(bpm_conversion(dial.read_u16()) / 4)
    sleep(bpm_conversion(dial.read_u16()) / 4)

# go though each LED from 0 to 9
def forward_sequence():
    global current_pin
    leds[current_pin].value(1)
    delay_time()
    leds[current_pin].value(0)
    if current_pin == NUMBER_OF_LEDS - 1:
        current_pin = 0
    else:
        current_pin += 1
    
# go through each LED 0 through 9 then back to 1
def knight_rider():
    for led in leds:
        led.value(1)
        delay_time()
        led.value(0)
    for i in range(8, 0, -1):
        leds[i].value(1)
        delay_time()
        leds[i].value(0)
   
# randomly select LEDs
def random_sequence():
    rand = randint(0, NUMBER_OF_LEDS - 1)
    leds[rand].value(1)
    delay_time()
    leds[rand].value(0)

while True:
    forward_sequence()





