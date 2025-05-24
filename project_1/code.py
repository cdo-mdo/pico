import machine
import time

led_onboard = machine.Pin(25, machine.Pin.OUT)
led_external = machine.Pin(15, machine.Pin.OUT)

while True:
    led_onboard.value(1)
    led_external.value(0)
    time.sleep(1)
    led_onboard.value(0)
    led_external.value(1)

