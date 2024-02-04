from utime import sleep
# We are using https://github.com/blaz-r/pi_pico_neopixel
from neopixel import Neopixel

NUMBER_PIXELS = 64
STATE_MACHINE = 0
LED_PIN = 26

strip = Neopixel(NUMBER_PIXELS, STATE_MACHINE, LED_PIN, "GRB")

# Color RGB values
red = (255, 0, 0)
off = (0,0,0)

delay = .1
while True:
    for i in range(0, NUMBER_PIXELS):
        strip.set_pixel(i, red)
        if i > 0: strip.set_pixel(i-1, off)
        if i == 0: strip.set_pixel(NUMBER_PIXELS-1, off)
        strip.show()
        sleep(delay)
