import RPi.GPIO as GPIO
import time

# Set the GPIO pin number (using BCM numbering)
BUTTON_PIN = 17  # GPIO17, physical pin 11

# Set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)

# Set up the pin as an input WITHOUT internal pull-up/down (we're using an external one)
GPIO.setup(BUTTON_PIN, GPIO.IN)

print("Press the button. Press Ctrl+C to exit.")

try:
    while True:
        if GPIO.input(BUTTON_PIN) == GPIO.LOW:
            print("pressed")
        time.sleep(0.1)  # debounce delay
except KeyboardInterrupt:
    print("\nExiting cleanly.")
finally:
    GPIO.cleanup()