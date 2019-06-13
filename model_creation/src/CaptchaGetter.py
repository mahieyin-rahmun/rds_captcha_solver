import urllib.request
import os

class CaptchaGetter:
    def __init__(self, num_of_rqsts, img_extension, path):
        self.url = 'https://rds3.northsouth.edu/index.php/captcha'
        self.iterations = num_of_rqsts
        self.dump_path = os.path.join(os.path.abspath(path), 'captcha_images')
        self.img_extension = img_extension

        if not os.path.isdir(self.dump_path):
            os.mkdir(self.dump_path)


    def dump_images(self):
        for i in range(self.iterations):
            img_name = f'{i}.{self.img_extension}'
            response = urllib.request.urlopen(self.url)
            output = open(os.path.join(self.dump_path, img_name), 'wb')
            output.write(response.read())
            output.close()
            print(f"Saved image {img_name}")


    def get_dump_path(self):
        return self.dump_path

