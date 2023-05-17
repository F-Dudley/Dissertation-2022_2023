from typing import Tuple
import open3d as o3d


def CreateBaseCubePointCloud(size: Tuple[float, float, float], resolution: int = 100) -> o3d.geometry.PointCloud:
    """
Creates a Point Cloud of a Cube with the given Size and Resolution (Density)
    """

    # Create a Cube Mesh
    cubeMesh = o3d.geometry.TriangleMesh.create_box(
        width=size[0], height=size[1], depth=size[2]
    )
    cubeMesh.compute_vertex_normals()

    # Samples required number of points from the cube mesh to generate a cloud
    cubeCloud = cubeMesh.sample_points_poisson_disk(
        number_of_points=resolution
    )

    return cubeCloud
