import os
import time
import cv2

# Import image and text to print.
from cards import card_1 as DATA
TEXT = DATA["text"]
PIC_PATH = "_.png"

def reset_usblp_device(device_id="1-1.1:1.0"):
    print(f"Resetting USB printer device {device_id}...")
    unbind_path = "/sys/bus/usb/drivers/usblp/unbind"
    bind_path = "/sys/bus/usb/drivers/usblp/bind"

    if os.path.exists(unbind_path) and os.path.exists(bind_path):
        with open(unbind_path, "w") as f:
            f.write(device_id)
        print(f"Unbound {device_id}")
        time.sleep(1)  # Give time to reset
        with open(bind_path, "w") as f:
            f.write(device_id)
        print(f"Bound {device_id}")
        time.sleep(1)
    else:
        print("USB usblp driver bind/unbind paths do not exist!")

def print_image():
    pic = cv2.imread(DATA["pic"])
    pic = cv2.resize(pic, (130, 130))
    cv2.imwrite(PIC_PATH, pic)

    # Print image using lp (slow but reliable for images)
    print("Printing image...")
    os.system(f"lp -d face_printer {PIC_PATH}")
    time.sleep(0.5)

def print_text(text):
    # Reset USB device so /dev/usb/lp0 reappears correctly after using lp
    reset_usblp_device()

    # Ensure permissions allow writing
    os.system("sudo chmod 777 /dev/usb/lp0")

    print("Printing text...")
    # Write text directly to device
    with open("/dev/usb/lp0", "w") as printer:
        printer.write(text + "\n")

if __name__ == "__main__":
    print_image()
    print_text(TEXT)
