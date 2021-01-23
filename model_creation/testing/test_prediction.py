import pickle
import os
import numpy as np
import cv2

import sys
sys.path.append("..")

import src.CaptchaGetter as CG
import src.CropImages as CI
import src.Cleaner as CL
import src.Preprocessor as PC

img_extension = 'png'
captcha_getter_obj = CG.CaptchaGetter(10, img_extension, './')
path_to_captcha_imgs = captcha_getter_obj.get_dump_path()
captcha_getter_obj.dump_images()
img_cropper = CI.CropImages(path_to_captcha_imgs, img_extension, './')
img_cropper.crop_and_save_images()
cropped_images_path = img_cropper.get_cropped_images_path()
img_cleaner = CL.Cleaner(cropped_images_path, img_extension, './')
img_cleaner.clean_images()

p = PC.Preprocessor('./', testing=True)
features = p.preprocess(testing=True)

# model name changes, silly. needs to be updated accordingly after running code in the src folder
with open(os.path.join(os.path.abspath('../model'), 'SVM-23-1-2021-19-18-34.sav'), 'rb') as model_file:
    model = pickle.load(model_file)

predictions = model.predict(features)

for idx, feature in enumerate(features):
    temp_feature = np.asarray(feature)
    temp_feature = temp_feature.reshape((10, 10))
    temp_feature_reshaped = cv2.resize(temp_feature, (1280, 720))
    cv2.imshow("Original Image", temp_feature)
    cv2.imshow(f'Predicted = {str(predictions[idx])}', temp_feature_reshaped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

