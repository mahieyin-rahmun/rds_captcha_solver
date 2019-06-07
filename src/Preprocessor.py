import cv2
import numpy as np
import glob
import os
from random import randint

class Preprocessor:
    def __init__(self):
        self.files_list = files_list = glob.glob(os.path.abspath('../labelled_data/**'), recursive=True)
        self.files_list = [individual_file_path for individual_file_path in files_list if not os.path.isdir(individual_file_path)]
        self.fixed_image_width = 10
        self.fixed_image_height = 10

    def preprocess(self, testing=False):
        features = []
        labels = []

        for image_path in self.files_list:
            image = cv2.imread(image_path)
            hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

            if not testing:
                digit = image_path.rsplit('\\', 2)[1]
                labels.append(digit)

            # B G R here too!
            lower_red_boundary = np.array([0, 0, 141])
            upper_red_boundary = np.array([0, 0, 255])

            mask = cv2.inRange(hsv_image, lower_red_boundary, upper_red_boundary)

            contours, hier = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            c = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(c)
            
            mask = mask[y:y + h, x:x + w]
            mask = cv2.resize(mask, (self.fixed_image_height, self.fixed_image_width))
            mask = np.asarray(mask).flatten()
            features.append(mask)

        features = np.array(features)

        if not testing:
            return features, labels
        else:
            return features