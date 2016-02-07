import time # for sleep
import RPi.GPIO as GPIO # GPIO python library
from neopixel import * # rpi_ws281x library
from random import randint # generate random integers

# LED strip configuration:
LED_COUNT      = 2       # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)

# GPIO configuration
buttonPin = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
# Intialize the library (must be called once before other functions).
strip.begin()

on_color  = Color(127, 127, 127)
off_color = Color(0, 0, 0)
color_state = False

prev_input = 0
while True:
	input = GPIO.input(buttonPin)
	if ((not prev_input) and input):
		i     = 0
		red   = randint(0, 255)
		green = randint(0, 255)
		blue  = randint(0, 255)
		strip.setPixelColorRGB(i, red, green, blue)
		strip.show()
		print("new color = (" + str(red) + ", " + str(green) + ", " + str(blue) + ")")

	prev_input = input
	time.sleep(0.05)

