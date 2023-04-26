import open3d as o3d


def CreateBaseSpherePointCloud(diameter: float, resolution: int = 100) -> o3d.geometry.PointCloud:
    """
Creates a Point Cloud of a Sphere with the given Diameter and Resolution (Density)
    """

    # Create a Sphere Mesh
    sphereMesh = o3d.geometry.TriangleMesh.create_sphere(
        radius=diameter / 2, resolution=50)
    sphereMesh.compute_vertex_normals()

    # Samples required number of points from the sphere mesh to generate a cloud
    sphereCloud = sphereMesh.sample_points_poisson_disk(
        number_of_points=resolution
    )

    return sphereCloud
