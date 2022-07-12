import machine
import time

pir1 = machine.Pin(28, machine.Pin.IN, machine.Pin.PULL_DOWN)
pir2 = machine.Pin(22, machine.Pin.IN, machine.Pin.PULL_DOWN)
led = machine.Pin(15, machine.Pin.OUT)
piezo = machine.Pin(14, machine.Pin.OUT)

def pir_handler(pin):
    time.sleep_ms(100) # debounce
    if pin.value():
        if pin is pir1:
            print("Alarm! You pressed the first button")
        elif pin is pir2:
            print("Alarm! You pressed the second button")
        for i in range(50):
            led.toggle()
            piezo.toggle()
            time.sleep_ms(100)
        
pir1.irq(trigger=machine.Pin.IRQ_RISING, handler=pir_handler)
pir2.irq(trigger=machine.Pin.IRQ_RISING, handler=pir_handler)

while True:
    led.toggle()
    time.sleep(5)