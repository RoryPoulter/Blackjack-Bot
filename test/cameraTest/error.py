"""Display error message when camera is not detected"""
def cameraError():
    """Prints an error message if the camera is not detected
    """
    print("""Error: Camera not detected.
If a camera is not installed: 
    1. Turn off Raspberry Pi
    2. Install camera
    3. Turn back on.
If a camera is installed:
    1. Type 'sudo raspi-config' in the terminal
    2. Select 'Interface Options'
    3. Enable Legacy Camera support""")
