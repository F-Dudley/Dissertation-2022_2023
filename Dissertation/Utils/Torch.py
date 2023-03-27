
import torch


def UseBestTorchDevice() -> torch.device:
    """Returns the best torch device to use"""
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print(f"Using {device} device for Torch Model.")

    return torch.device(device=device)


def UseTorchDevice(tDevice: str) -> torch.device:
    """Returns a Torch Device of the user's choice"""

    if (tDevice != 'cuda' and tDevice != 'cpu'):
        raise ValueError(f"Invalid Torch Device: {tDevice}")

    if (torch.cuda.is_available() == False and tDevice == 'cuda'):
        raise ValueError("Cannot use CUDA device as it is not available.")

    print(f"Using {tDevice} device for Torch Model.")

    return torch.device(device=tDevice)
