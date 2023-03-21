import numpy as np


def uniformSampleList(list: list, sampleSize: int) -> list:
    """Returns an array of the given size with random samples from the given list."""

    if (sampleSize > len(list)):
        raise ValueError("Sample size is greater than the list size.")

    uniformSamples = np.linspace(0, len(list) - 1, sampleSize, dtype=int)

    newSample = [list[i] for i in uniformSamples]

    print(
        f"Uniform Sample of size {sampleSize} from list of size {len(list)} created."
    )

    return newSample


def MilimeterToMeter(milimeter: float) -> float:
    """Converts milimeter to meter."""

    return milimeter / 1000


def MeterToMilimeter(meter: float) -> float:
    """Converts meter to milimeter."""

    return meter * 1000


def FeetToMeter(feet: float) -> float:
    """Converts feet to meter."""

    return feet / 3.28084


def MeterToFeet(meter: float) -> float:
    """Converts meter to feet."""

    return meter * 3.28084
