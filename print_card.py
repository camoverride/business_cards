import os
import time
import cv2



# Import image and text to print.
from cards import card_1 as DATA
pic = cv2.imread(DATA["pic"])
pic = cv2.resize(pic, (130, 130))
PIC_PATH = cv2.imwrite("_.png", pic)
TEXT = DATA["text"]


# Enable the printer.
os.system("sudo chmod 777 /dev/usb/lp0")

# Print the image
os.system(f"lp -d face_printer {PIC_PATH}")
time.sleep(0.5)

# Print the text.
os.system(f"sudo echo -e {TEXT} > /dev/usb/lp0")
time.sleep(0.5)
