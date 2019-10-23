import cv2
import numpy as np

net = cv2.dnn.readNet("/Users/mohammedchowdhury/Desktop/YOLO ObjectDetection/Yolo/yolov3.weights","/Users/mohammedchowdhury/Desktop/YOLO ObjectDetection/Yolo/yolov3.cfg")

classes = []
