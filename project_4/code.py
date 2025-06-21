import machine
import utime

led = machine.PWM(machine.Pin(15))
led.freq(1000)
while True:
    for brightness in range(0, 65535, 100):
        led.duty_u16(brightness)
        utime.sleep_ms(5)
    for brightness in range(65535, 0, -100):
        led.duty_u16(brightness)
        utime.sleep_ms(5)

