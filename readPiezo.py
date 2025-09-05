# https://www.luisllamas.es/en/analog-entries-adc-micropython/
from machine import ADC
import time


piezo = ADC(27)

while True:
    print("0-65535", piezo.read_u16())
    time.sleep(0.1)