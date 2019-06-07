import cv2
import numpy as np
import glob
import os

class Cleaner:
    def __init__(self, path_to_cropped_images, img_extension, path):
        self.cropped_images_path = path_to_cropped_images
        self.image_extension = img_extension
        self.cleaned_image_path = os.path.join(os.path.abspath(path), 'cleaned_images')

        if not os.path.isdir(self.cleaned_image_path):
            os.mkdir(self.cleaned_image_path)
    
    def clean_images(self):
        image_list = glob.glob(os.path.join(self.cropped_images_path, f'*.{self.image_extension}'))
        for image in image_list:
            img = cv2.imread(image)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            img = np.where(img == 128, 45, img)
            img_name = image.rsplit('\\', 1)[1]
            print(f"Cleaning image {img_name}...")
            cv2.imwrite(os.path.join(self.cleaned_image_path, img_name), img)
