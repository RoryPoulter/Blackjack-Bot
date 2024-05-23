# Blackjack-Bot
Python program which uses a Raspberry Pi with a camera to read the cards in play, and decide the best possible move.

## Requirements
* [Raspberry Pi 4 Model B](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/)
* [Raspberry Pi Camera Module 2](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/)
* [Python 3.12.2](https://www.python.org/downloads/release/python-3122/)

## Installation
* Install the camera and enable in the Raspberry Pi configuration. *DO NOT TURN ON BEFORE INSTALLING THE CAMERA.*
* Run the `setup.sh` script to install the required modules and run the main code.
```bash
sh path/to/.build/setup.sh
```
### Manual Installation
* Install Python 3.12.3; follow the steps from [here](https://aruljohn.com/blog/python-raspberrypi/)

* Install the requirements

```bash 
sudo pip3 install -r path/to/requirements.txt
```

## Usage
