from PIL import Image
import os


class ImageEditor:

    proccesed_image = None
    config = None
    attributes = None

    def set_config(self, config):
        self.config = config
        self.attributes = [attr for attr in dir(self.config)
                           if not attr.startswith('__')]

    def run(self):
        media_path = 'media'
        files_names = os.listdir(media_path)
        files_paths = [media_path + "/" + file_name for file_name in files_names]

        for image_path in files_paths:
            self.proccesed_image = Image.open(image_path)
            for attr in self.attributes:
                try:
                    self.METHODS_DICT[attr](self, self.proccesed_image)
                except KeyError:
                    print(f"config attribute {attr} not supported")
            self.proccesed_image.save(image_path)
            self.proccesed_image.close()

    def image_w(self, image):
        width = self.config.IMAGE_W
        height = image.size[1]
        changed_image = image.resize((width, height))
        self.proccesed_image = changed_image

    def image_h(self, image):
        width = image.size[0]
        height = self.config.IMAGE_H
        changed_image = image.resize((width, height))
        self.proccesed_image = changed_image

    def rotate(self, image):
        rotation = self.config.ROTATE
        if not rotation:
            pass
        else:
            try:
                changed_image = image.rotate(rotation)
                self.proccesed_image = changed_image
            except TypeError:
              print("Wrong rotate attribute value")

    def white_black(self, image):
        if self.config.WHITE_BLACK == True:
            changed_image = image.convert("L")
            self.proccesed_image = changed_image


    METHODS_DICT = {'IMAGE_W': image_w, 'IMAGE_H': image_h, 'ROTATE': rotate, 'WHITE_BLACK': white_black}
