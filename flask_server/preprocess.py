import cv2
import numpy as np

def preprocess(img_parts):
    features_list = []

    for img_part in img_parts:
        hsv_image = cv2.cvtColor(img_part, cv2.COLOR_BGR2HSV)

        # B G R here too!
        lower_red_boundary = np.array([0, 0, 141])
        upper_red_boundary = np.array([0, 0, 255])

        mask = cv2.inRange(hsv_image, lower_red_boundary, upper_red_boundary)

        contours, hier = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        c = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(c)
        
        mask = mask[y:y + h, x:x + w]
        mask = cv2.resize(mask, (10, 10))
        mask = np.asarray(mask).flatten()

        features_list.append(mask)

    return features_list