import os
import cv2
import glob
import string
import random


class CropImages:
    def __init__(self, dump_path, image_extension):
        self.image_extension = image_extension
        self.files_list = glob.glob(os.path.join(dump_path, f'*.{self.image_extension}'))
        self.files_list.sort(key=lambda file_path: int(file_path.rsplit('\\', 1)[1].split('.')[0]))
        self.write_path = os.path.join(os.path.abspath('../'), 'cropped_images')
        self.characters = string.ascii_lowercase + string.digits

        if not os.path.isdir(self.write_path):
            os.mkdir(self.write_path)


    def crop_and_save_images(self):
        for i in range(len(self.files_list)):
            captcha_img = cv2.imread(self.files_list[i])
            captcha_img = cv2.cvtColor(captcha_img, cv2.COLOR_BGR2GRAY)
            height, width = captcha_img.shape
            DIVISION = width//4

            for j in range(4):
                start = j * DIVISION
                end = (j + 1) *  DIVISION
                captcha_img_temp = captcha_img[0:height, start:end]
                img_name = ''.join([random.choice(self.characters) for i in range(8)]) + f'.{self.image_extension}'
                print(f'Saving image {img_name}...')
                cv2.imwrite(os.path.join(self.write_path, img_name), captcha_img_temp)

        print("Files cropped and saved successfully...")
    
    def get_cropped_images_path(self):
        return self.write_path