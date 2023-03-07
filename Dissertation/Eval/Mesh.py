import os
import open3d as o3d


def CreatePointcloudFromMeshVertices(meshDir: str) -> o3d.geometry.PointCloud:

    if (os.path.exists(meshDir) is False):
        raise Exception("Provided Mesh Directory does not exist.")

    # Load Mesh from File.
    mesh = o3d.io.read_triangle_mesh(meshDir)
    if (mesh.has_vertices() is False):
        raise Exception("Provided Mesh has no Vertices.")

    pointCloud = o3d.geometry.PointCloud()
    pointCloud.points = mesh.vertices

    del mesh

    return pointCloud
