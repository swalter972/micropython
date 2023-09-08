from microbit import *
from machine import time_pulse_us

# default pins in Ultrasonic class are:
trigger= pin0
echo= pin0
trigger.write_digital(0)
echo.read_digital()
while True:
    trigger.write_digital(1)
    trigger.write_digital(0)
    msec = time_pulse_us(echo, 1)
    echo_time = msec / 1000000
    dist_cm = (echo_time / 2) * 34300
    display.scroll(str(int(dist_cm)))
    sleep(2000)

        
