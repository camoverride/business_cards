import RPi.GPIO as GPIO
import subprocess



# Text to be displayed on the card
TEXT = """
I'm Cam Smith, a Seattle-based artist whose work explores how AI is used for surveillance and control.

I teamed up with Myke Walton, a Biden-era AI policy expert, to write AI MUST DIE. It's a well-researched zine that presents critical perspectives on the way AI is talked about, governed, and owned in 2026.

Please take a look. If you'd like more copies, let 's get in touch. They usually sell for between $6 and $10.

There's also an online version you can share for free:

https:..aimustdie.info

Thanks!


CAM SMITH
email : camoverride@gmail.com
IG    : @camoverride
site  : https://smith.cam
"""


with open("/dev/usb/lp0", "wb") as printer:
    printer.write(TEXT.encode("utf-8"))
    printer.write(b"\n\n\n")

# subprocess.run(
#     ["lp", "-d", "face_printer"],
#     input=TEXT,
#     text=True,
#     check=True,
# )
