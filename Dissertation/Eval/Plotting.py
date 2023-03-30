from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np

from .Info import SCANNING_TECHNIQUES
from Utils.Math import RoundToNearestMultiple


def plot_technique_rmse(data: dict, target_rmse: float = 0.5, bar_width: float = 0.4, upper_lim=10) -> Figure:
    """
    Plots the RMSE for each technique.
    The data should be in the following format:

    {
        "<TECHNIQUENAME>": {
            "sphere": {
                "rmse": float,
                "inlier_rmse": float,
            },
            "box": {
                "rmse": float,
                "inlier_rmse": float,
            }
        },
    }

    """

    plt.style.use('ggplot')

    # Prepare the data
    techniques = SCANNING_TECHNIQUES
    x = np.arange(len(techniques), step=1)
    rmses = {
        "sphere": [data[technique]["sphere"]["rmse"] for technique in techniques],
        "box": [data[technique]["box"]["rmse"] for technique in techniques]
    }

    # Create the Figure
    fig, ax = plt.subplots(layout='constrained')

    multiplier = 0
    for attr, measurement in rmses.items():
        offset = multiplier * bar_width
        rects = ax.bar(x + offset, measurement,
                       bar_width, label=attr.capitalize())
        ax.bar_label(rects, padding=3)
        multiplier += 1

    # Add Text Labels
    ax.set_ylabel('RMSE (mm)')
    ax.set_title('RMSE Values for Different Techniques')
    ax.set_xticks(x + bar_width, techniques)
    ax.axhline(y=5, linestyle='--', color='green', label='Target RMSE')
    ax.legend(
        loc='center left',
        bbox_to_anchor=(1.04, 0.5),
    )
    ax.set_ylim(0, upper_lim)

    return fig


def plot_technique_std(data: dict, x_gap_size: float, y_gap_size: float) -> Figure:
    """
    Plots the standard deviation for each technique.
    The data should be in the following format:

    {
        "<TECHNIQUENAME>": {
            "sphere": {
                "std": float,
                "inlier_std": float,
            },
            "box": {
                "std": float,
                "inlier_std": float,
            }
        },
    }

    """

    plt.style.use('ggplot')

    # Prepare the Data
    techniques = SCANNING_TECHNIQUES

    stds: list = []
    lower = []
    upper = []
    means = []

    for technique in techniques:

        stds.append(data[technique]["sphere"]["std"])
        lower.append(data[technique]["sphere"]["min"])
        upper.append(data[technique]["sphere"]["max"])
        means.append(data[technique]["sphere"]["mean"])

    print(f'STDS: {stds}')
    print(f'LOWER: {lower}')
    print(f'UPPER: {upper}')
    print(f'MEANS: {means}')

    fig, ax = plt.subplots(layout='constrained')

    # X Ticks
    xTicks = np.arange(
        x_gap_size / 2,
        (len(techniques) * x_gap_size),
        step=x_gap_size
    )
    ax.set_xlim(0, np.max(xTicks) + (x_gap_size/2))
    ax.set_xticks(xTicks)
    ax.set_xticklabels(techniques)

    # Plot the Data
    ax.errorbar(
        x=xTicks,
        y=stds,
        yerr=[lower, upper],
        fmt='o',
        capsize=4,
        capthick=1,
        ecolor='blue',
    )

    # Set Table Titles
    ax.set_xlabel('Technique')
    ax.set_ylabel('Standard Deviation (mm)')
    ax.set_title('Standard Deviation for Different Techniques')
    ax.legend(loc='upper right')

    return fig
