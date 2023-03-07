
import torch


def UseBestTorchDevice() -> torch.device:
    """Returns the best torch device to use"""
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print(f"Using {device} device for Torch Model.")

    return torch.device(device=device)
