# Blackjack-Bot
Python program which uses a Raspberry Pi with a camera to read the cards in play, and decide the best possible move.

## Requirements
* [Raspberry Pi 4 Model B](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/)
* [Raspberry Pi Camera Module 2](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/)
* 64 bit Raspbian OS
* Deck of Cards
#### Recommended
* [Fan and Heat Sink](https://www.amazon.co.uk/GeeekPi-Version-Raspberry-Heatsink-Cooling/dp/B07DCP4973/ref=trb_chk_auth)

## Installation
### ----Hardware Installation----
Before turning the Raspberry Pi on, install the camera and cooling system (if purchased).\
Enable the camera in the Raspberry Pi config settings.

### ----Installing the Correct OS----
Install a 64 bit OS onto the Raspberry Pi.
If an OS is already installed, run the following command in the termial to check the OS version:
```bash
uname -m
```
If it says `aarch64` then it is 64 bit. If it says `armv7l` then it is 32 bit. To change the OS, reboot the Raspberry Pi and, when it is turning back on, hold `shift` to enter *Recovery Mode*.

### ----Software Installation----
#### Automatic
* Run the `setup.sh` script to install the required modules and run the main code
```bash
sh path/to/.build/setup.sh
```
#### Manual
* Install the dependencies

```bash
sudo apt install python3-opencv
sudo pip3 install -r path/to/requirements.txt
```
* Run the `main.py` file in the src directory

```bash
python3 path/to/src/main.py
```
