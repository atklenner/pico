import machine
import time

pot = machine.ADC(28)
led = machine.PWM(machine.Pin(15))
led.freq(1000)
conversion_factor = 3.3 / 65535

while True:
    led.duty_u16(pot.read_u16())
    
