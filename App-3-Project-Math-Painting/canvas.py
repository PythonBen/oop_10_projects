import numpy as np
from PIL import Image


class Canvas:
    """Object where all shape will be drawn"""
    def __init__(self, height, width, color):
        self.height  = height
        self.width = width
        self.color = color

    # create a 3D numpy array of seros
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        self.data[:] = self.color

    def make(self, imagepath):
        image = Image.fromarray(self.data, 'RGB')
        image.save(imagepath)