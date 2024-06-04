"""Test for using the RaspberryPi camera to read the faces of the cards and create objects from the data"""
# import card
from time import sleep

from picamera import PiCamera


def main():
    try:
        camera = PiCamera()  # Creates PiCamera object
    except Exception:
        print("""Error: Camera not detected.
If a camera is not installed: 
    1. Turn off Raspberry Pi
    2. Install camera
    3. Turn back on.
If a camera is installed:
    1. Type 'sudo raspi-config' in the terminal
    2. Select 'Interface Options'
    3. Enable Legacy Camera support""")
        return
    camera.start_preview()  # Turns on the camera
    sleep(5)  # Waits 5 seconds
    camera.stop_preview()  # Turns off the camera


if __name__ == "__main__":
    main()
