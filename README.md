# Business Card Printer


## Install

If it's your first time using a particular Pi:

- Generate an SSH key and add it to GitHub.
- `git clone git@github.com:camoverride/business_cards.git`
- `cd business_cards`
- `python3 -m venv .venv`
- `source .venv/bin/activate`
- `pip install -r requirements.txt`

Install printer requirements (probably not all are needed):

- `sudo apt install libatlas-base-dev libgstreamer1.0-dev gstreamer1.0-plugins-base gstreamer1.0-plugins-good libcups2-dev libcupsimage2-dev git build-essential cups system-config-printer`

Test print some text:

- enable printer: `sudo chmod 777 /dev/usb/lp0`
- test printer: `echo -e "This is a test.\\n\\n\\n" > /dev/usb/lp0`

Get CUPS up and running [link](https://cdn-learn.adafruit.com/downloads/pdf/networked-thermal-printer-using-cups-and-raspberry-pi.pdf) and install the printer drivers:

- `cd ..`
- `git clone https://github.com/adafruit/zj-58`
- `cd zj-58`
- `make`
- `sudo ./install`

Set the printer name:

- `cd ../business_cards`
- `lpadmin -p face_printer -v usb://POS58/Printer?serial=FMD072`
- `lpadmin -p face_printer -E -m zjiang/ZJ-58.ppd`
- `cupsenable face_printer`


## Test

- `python print_card.py`


## Run

Start a service with *systemd*. This will start the program when the computer starts and revive it when it dies:

- `mkdir -p ~/.config/systemd/user`
- `cat business_card.service > ~/.config/systemd/user/business_card.service`

Start the service using the commands below:

- `systemctl --user daemon-reload`
- `systemctl --user enable business_card.service`
- `systemctl --user start business_card.service`

Check the status: `systemctl --user status business_card.service`

Start it on boot: `sudo loginctl enable-linger pi`

Get the logs: `journalctl --user -u business_card.service`

