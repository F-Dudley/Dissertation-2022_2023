import torch
from point_e.diffusion import gaussian_diffusion

from point_e.diffusion.configs import DIFFUSION_CONFIGS, diffusion_from_config
from point_e.diffusion.sampler import PointCloudSampler
from point_e.models.download import load_checkpoint
from point_e.models.configs import MODEL_CONFIGS, model_from_config


def CreateCloudSampler(baseName: str) -> PointCloudSampler:
    device = torch.device('cude' if torch.cuda.is_available() else 'cpu')

    base_model = CreateModel(baseName, device)
    upsampler_model = CreateModel('upsample', device)

    base_diffusion = CreateDiffusion(baseName)
    upsampler_diffusion = CreateDiffusion('upsample')

    return PointCloudSampler(
        device=device,
        models=[base_model, upsampler_model],
        diffusions=[base_diffusion, upsampler_diffusion],
        num_points=[1024, 4096 - 1024],
        aux_channels=['R', 'G', 'B'],
        guidance_scale=[3.0, 3.0],
    )


def CreateModel(modelName: str, device: torch.device) -> torch.nn.Module:
    print(f'Loading {modelName} Model')
    model = model_from_config(MODEL_CONFIGS[modelName], device)
    model.eval()

    print('Loading Base Model Checkpoint')
    model.load_state_dict(load_checkpoint(modelName))

    return model


def CreateDiffusion(diffusionName: str) -> gaussian_diffusion.GaussianDiffusion:
    print(f'Loading {diffusionName} Diffusion')
    return diffusion_from_config(DIFFUSION_CONFIGS[diffusionName])
