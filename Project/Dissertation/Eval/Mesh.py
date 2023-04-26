import os
import open3d as o3d


def CreatePointcloudFromMeshVertices(meshDir: str) -> o3d.geometry.PointCloud:
    """
Creates a Point Cloud from the Vertices of a Mesh.
    """
    # Check if the Mesh Directory exists.
    if (os.path.exists(meshDir) is False):
        raise Exception("Provided Mesh Directory does not exist.")

    # Load Mesh from File.
    # and Check if verticies are valid
    mesh = o3d.io.read_triangle_mesh(meshDir)
    if (mesh.has_vertices() is False):
        raise Exception("Provided Mesh has no Vertices.")

    # Creates a Pointcloud from the vertex points
    pointCloud = o3d.geometry.PointCloud()
    pointCloud.points = mesh.vertices

    del mesh

    return pointCloud


def CreatePointcloudFromSampledMesh(meshDir: str, sampleSize: int = 1000) -> o3d.geometry.PointCloud:
    """
Creates a Point Cloud from a Mesh using the Mesh Vertices.
    """

    if (os.path.exists(meshDir) is False):
        raise Exception("Provided Mesh Directory does not exist.")

    # Load Mesh from File.
    mesh = o3d.io.read_triangle_mesh(meshDir)
    if (mesh.has_vertices() is False):
        raise Exception("Provided Mesh has no Vertices.")

    # Sample Mesh Vertices.
    pointCloud = mesh.sample_points_uniformly(sampleSize)

    del mesh

    return pointCloud


def CreatePointcloudFromDir(cloudDir: str) -> o3d.geometry.PointCloud:
    """
Loads a Pointcloud from a File Directory.
    """

    # Checks if the Pointcloud File exists.
    if (os.path.exists(cloudDir) is False):
        raise Exception("Provided Cloud File does not exist.")

    # Load Pointcloud from File.
    return o3d.io.read_point_cloud(cloudDir)
