"""Test for using the RaspberryPi camera to read the faces of the cards and create objects from the data"""
# import card
from picamera import PiCamera
from time import sleep


def main():
    try:
        camera = PiCamera()  # Creates PiCamera object
    except Exception:
        print("Error: Camera not connected")
        return
    camera.start_preview()  # Turns on the camera
    sleep(5)  # Waits 5 seconds
    camera.stop_preview()  # Turns off the camera
    

if __name__ == "__main__":
    main()
