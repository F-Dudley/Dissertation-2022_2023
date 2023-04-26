import sys
from typing import Dict, List
import open3d as o3d
import numpy as np
import tqdm


def CalculateDistance(cloud1: o3d.geometry.PointCloud, cloud2: o3d.geometry.PointCloud) -> List[float]:
    """
Calculates the distance between two point clouds.
\nUses the brute force method. (Not recommended)
\nReturns the distance in meters.
    """

    distances = []

    # Loops over each point in the first cloud
    # to find its closest point in the second cloud loop
    for point in cloud1.points:

        closestDist: np.floating = np.finfo(np.float32).max

        for point2 in cloud2.points:

            # Calculate the distance between the two points
            newDist = np.linalg.norm(point - point2)

            # If the new distance is closer than the previous closest
            # then update the closest distance
            if newDist < closestDist:
                closestDist = newDist

        # Add the closest distance to the list of distances
        distances.append(closestDist)

    return distances


def CalculateRMSE(cloud1: o3d.geometry.PointCloud, cloud2: o3d.geometry.PointCloud) -> float:
    """
Calculates the root mean squared error between two point clouds.
\nUses the Open3D compute_point_cloud_distance method. (Using a KDTree)
\nReturns the RMSE in meters.
    """

    # Calculate the distances between the two clouds
    distances = cloud1.compute_point_cloud_distance(cloud2)

    # Calculate the mean squared error
    mse = np.mean(np.square(distances))

    # Calculate the root mean squared error
    rmse = np.sqrt(mse)

    return rmse


def CalculateRMSE_brute(baseCloud: o3d.geometry.PointCloud, evalCloud: o3d.geometry.PointCloud) -> float:
    """
Calculates the root mean squared error between two point clouds.
\nUses a brute force method.
\nReturns the RMSE in meters.
    """

    sum = 0

    # Loops over each point in the first cloud
    # to find its closest point in the second cloud loop
    for point in tqdm.tqdm(evalCloud.points):

        closestDist: np.floating = np.finfo(np.float32).max

        for point2 in baseCloud.points:

            # Calculate the distance between the two points
            # and update the closest distance if it is closer
            newDist = np.linalg.norm(point - point2)
            if newDist < closestDist:
                closestDist = newDist

        # Add the squared distance to the sum
        sqDist = np.square(closestDist)

        sum += sqDist

    mse = sum / len(evalCloud.points)

    return np.sqrt(mse)


def CalculateSTD(cloud1: o3d.geometry.PointCloud, cloud2: o3d.geometry.PointCloud) -> Dict:
    """
Calculates the standard deviation between two point clouds.
\nUses the Open3D compute_point_cloud_distance method. (Using a KDTree)
\nReturns the standard deviation in meters. (Close to 0 is Best)
    """

    # Calculate the distances between the two clouds
    distances = cloud1.compute_point_cloud_distance(cloud2)

    # Returns values related to normal distribution, using the distance data.
    # With Standard Deviation being the most useful.
    return {
        "std": np.std(distances, dtype=np.float64),

        "min": np.min(distances),
        "max": np.max(distances),
        "mean": np.mean(distances),
    }
