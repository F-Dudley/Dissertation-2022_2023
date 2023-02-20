import os
from PIL import Image


def getPathImages(path) -> list[Image.Image]:
    """ Returns a list of images from the given file. """

    if (not os.path.isdir(path) or not os.path.exists(path)):
        throw("Provided Path does not exist or is not a directory.")

    images: list[Image.Image] = []

    for file in os.listdir(path):
        if (file.endswith(".jpg") or file.endswith(".png")):
            images.append(Image.open(os.path.join(path, file)))
        else:
            print(f"File: {file} is not a valid image file.")

    print(f'{len(images)} images found in {path}')

    return images