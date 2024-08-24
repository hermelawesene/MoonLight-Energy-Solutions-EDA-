import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_wind_polar(df, wind_speed_column='WS', wind_direction_column='WD', title="Wind Speed and Direction", figsize=(10, 8)):
    """
    Plot a polar plot to visualize wind speed distribution across wind direction.

    Parameters:
    df (pd.DataFrame): The input DataFrame.
    wind_speed_column (str): The name of the wind speed column.
    wind_direction_column (str): The name of the wind direction column.
    title (str): The title of the plot.
    figsize (tuple): Figure size of the plot.
    """
    wind_speeds = df[wind_speed_column]
    wind_directions = np.deg2rad(df[wind_direction_column])  # Convert degrees to radians

    plt.figure(figsize=figsize)
    ax = plt.subplot(111, polar=True)
    ax.scatter(wind_directions, wind_speeds, c=wind_speeds, cmap='viridis', alpha=0.75, edgecolors='w')
    ax.set_title(title, va='bottom')
    plt.show()

def plot_wind_direction_distribution(df, wind_direction_column='WD', title="Wind Direction Distribution", bins=36, figsize=(10, 6)):
    """
    Plot a histogram of wind direction distribution.

    Parameters:
    df (pd.DataFrame): The input DataFrame.
    wind_direction_column (str): The name of the wind direction column.
    title (str): The title of the plot.
    bins (int): Number of bins for the histogram.
    figsize (tuple): Figure size of the plot.
    """
    plt.figure(figsize=figsize)
    wind_directions = df[wind_direction_column]
    plt.hist(wind_directions, bins=bins, edgecolor='k', alpha=0.7)
    plt.title(title)
    plt.xlabel('Wind Direction (°)')
    plt.ylabel('Frequency')
    plt.show()
