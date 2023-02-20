import os
from PIL import Image

from point_e import PointE


def getPathImages(path) -> list[Image.Image]:
    """ Returns a list of images from the given path. """

    if (not os.path.isdir(path) or not os.path.exists(path)):
        throw("Provided Path does not exist or is not a directory.")

    images: list[Image.Image] = []

    for file in os.listdir(path):
        if (file.endswith(".jpg") or file.endswith(".png")):
            images.append(Image.open(os.path.join(path, file)))
        else:
            print(f"File: {file} is not a valid image file.")

    return images
