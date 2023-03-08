import open3d as o3d


def CreateBaseSpherePointCloud(diameter: float, resolution: int = 100) -> o3d.geometry.PointCloud:
    sphereMesh = o3d.geometry.TriangleMesh.create_sphere(
        radius=diameter / 2, resolution=50)
    sphereMesh.compute_vertex_normals()

    sphereCloud = sphereMesh.sample_points_poisson_disk(
        number_of_points=resolution
    )

    return sphereCloud
