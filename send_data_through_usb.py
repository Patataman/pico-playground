""" Send data to Windows when a button is pressed
"""

from machine import Pin
import time

LED = Pin(25, Pin.OUT)
DELAY = time.ticks_ms()

def alter_led(inst):
    global LED, DELAY
    
    if time.ticks_diff(time.ticks_ms(), DELAY) < 500:
        return
    
    # print(inst.value)
    LED.toggle()
    # print("Press button works!")
    print("l")
    DELAY = time.ticks_ms()

but = Pin(0, Pin.IN, Pin.PULL_UP)
but.irq(handler=alter_led, trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING)


LED.value(0)
