from machine import Pin, PWM
import time

buzz = PWM(Pin(21))
lol = PWM(Pin(22))

buzz.duty(0)
lol.duty(0)

IR = Pin(19, Pin.IN)

A = Pin(32, Pin.IN, Pin.PULL_UP)
B = Pin(33, Pin.IN, Pin.PULL_UP)
C = Pin(25, Pin.IN, Pin.PULL_UP)
D = Pin(26, Pin.IN, Pin.PULL_UP)

mode_switch = Pin(27, Pin.IN, Pin.PULL_UP)

while True:

    if A.value() == 0:
        if mode_switch.value() == 0 and IR.value() == 0:
            freq = 400
            led_level = 300
        elif mode_switch.value() == 0 and IR.value() == 1:
            freq = 200
            led_level = 300
        else:
            freq = 260
            led_level = 300

        buzz.freq(freq)
        buzz.duty(512)
        lol.duty(led_level)

    elif B.value() == 0:
        if mode_switch.value() == 0 and IR.value() == 0:
            freq = 500
            led_level = 400
        elif mode_switch.value() == 0 and IR.value() == 1:
            freq = 250
            led_level = 400
        else:
            freq = 330
            led_level = 400

        buzz.freq(freq)
        buzz.duty(512)
        lol.duty(led_level)

    elif C.value() == 0:
        if mode_switch.value() == 0 and IR.value() == 0:
            freq = 600
            led_level = 600
        elif mode_switch.value() == 0 and IR.value() == 1:
            freq = 300
            led_level = 600
        else:
            freq = 390
            led_level = 600

        buzz.freq(freq)
        buzz.duty(512)
        lol.duty(led_level)

    elif D.value() == 0:
        if mode_switch.value() == 0 and IR.value() == 0:
            freq = 700
            led_level = 800
        elif mode_switch.value() == 0 and IR.value() == 1:
            freq = 350
            led_level = 800
        else:
            freq = 440
            led_level = 800

        buzz.freq(freq)
        buzz.duty(512)
        lol.duty(led_level)

    else:
        buzz.duty(0)
        lol.duty(0)

    time.sleep_ms(20)