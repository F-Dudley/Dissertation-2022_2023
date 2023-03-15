import open3d as o3d
import numpy as np
import copy


def VizualiseBaseTargetPointclouds(
    basePointcloud: o3d.geometry.PointCloud,
    targetPointcloud: o3d.geometry.PointCloud,
    windowName: str = "Base and Target Pointclouds",
    windowWidth: int = 1280, windowHeight: int = 720,
):

    clouds = []

    if (basePointcloud is not None):
        baseTmp = copy.deepcopy(basePointcloud)
        baseTmp.paint_uniform_color([0.25, 0.25, 0.25])
        clouds.append(baseTmp)

    if (targetPointcloud is not None):
        targetTmp = copy.deepcopy(targetPointcloud)
        targetTmp.paint_uniform_color([0.75, 0, 0])
        clouds.append(targetTmp)

    o3d.visualization.draw_geometries(
        clouds,
        window_name=windowName,
        width=windowWidth,
        height=windowHeight,
    )
