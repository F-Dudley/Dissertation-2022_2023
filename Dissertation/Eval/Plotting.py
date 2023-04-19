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

    data_keys = list(rmseData.keys())
    data_values = list(rmseData.values())

    plt.style.use('ggplot')

    fig, ax = plt.subplots(layout='constrained')

    ax.bar(data_keys, data_values, width=bar_width)

    ax.axhline(
        y=target_rmse, linestyle='--',
        color='green',
        label='Target RMSE'
    )

    ax.legend(
        loc='center left',
        bbox_to_anchor=(1.04, 0.5),
    )
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
    x_lim_multiple: float = 2, y_lim_multiple: float = 2
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
    ax.hist(
        dist_data,
        bins=bins,
        density=True,
        color=hist_color, alpha=hist_alpha,
        label='Distance Data'
    )

    # # # #   # # # #

    # Plot Normal Distribution #

    mu, std = norm.fit(dist_data)
    xmin, xmax = ax.get_xlim()

    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, std)

    ax.plot(
        x, p, 'k',
        linewidth=2,
        color=curve_color, alpha=curve_alpha,
        label='Normal Distribution'
    )

    # # # # # # # # # # # # # #

    # Plot Mean / STD Increments
    ax.axvline(
        mu,
        color=mean_color, alpha=mean_alpha,
        linestyle='--',
        label='Mean'
    )

    std_plots = [mu - (std*2), mu - std, mu + std, mu + (std*2)]
    for i, value in enumerate(std_plots):
        ax.axvline(
            value,
            color=std_color, alpha=std_alpha,
            linestyle='--',
            label=f'Standard Deviations' if i == 0 else None
        )

    ax.legend(
        loc='center left',
        bbox_to_anchor=(1.04, 0.5),
    )

    ax.set_ylim(
        0,
        RoundToNearestMultiple(
            graph_standards['MAX_FREQUENCY'], y_lim_multiple)
    )

    ax.set_xlim(
        0,
        RoundToNearestMultiple(graph_standards['MAX_DISTANCE'], x_lim_multiple)
    )

    ax.set_xlabel('Distance (mm)')
    ax.set_ylabel('Frequency')
    plt.title(f'Normal Distribution of {technique} Data')

    return fig


def get_histogram_standards(cloud1, cloud2):

    dist = cloud1.compute_point_cloud_distance(cloud2)

    hist, bin = np.histogram(dist, bins=100, density=True)

    bin_width = bin[1] - bin[0]
    max_prob_density = np.max(hist) * bin_width * len(dist)

    print(f'Max Bin: {np.max(hist)}')

    return max_prob_density, np.max(dist)
