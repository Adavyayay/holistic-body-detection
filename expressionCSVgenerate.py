import mediapipe as mp
import cv2 
import csv
import os
import numpy as np

mp_drawing = mp.solutions.drawing_utils 
mp_holistic = mp.solutions.holistic

landmarks = ['class']

for val in range(1, 502):
    landmarks += ['x{}'.format(val), 'y{}'.format(val), 'z{}'.format(val), 'v{}'.format(val)]

with open('coordsTEST1.csv', mode='w', newline='') as f:
    csv_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(landmarks)

class_name = "smile"