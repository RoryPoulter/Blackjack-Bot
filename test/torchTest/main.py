"""Test file for using PyTorch for text/image recognition
"""
import time

import torch
# import numpy as np
from torchvision import models, transforms

import cv2
# from PIL import Image

torch.backends.quantized.engine = "qnnpack"

cap = cv2.VideoCapture(0, cv2.CAP_V4L2)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 224)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 224)
cap.set(cv2.CAP_PROP_FPS, 36)

preprocess = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

net = models.quantization.mobilenet_v2(pretrained=True, quantize=True)
# jit model to take it from ~20fps to ~30fps
net = torch.jit.script(net)

started: float = time.time()
last_logged: float = time.time()
frame_count: int = 0

count: int = 0
total: int = 0

with torch.no_grad():
    while count < 60:
        # read image
        ret, image = cap.read()
        if not ret:
            raise RuntimeError("failed to read frame")

        # convert from BGR to RGB
        image = image[:, :, [2, 1, 0]]
        permuted = image
        # preprocesses
        input_tensor = preprocess(image)

        # create a mini batch as expected by the model
        input_batch = input_tensor.unsqueeze(0)

        # run model
        output = net(input_batch)
        # do something with output...

        # log model performance
        frame_count += 1
        now = time.time()
        if now - last_logged > 1:
            total += frame_count / (now-last_logged)
            # print(f"{frame_count / (now-last_logged)} fps")
            last_logged = now
            frame_count = 0
            count += 1
    print(f"Average fps: {total / count}")
