import open3d as o3d


def CreateSpherePointCloud(diameter: float, resolution: int = 100) -> o3d.geometry.PointCloud:
    sphereMesh = o3d.geometry.TriangleMesh.create_sphere(
        radius=diameter / 2, resolution=20)
    sphereMesh.compute_vertex_normals()

    sphereCloud = sphereMesh.sample_points_uniformly(
        number_of_points=resolution
    )

    return sphereCloud
