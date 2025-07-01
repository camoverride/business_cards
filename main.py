import RPi.GPIO as GPIO
import os
import time
import random



# Set the GPIO pin number (using BCM numbering)
BUTTON_PIN = 17  # GPIO17, physical pin 11

# Delay between allowed button presses (seconds)
DELAY = 10

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN)

# Text to be displayed on the card
TEXT = """
CAM SMITH
email : camoverride@gmail.com
IG    : camoverride
web   : https://smith.cam
"""

# Picture to be displayed on the card.
PICS = [
    "pics/cam1.png",
    "pics/cam2.jpg",
    "pics/cam3.jpg",
    "pics/cam4.jpg",
    "pics/cam5.jpg",
    "pics/cam6.jpg",
    "pics/cam7.jpg",
]

last_press_time = 0

try:
    while True:
        if GPIO.input(BUTTON_PIN) == GPIO.LOW:
            now = time.time()
            if now - last_press_time > DELAY:
                print("Pressed!")

                # Print the text
                os.system(f"sudo sh -c 'echo \"{TEXT}\" > /dev/usb/lp0'")

                # Print the image
                pic_path = random.choice(PICS)
                os.system(f"lp -d face_printer {pic_path}")

                last_press_time = now

        # Check every 50 ms
        time.sleep(0.05)

except KeyboardInterrupt:
    print("Exiting")

finally:
    GPIO.cleanup()
