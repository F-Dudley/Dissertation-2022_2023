from math import ceil


def RoundToNearestMultiple(num: float, multiple: float) -> float:
    """ Rounds the given number to the nearest multiple of the given multiple. """

    return ceil(num / multiple) * multiple
