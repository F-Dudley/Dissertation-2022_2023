from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np


def plot_technique_rmse(data: dict, target_rmse: float = 0.5, bar_width: float = 0.4) -> Figure:
    """Plots the RMSE for each technique."""

    # Seperate the Data
    techniques = list(data.keys())

    sphere_rmse = []
    box_rmse = []

    for technique in techniques:
        if "sphere" in data[technique]:
            sphere_rmse.append(data[technique]["sphere"]["rmse"])
        if "box" in data[technique]:
            box_rmse.append(data[technique]["box"]["rmse"])

    x_ticks = np.arange(len(techniques))
    sphere_x_ticks = x_ticks - bar_width/2
    box_x_ticks = x_ticks + bar_width/2

    # Create the figure and the axis object
    fig, ax = plt.subplots()

    # Create the bars for the "sphere" RMSE values
    sphere_bars = ax.bar(sphere_x_ticks, sphere_rmse,
                         bar_width, label='Sphere', color='blue')

    # Create the bars for the "box" RMSE values
    box_bars = ax.bar(box_x_ticks, box_rmse, bar_width,
                      label='Box', color='orange')

    # Add the legend
    ax.legend()

    # Add the x-axis labels and ticks
    ax.set_xticks(x_ticks)
    ax.set_xticklabels(techniques)

    # Add the y-axis label
    ax.set_ylabel('RMSE')

    # Add the target dashed line for 0.5 that is green
    ax.axhline(y=0.5, linestyle='--', color='green')

    # Set the title
    ax.set_title('RMSE Values for Different Techniques')

    return fig
