import os
import time
import cv2

# Import image and text to print.
from cards import card_1 as DATA
TEXT = DATA["text"]
PIC_PATH = "_.png"
pic = cv2.imread(DATA["pic"])
pic = cv2.resize(pic, (130, 130))
cv2.imwrite(PIC_PATH, pic)

def reset_usblp_device(usb_device_id="1-1.1"):
    unbind_path = "/sys/bus/usb/drivers/usblp/unbind"
    bind_path = "/sys/bus/usb/drivers/usblp/bind"
    print(f"Resetting USB printer device {usb_device_id}...")
    os.system(f"echo '{usb_device_id}' | sudo tee {unbind_path}")
    time.sleep(0.2)
    os.system(f"echo '{usb_device_id}' | sudo tee {bind_path}")
    print("Reset done.")

# 1) Print the image using lp (slow but works)
os.system(f"lp -d face_printer {PIC_PATH}")

# 2) Reset the USB printer device so /dev/usb/lp0 becomes accessible again
reset_usblp_device("1-1.1")

time.sleep(1)  # give time to reinitialize

# 3) Allow writing to lp0 device
os.system("sudo chmod 777 /dev/usb/lp0")

# 4) Print the text directly to the device (fast)
os.system(f"sudo bash -c \"echo -e '{TEXT}' > /dev/usb/lp0\"")
