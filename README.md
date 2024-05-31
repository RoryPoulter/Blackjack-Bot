# Blackjack-Bot
Python program which uses a Raspberry Pi with a camera to read the cards in play, and decide the best possible move.

## Requirements
* [Raspberry Pi 4 Model B](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/)
* [Raspberry Pi Camera Module 2](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/)
* 64 bit Raspbian OS

Run the following command in the termial to check the OS version:
```bash
uname -m
```
If it says `aarch64` then it is 64 bit. If it says `armv7l` then it is 32 bit.

## Installation
* Install the camera and enable in the Raspberry Pi configuration. *DO NOT TURN ON BEFORE INSTALLING THE CAMERA.*
* Run the `setup.sh` script to install the required modules and run the main code.
```bash
sh path/to/.build/setup.sh
```
### Manual Installation
* Install the dependencies

```bash
sudo apt install python3-opencv
sudo pip3 install -r path/to/requirements.txt
```

## Usage
