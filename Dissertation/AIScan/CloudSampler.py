from typing import Sequence
import torch
from point_e.diffusion.sampler import PointCloudSampler

from .Models import CreateModel, CreateDiffusion
from Utils.Torch import UseBestTorchDevice


def CreateCloudSampler(baseName: str, numPoints: Sequence[int] = [1024, 4096 - 1024]) -> PointCloudSampler:
    """Creates a Sampler and Model for the given Model Name"""

    bestDevice = UseBestTorchDevice()

    base_model = CreateModel(modelName=baseName, device=bestDevice)
    upsampler_model = CreateModel(modelName='upsample', device=bestDevice)

    base_diffusion = CreateDiffusion(baseName)
    upsampler_diffusion = CreateDiffusion('upsample')

    return PointCloudSampler(
        device=bestDevice,
        models=[base_model, upsampler_model],
        diffusions=[base_diffusion, upsampler_diffusion],
        num_points=numPoints,
        aux_channels=['R', 'G', 'B'],
        guidance_scale=[3.0, 3.0],
    )
