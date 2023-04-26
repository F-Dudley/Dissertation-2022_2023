from typing import Dict
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

from .Info import SCANNING_TECHNIQUES
from Utils.Math import RoundToNearestMultiple


def plot_technique_rmse(rmseData: dict, target_rmse: float = 0.5, bar_width: float = 0.4) -> Figure:
    """
Plots the RMSE for each Technique.

:param rmseData: The RMSE data to plot. Should be in the following format: {<TECHNIQUENAME>: <RMSE>: float, ...}

    """

    data_keys = [
        key for key in list(rmseData.keys())
        if key in SCANNING_TECHNIQUES
    ]
    data_values = list(rmseData.values())

    plt.style.use('ggplot')

    # Create a figure with a constrained layout
    fig, ax = plt.subplots(layout='constrained')

    # Plot the bar data
    ax.bar(data_keys, data_values, width=bar_width)

    # Add the Horizontal RMSE Target Line
    ax.axhline(
        y=target_rmse, linestyle='--',
        color='green',
        label='Target RMSE'
    )

    # Add a Legend, with origin offset to the right of the table
    ax.legend(
        loc='center left',
        bbox_to_anchor=(1.04, 0.5),
    )

    # Apply Title and Axis Labels
    ax.set_xlabel('Techniques')
    ax.set_ylabel('RMSE (mm)')
    ax.set_title('RMSE Values for Different Techniques')

    return fig


def plot_technique_std(
    dist_data: np.ndarray,
    graph_standards: Dict[str, float],
    technique: str,
    bins: int = 100,
    hist_alpha: float = 0.6, curve_alpha: float = 0.8,
    hist_color: str = 'b', curve_color: str = 'r',
    mean_color: str = 'g', mean_alpha: float = 1,
    std_color: str = 'y', std_alpha: float = 1,
    x_lim_multiple: float = 2, y_lim_multiple: float = 0.1
) -> Figure:
    """
Plots the standard deviation for an input technique.

The Figure denotes the distance data in a histogram, and the standard deviation in a bell curve.
    """

    assert technique in SCANNING_TECHNIQUES, f'Invalid Technique: {technique}'
    assert bins > 0, f'Invalid Number of Bins: {bins}'

    plt.style.use('ggplot')
    fig, ax = plt.subplots(layout='constrained')

    # Plot Histogram #

    dist_data = np.array(dist_data)

    # Plot the Histogram based on Density using the distance data.
    ax.hist(
        dist_data,
        bins=bins,
        density=True,
        color=hist_color, alpha=hist_alpha,
        label='Distance Data'
    )

    # # # #   # # # #

    # Plot Normal Distribution #

    # Fit a normal distribution to the data:
    # providing the mean and standard deviation of the data.
    mu, std = norm.fit(dist_data)
    xmin, xmax = ax.get_xlim()

    # Get the x values for the curve, based on the min and max of the histogram.
    # Then get the probability density for each x value, based on the mean and standard deviation.
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, std)

    # Plots the Bell Curve
    ax.plot(
        x, p, 'k',
        linewidth=2,
        color=curve_color, alpha=curve_alpha,
        label='Normal Distribution'
    )

    # # # # # # # # # # # # # #

    # Plot Mean / STD Increments

    # Plots the Mean
    ax.axvline(
        mu,
        color=mean_color, alpha=mean_alpha,
        linestyle='--',
        label='Mean'
    )

    # Plots each Standard Deviation around the mean
    std_plots = [mu - (std*2), mu - std, mu + std, mu + (std*2)]
    for i, value in enumerate(std_plots):
        ax.axvline(
            value,
            color=std_color, alpha=std_alpha,
            linestyle='--',
            label=f'Standard Deviations' if i == 0 else None
        )

    # Creates a legend, with origin offset to the right of the table
    ax.legend(
        loc='center left',
        bbox_to_anchor=(1.04, 0.5),
    )

    # Sets the upper x and y axis limits, based on the graph standards.
    # With the graph standards being the max recorded distance and probability density.
    ax.set_ylim(
        0,
        RoundToNearestMultiple(
            graph_standards['MAX_PROB_DENSITY'],
            y_lim_multiple
        )
    )

    ax.set_xlim(
        0,
        RoundToNearestMultiple(
            graph_standards['MAX_DISTANCE'],
            x_lim_multiple
        )
    )

    # Adds a Title and Axis labels
    ax.set_xlabel('Distance (mm)')
    ax.set_ylabel('Density')
    plt.title(f'Normal Distribution of {technique} Data')

    return fig


def get_histogram_standards(
    cloud1,
    cloud2,
    bins: int = 100,
):
    """
Gets the maximum probability density and distance for a histogram of two point clouds.
    """

    # Get the distance between each point in the two clouds.
    # Then multiply by 1000 to convert to mm.
    dist = np.array(cloud1.compute_point_cloud_distance(cloud2))
    dist *= 1000

    # Get the histogram of the distance data, with the specified number of bins.
    hist, bin = np.histogram(dist, bins=bins, density=True)

    # Gets the Maximum Probability Density and Distance
    return np.max(hist), np.max(dist)
