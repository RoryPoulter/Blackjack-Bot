"""Test file for text recognition in a camera feed
Code from: https://tutorials-raspberrypi.com/raspberry-pi-text-recognition-ocr/"""

import sys

import cv2
import pytesseract
from pytesseract import Output

from error import cameraError


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()   
    try:
        d= pytesseract.image_to_data(frame, output_type=Output.DICT)
    except Exception:
        cameraError()
        sys.exit()
    n_boxes = len(d["text"])
    for i in range(n_boxes):
        if int(d["conf"][i]) > 60:
            (text, x, y, w, h) = (d["text"][i], d["left"][i], d["top"][i], d["width"][i],
                                  d["height"][i])
            if text and text.strip() != "":  # don't show empty text
                frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                frame = cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.2,
                                    (0, 255, 0), 3)
    cv2.imshow("frame", frame)  # Display the resulting frame
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()
