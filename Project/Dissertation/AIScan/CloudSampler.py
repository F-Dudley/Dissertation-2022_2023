from typing import Sequence
import torch
from point_e.diffusion.sampler import PointCloudSampler

from .Models import CreateModel, CreateDiffusion
from Utils.Torch import UseBestTorchDevice, UseTorchDevice


def CreateCloudSampler(baseName: str, numPoints: Sequence[int] = [1024, 4096 - 1024], torchDevice: str = None) -> PointCloudSampler:
    """Creates a Sampler and Model for the given Model Name"""

    device: torch.device = None                                         # type: ignore

    # Get the best device available if none is specified
    # but use their device if they specified one
    if (torchDevice == None):
        device = UseBestTorchDevice()
    else:
        device = UseTorchDevice(torchDevice)

    # Create the specified and upsampler model
    base_model = CreateModel(modelName=baseName, device=device)
    upsampler_model = CreateModel(modelName='upsample', device=device)

    # Create the specified and upsampler diffusion
    base_diffusion = CreateDiffusion(baseName)
    upsampler_diffusion = CreateDiffusion('upsample')

    # Return the Final Sampler with required components
    return PointCloudSampler(
        device=device,
        models=[base_model, upsampler_model],
        diffusions=[base_diffusion, upsampler_diffusion],
        num_points=numPoints,
        aux_channels=['R', 'G', 'B'],
        guidance_scale=[3.0, 3.0],
    )
