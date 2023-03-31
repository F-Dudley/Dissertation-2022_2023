import sys
from typing import Dict
import open3d as o3d
import numpy as np


def CalculateRMSE(cloud1: o3d.geometry.PointCloud, cloud2: o3d.geometry.PointCloud) -> float:
    """
Calculates the root mean squared error between two point clouds.
\nUses the Open3D compute_point_cloud_distance method. (Using a KDTree)
\nReturns the RMSE in meters.
    """

    distances = cloud1.compute_point_cloud_distance(cloud2)

    mse = np.mean(np.square(distances))

    rmse = np.sqrt(mse)

    return rmse


def CalculateRMSE_brute(baseCloud: o3d.geometry.PointCloud, evalCloud: o3d.geometry.PointCloud) -> float:
    """
Calculates the root mean squared error between two point clouds.
\nUses a brute force method.
\nReturns the RMSE in meters.
    """

    sum = 0

    for point in evalCloud.points:

        closestDist: np.floating = np.finfo(np.float32).max

        for point2 in baseCloud.points:

            newDist = np.linalg.norm(point - point2)
            if newDist < closestDist:
                closestDist = newDist

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

    distances = cloud1.compute_point_cloud_distance(cloud2)

    return {
        "std": np.std(distances, dtype=np.float64),

        "min": np.min(distances),
        "max": np.max(distances),
        "mean": np.mean(distances),
    }
