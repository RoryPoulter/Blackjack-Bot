"""Test for using the RaspberryPi camera to read the faces of the cards and create objects from the 
data. Currently does not read text on cards."""
# from time import sleep
# import sys

# try:
#     from picamera import PiCamera
# except OSError as e:
#     print(f"Module 'Picamera' not detected; {e}")
#     sys.exit()

# from error import cameraError

# def main():
#     """The main body of code
#     """
#     PiCamera()
#     try:
#         camera = PiCamera()  # Creates PiCamera object
#     except Exception:
#         cameraError()
#         return
#     camera.start_preview()  # Turns on the camera
#     sleep(5)  # Waits 5 seconds
#     camera.stop_preview()  # Turns off the camera


# if __name__ == "__main__":
#     main()
