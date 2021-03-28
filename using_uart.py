#ESP8266 commands: https://www.itead.cc/wiki/ESP8266_Serial_WIFI_Module
from machine import Pin, UART
import utime

led = Pin(25, Pin.OUT)
led.value(0)
uart = UART(0, baudrate=115200) #, tx=Pin(0), rx=Pin(1))

# turn on an LED
#https://www.youtube.com/watch?v=02yfpA3h_w8


while True:
    rxData = bytes()

    while uart.any() > 0:
        rxData += uart.read(1)

    if len(rxData):
        led.value(1)
        utime.sleep(0.25)
        led.value(0)
        utime.sleep(0.25)
        led.value(1)
        utime.sleep(0.25)
        led.value(0)
        print(rxData.decode("utf-8"), end="")
        
    var = input("Input: ")
    uart.write(var+"\r\n")
