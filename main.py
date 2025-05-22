import RPi.GPIO as GPIO
import os
import time
import cv2



# Set the GPIO pin number (using BCM numbering)
BUTTON_PIN = 17  # GPIO17, physical pin 11

# Delay between allowed button presses (seconds)
DELAY = 5

# Import image and text to print.
from cards import card_1 as DATA
TEXT = DATA["text"]
PIC_PATH = "_.png"
pic = cv2.imread(DATA["pic"])
pic = cv2.resize(pic, (130, 130))
cv2.imwrite(PIC_PATH, pic)

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN)

print("Press the button. Press Ctrl+C to exit.")

last_press_time = 0

try:
    while True:
        if GPIO.input(BUTTON_PIN) == GPIO.LOW:
            now = time.time()
            if now - last_press_time > DELAY:
                print("pressed")

                # Print the text
                os.system(f"sudo sh -c 'echo -e \"{TEXT}\" > /dev/usb/lp0'")

                # Print the image
                os.system(f"lp -d face_printer {PIC_PATH}")

                last_press_time = now

        time.sleep(0.05)  # check every 50 ms

except KeyboardInterrupt:
    print("Exiting")

finally:
    GPIO.cleanup()
