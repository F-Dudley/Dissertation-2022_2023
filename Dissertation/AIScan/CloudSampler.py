from typing import Sequence
import torch
from point_e.diffusion.sampler import PointCloudSampler

from .Models import CreateModel, CreateDiffusion
from Utils.Torch import UseBestTorchDevice, UseTorchDevice


def CreateCloudSampler(baseName: str, numPoints: Sequence[int] = [1024, 4096 - 1024], torchDevice: str = None) -> PointCloudSampler:
    """Creates a Sampler and Model for the given Model Name"""

    device: torch.device = None

    if (torchDevice == None):
        device = UseBestTorchDevice()
    else:
        device = UseTorchDevice(torchDevice)

    base_model = CreateModel(modelName=baseName, device=device)
    upsampler_model = CreateModel(modelName='upsample', device=device)

    base_diffusion = CreateDiffusion(baseName)
    upsampler_diffusion = CreateDiffusion('upsample')

    return PointCloudSampler(
        device=device,
        models=[base_model, upsampler_model],
        diffusions=[base_diffusion, upsampler_diffusion],
        num_points=numPoints,
        aux_channels=['R', 'G', 'B'],
        guidance_scale=[3.0, 3.0],
    )
