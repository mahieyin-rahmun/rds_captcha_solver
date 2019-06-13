import pickle
import os
import numpy as np
import cv2

from crop_and_clean import crop_and_clean_images
from preprocess import preprocess

def get_text_from_captcha(img_path=None):
    with open(os.path.join(os.path.abspath('.'), 'mysite', 'SVM-13-6-2019-11-45-2.sav'), 'rb') as model_file:
        model = pickle.load(model_file)

    img_parts = crop_and_clean_images(img_path)
    features = preprocess(img_parts)

    predictions = model.predict(features)

    prediction_text = ''.join([prediction for prediction in predictions])

    return prediction_text
