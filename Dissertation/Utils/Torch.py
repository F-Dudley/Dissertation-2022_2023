
import torch


def UseBestTorchDevice() -> torch.device:
    return torch.device('cuda' if torch.cuda.is_available() else 'cpu')
