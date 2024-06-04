"""Test file for text recognition in an image
Code from: https://tutorials-raspberrypi.com/raspberry-pi-text-recognition-ocr/"""
# TODO AI image recognition to read card faces; train model with images

import pytesseract
import numpy as np
from pytesseract import Output
import cv2

img_source = cv2.imread("test/cameraTest/coffee.jpg")


def getGreyscale(image):
    """Converts the original image to a greyscale version

    Args:
        image (MatLike): The original image

    Returns:
        MatLike: The greyscale image
    """
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def thresholding(image):
    """Converts the greyscale image to a binary image (black and white)

    Args:
        image (MatLike): The greyscale image

    Returns:
        MatLike: The binary image
    """
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


def opening(image):
    """Smooths the borders of the greyscale image

    Args:
        image (MatLike): The greyscale image

    Returns:
        MatLike: The opening of the image
    """
    kernel = np.ones((5, 5), np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)


def canny(image):
    """Identifies the edges in an image

    Args:
        image (MatLike): The greyscale image

    Returns:
        MatLike: The canny image
    """
    return cv2.Canny(image, 100, 200)


grey = getGreyscale(img_source)
thresh = thresholding(grey)
opening = opening(grey)
canny = canny(grey)

for img in [img_source, grey, thresh, opening, canny]:
    d = pytesseract.image_to_data(img, output_type=Output.DICT)
    n_boxes = len(d["text"])

    # back to RGB
    if len(img.shape) == 2:
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)

    for i in range(n_boxes):
        if int(d["conf"][i]) > 60:
            (text, x, y, w, h) = (d["text"][i], d["left"][i], d["top"][i], d["width"][i], d["height"][i])
            # don't show empty text
            if text and text.strip() != "":
                img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                img = cv2.putText(img, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)

    cv2.imshow("img", img)
    cv2.waitKey(0)
