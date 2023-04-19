
import torch
from point_e.models.download import load_checkpoint
from point_e.models.configs import MODEL_CONFIGS, model_from_config
from point_e.diffusion.configs import DIFFUSION_CONFIGS, diffusion_from_config
from point_e.diffusion import gaussian_diffusion


def CreateModel(modelName: str, device: torch.device) -> torch.nn.Module:
    print(f'Loading {modelName} Model')
    model = model_from_config(MODEL_CONFIGS[modelName], device)
    model.eval()

    print(f'Loading {modelName} Model Checkpoint')
    model.load_state_dict(load_checkpoint(modelName, device=device))

    return model


def CreateDiffusion(diffusionName: str) -> gaussian_diffusion.GaussianDiffusion:
    print(f'Loading {diffusionName} Diffusion')
    return diffusion_from_config(DIFFUSION_CONFIGS[diffusionName])
