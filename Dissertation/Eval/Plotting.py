from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np


def plot_technique_rmse(data: dict, target_rmse: float = 0.5, bar_width: float = 0.4, upper_lim=2.0) -> Figure:
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

    # Prepare the data
    techniques = list(data.keys())
    x = np.arange(len(techniques))
    rmses = {
        "sphere": [data[technique]["sphere"]["rmse"] for technique in techniques],
        "box": [data[technique]["box"]["rmse"] for technique in techniques]
    }

    print(f'RMSE Data: \n{rmses}')

    # Create the Figure
    fig, ax = plt.subplots(layout='constrained')

    multiplier = 0
    for attr, measurement in rmses.items():
        offset = multiplier * bar_width
        rects = ax.bar(x + offset, measurement, bar_width, label=attr)
        ax.bar_label(rects, padding=3)
        multiplier += 1

    # Add Text Labels
    ax.set_ylabel('RMSE (mm)')
    ax.set_title('RMSE Values for Different Techniques')
    ax.set_xticks(x + bar_width, techniques)
    ax.axhline(y=0.5, linestyle='--', color='green', label='Target RMSE')
    ax.legend(loc='upper right')
    ax.set_ylim(0, upper_lim)

    return fig
