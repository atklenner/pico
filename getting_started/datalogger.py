import machine
import time

temp_sensor = machine.ADC(machine.ADC.CORE_TEMP)

conversion_factor = 3.3 / 65535

file = open("temps.txt", "w")

while True:
    reading = temp_sensor.read_u16() * conversion_factor
    temp = 27 - (reading - 0.706) / 0.001721
    file.write(str(temp) + "\n")
    file.flush()
    time.sleep(2)
