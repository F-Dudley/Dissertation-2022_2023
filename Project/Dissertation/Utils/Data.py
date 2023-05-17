import os
import json
from PIL import Image


def getPathNPBinaries(path) -> list[str]:
    """ Returns a list of file paths to the .npz files in the given directory. """

    # Check if the path exits and is a directory
    if (not os.path.isdir(path) or not os.path.exists(path)):
        raise ValueError("Provided Path does not exist or is not a directory.")

    npBinaries: list[str] = []

    # Gets all the .npz files in the provided directory
    for file in os.listdir(path):
        if (file.endswith(".npz")):
            npBinaries.append(os.path.join(path, file))
        else:
            print(f"File: {file} is not a valid .npy file.")

    print(f'{len(npBinaries)} .npz files found in {path}')

    return npBinaries


def getPathImages(path) -> list[Image.Image]:
    """ Returns a list of images from the given file. """

    # Check if the path exits and is a directory
    if (not os.path.isdir(path) or not os.path.exists(path)):
        raise ValueError("Provided Path does not exist or is not a directory.")

    images: list[Image.Image] = []

    # Gets all the image files in the provided directory
    for file in os.listdir(path):
        if (file.lower().endswith(".jpg") or file.lower().endswith(".png")):
            images.append(Image.open(os.path.join(path, file)))
        else:
            print(f"File: {file} is not a valid image file.")

    print(f'{len(images)} images found in {path}')

    return images


def loadJSON(path: str) -> dict:
    """ Returns a dictionary of the JSON file at the given path. """

    # Check if the path exits and is a file
    if (not os.path.isfile(path) or not os.path.exists(path)):
        raise ValueError("Provided Path does not exist or is not a file.")

    # Returns the loaded JSON file
    with open(path, 'r') as f:
        return json.load(f)


def saveJSON(path: str, data: dict) -> None:
    """ Saves the given data to the given path as a JSON file. """

    # Check if the path exits and is a file
    if (not os.path.isfile(path) or not os.path.exists(path)):
        raise ValueError("Provided Path does not exist or is not a file.")

    # Saves the data to the given path
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)


class JSON:
    """ A class to handle JSON files."""

    def __init__(self, path: str) -> None:
        """ Loads the JSON file at the given path. """

        # Checks if the path exits and is a file
        if (not os.path.isfile(path) or not os.path.exists(path)):
            raise ValueError("Provided Path does not exist or is not a file.")

        # Loads the JSON file
        self.path: str = os.path.abspath(path)
        self.load()

        print(f"Loaded JSON From: {self.path}")

    def __del__(self) -> None:
        """ Saves the JSON file when the object is destroyed."""

        self.save()

        print(f"Saved JSON at: {self.path}")

    def load(self) -> None:
        """ Loads the JSON file. """

        with open(self.path, 'r') as f:
            self.data = json.load(f)

    def save(self) -> None:
        """ Saves the JSON file. """

        with open(self.path, 'w') as f:
            json.dump(self.data, f, indent=4)

    def has(self, key: str) -> bool:
        """ Returns True if the given key exists. """

        return key in self.data

    def print(self):
        """ Prints out the Current Cached Data."""

        print(self.data)
