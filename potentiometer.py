import machine
import time

pot = machine.ADC(28)
conversion_factor = 3.3 / 65535

while True:
    voltage = pot.read_u16() * conversion_factor
    print(voltage)
    time.sleep(0.5)