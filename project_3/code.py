import machine
import time

switch_control = machine.Pin(13, machine.Pin.IN)
led_onboard = machine.Pin(25, machine.Pin.OUT)
led_ext = machine.Pin(15, machine.Pin.OUT)

while True:
    if (switch_control.value() == 1):
        led_ext.value(1)
        time.sleep(1)
        led_ext.value(0)
    else:
        led_onboard.value(1)
        time.sleep(1)
        led_value(0)


