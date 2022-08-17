from PIL import Image
from Picture import Picture


class PictureProvider:
    def __init__(self, path):
        self.path = path

    def read(self):
        with Image.open(self.path) as im:
            return Picture(im.getdata(), im.width, im.height)
