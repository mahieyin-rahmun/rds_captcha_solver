import CaptchaGetter as CG
import CropImages as CI
import Cleaner as CL
import os

img_extension = 'png'
captcha_getter_obj = CG.CaptchaGetter(100, img_extension, '../')
path_to_captcha_imgs = captcha_getter_obj.get_dump_path()
captcha_getter_obj.dump_images()
img_cropper = CI.CropImages(path_to_captcha_imgs, img_extension, '../')
img_cropper.crop_and_save_images()
cropped_images_path = img_cropper.get_cropped_images_path()
img_cleaner = CL.Cleaner(cropped_images_path, img_extension, '../')
img_cleaner.clean_images()


# ================ CREATES LABELLED_DATA FOLDER ================ 
labelled_images_path_root = os.path.abspath('../labelled_data')

if not os.path.isdir(labelled_images_path_root):
    os.mkdir(labelled_images_path_root)

for i in range(10):
    if not os.path.isdir(os.path.join(labelled_images_path_root, str(i))):
        os.mkdir(os.path.join(labelled_images_path_root, str(i)))

# after this, manual labelling is needed. sort the files into their folder under the 'labelled_data' folder