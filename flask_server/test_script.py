import cv2
import numpy as np
from random import randint
import pickle
import os


for i in range(1, 6):
    img = cv2.imread(f"./captcha{i}.png")
    img = cv2.resize(img, (480, 198))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(gray, 100, 150)

    # image_gs = cv2.adaptiveThreshold(image_gs, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 41, 3)
    # image_gs = cv2.bitwise_not(image_gs)
    # kernel = np.ones((5, 5), np.uint8)
    # image_gs = cv2.erode(image_gs, kernel, iterations=3)

    # lower_red_boundary = np.array([0])
    # upper_red_boundary = np.array([30])

    # mask = cv2.inRange(image_gs, lower_red_boundary, upper_red_boundary)
    # contours, hier = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # contours.sort(key=cv2.contourArea, reverse=True)
    # print(len(contours))

    # features_list = []

    # for idx, c in enumerate(contours):
    #     x, y, w, h = cv2.boundingRect(c)
    #     color = (70, 70, 70)
    #     cv2.rectangle(image_gs, (x, y), (x + w, y + h), color, 2)
    #     # cv2.putText(image_gs, str(idx), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, color, lineType=cv2.LINE_AA)
    #     # mask_temp = mask[y:y+h, x:x+w]
    #     # mask_temp = cv2.resize(mask_temp, (10, 10))
    #     # mask_temp = np.asarray(mask_temp).flatten()

    #     # features_list.append(mask_temp)
    #     # break

    cv2.imshow("Test", gray)
    cv2.imshow("Edges", edges)
    # cv2.imshow("Mask", mask)
    # cv2.imshow("Mask", hsv_img)
    cv2.waitKey(0)

# with open(os.path.join(os.path.abspath('.'), 'SVM-13-6-2019-11-45-2.sav'), 'rb') as model_file:
#     model = pickle.load(model_file)

# predictions = model.predict(features_list)
# text = ''.join([p for p in predictions])
# print(text)

# for idx, feature in enumerate(features_list):
#     temp_feature = np.asarray(feature)
#     temp_feature = temp_feature.reshape((10, 10))
#     temp_feature_reshaped = cv2.resize(temp_feature, (1280, 720))
#     cv2.imshow("Original Image", temp_feature)
#     cv2.imshow(f'Predicted = {str(predictions[idx])}', temp_feature_reshaped)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()