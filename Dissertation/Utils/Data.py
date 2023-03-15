import os
import json
from PIL import Image


def getPathNPBinaries(path) -> list[str]:
    """ Returns a list of file paths to the .npz files in the given directory. """

    if (not os.path.isdir(path) or not os.path.exists(path)):
        raise ValueError("Provided Path does not exist or is not a directory.")

    npBinaries: list[str] = []

    for file in os.listdir(path):
        if (file.endswith(".npz")):
            npBinaries.append(os.path.join(path, file))
        else:
            print(f"File: {file} is not a valid .npy file.")

    print(f'{len(npBinaries)} .npz files found in {path}')

    return npBinaries


def getPathImages(path) -> list[Image.Image]:
    """ Returns a list of images from the given file. """

    if (not os.path.isdir(path) or not os.path.exists(path)):
        raise ValueError("Provided Path does not exist or is not a directory.")

    images: list[Image.Image] = []

    for file in os.listdir(path):
        if (file.lower().endswith(".jpg") or file.lower().endswith(".png")):
            images.append(Image.open(os.path.join(path, file)))
        else:
            print(f"File: {file} is not a valid image file.")

    print(f'{len(images)} images found in {path}')

    return images


def loadJSON(path: str) -> dict:
    """ Returns a dictionary of the JSON file at the given path. """

    if (not os.path.isfile(path) or not os.path.exists(path)):
        raise ValueError("Provided Path does not exist or is not a file.")

    with open(path, 'r') as f:
        return json.load(f)


def saveJSON(path: str, data: dict) -> None:
    """ Saves the given data to the given path as a JSON file. """

    if (not os.path.isfile(path) or not os.path.exists(path)):
        raise ValueError("Provided Path does not exist or is not a file.")

    with open(path, 'w') as f:
        json.dump(data, f, indent=4)