import os
import open3d as o3d
import numpy as np


def main():

    dir: str = "D:/Programming/Projects/Dissertation-2022_2023/Dissertation/samples/data/Kinect/sphere/raw"

    if (not os.path.isdir(dir) or not os.path.exists(dir)):
        raise ValueError("Provided Path does not exist or is not a directory.")

    clouds = os.listdir(dir)

    # Only keep the .ply files
    clouds = [cloud for cloud in clouds if cloud.endswith(".ply")]

    pcds = []

    for cloudName in clouds:

        cloudRotation = int(cloudName.split(".")[0])
        print(cloudRotation)

        cloud = o3d.io.read_point_cloud(os.path.join(dir, cloudName))

        # Kinect Rotation Correction
        rotation = o3d.geometry.get_rotation_matrix_from_xyz(
            (0, -cloudRotation, 0))
        cloud.rotate(rotation)

        # Rotate cloud around y axis using cloudRotation
        rotation = o3d.geometry.get_rotation_matrix_from_xyz(
            (0, np.deg2rad(cloudRotation), 0))
        cloud.rotate(rotation)

        pcds.append(cloud)

        saveLocation: str = os.path.join(dir, cloudName)

        print(f"Saving {cloud} @ {saveLocation}")
        o3d.io.write_point_cloud(saveLocation, cloud)

    # Vizualize the clouds
    o3d.visualization.draw_geometries(pcds)


if __name__ == "__main__":
    main()
