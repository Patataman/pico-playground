#ESP8266 commands: https://www.itead.cc/wiki/ESP8266_Serial_WIFI_Module
from machine import Pin, UART
import utime
import _thread

led = Pin(25, Pin.OUT)
led.value(0)
uart = UART(0, baudrate=115200, tx=Pin(0), rx=Pin(1))

def rcv_uart():
    while True:
        rxData=str(uart.read(1).decode("utf-8"))
        print(rxData, end='')

_thread.start_new_thread(rcv_uart, ())

while True:
    send = input('$> ')
    uart.write(send+'\r\n')