import open3d as o3d
import numpy as np


def OLD_CalculateRMSE(cloud1: o3d.geometry.PointCloud, cloud2: o3d.geometry.PointCloud) -> float:
    """Calculates the root mean squared error between two point clouds."""

    # Get the points from the clouds
    points1 = np.asarray(cloud1.points)
    points2 = np.asarray(cloud2.points)

    assert points1.shape == points2.shape

    # Calculate the difference between the points
    difference = points1 - points2

    # Calculate the squared difference
    squaredDifference = difference * difference

    # Sum the squared difference
    sumSquaredDifference = np.sum(squaredDifference)

    # Divide the sum by the number of points
    meanSquaredDifference = sumSquaredDifference / points1.shape[0]

    # Take the square root of the mean
    rootMeanSquaredDifference = np.sqrt(meanSquaredDifference)

    return rootMeanSquaredDifference


def CalculateRMSE(cloud1: o3d.geometry.PointCloud, cloud2: o3d.geometry.PointCloud) -> float:
    """Calculates the root mean squared error between two point clouds."""

    distances = cloud1.compute_point_cloud_distance(cloud2)

    mse = np.mean(np.square(distances))

    rmse = np.sqrt(mse)

    return rmse
