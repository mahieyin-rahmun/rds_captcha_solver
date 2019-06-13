import cv2
import numpy as np

def crop_and_clean_images(img_path):
    captcha_img = cv2.imread(img_path)
    captcha_img = cv2.cvtColor(captcha_img, cv2.COLOR_BGR2GRAY)
    height, width = captcha_img.shape
    DIVISION = width//4

    parts = []

    for j in range(4):
        # cropping
        start = j * DIVISION
        end = (j + 1) *  DIVISION        
        captcha_img_temp = captcha_img[0:height, start:end]

        # cleaning
        captcha_img_temp = np.where(captcha_img_temp == 128, 45, captcha_img_temp)

        captcha_img_temp = cv2.cvtColor(captcha_img_temp, cv2.COLOR_GRAY2BGR)
        
        parts.append(captcha_img_temp)
    
    return parts        
