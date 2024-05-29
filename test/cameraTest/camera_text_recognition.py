"""Test file for text recognition in a camera feed
Code from: https://tutorials-raspberrypi.com/raspberry-pi-text-recognition-ocr/"""

import cv2
import pytesseract
from pytesseract import Output


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    try:
        d= pytesseract.image_to_data(frame, output_type=Output.DICT)
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
        quit()
    n_boxes = len(d["text"])
    for i in range(n_boxes):
        if int(d["conf"][i]) > 60:
            (text, x, y, w, h) = (d["text"][i], d["left"][i], d["top"][i], d["width"][i], d["height"][i])
            # don't show empty text
            if text and text.strip() != "":
                frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                frame = cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)
    
    # Display the resulting frame
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()
