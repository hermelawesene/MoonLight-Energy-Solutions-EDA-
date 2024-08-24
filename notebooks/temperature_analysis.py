import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_temperature_vs_rh(df, temperature_column='Tamb', rh_column='RH', title="Temperature vs Relative Humidity", figsize=(10, 6)):
    """
    Plot a scatter plot to visualize the relationship between temperature and relative humidity.

    Parameters:
    df (pd.DataFrame): The input DataFrame.
    temperature_column (str): The name of the temperature column.
    rh_column (str): The name of the relative humidity column.
    title (str): The title of the plot.
    figsize (tuple): Figure size of the plot.
    """
    plt.figure(figsize=figsize)
    sns.scatterplot(x=df[rh_column], y=df[temperature_column])
    plt.title(title)
    plt.xlabel('Relative Humidity (%)')
    plt.ylabel('Temperature (°C)')
    plt.show()

def plot_temperature_vs_solar_radiation(df, temperature_column='Tamb', solar_radiation_column='GHI', title="Temperature vs Solar Radiation", figsize=(10, 6)):
    """
    Plot a scatter plot to visualize the relationship between temperature and solar radiation.

    Parameters:
    df (pd.DataFrame): The input DataFrame.
    temperature_column (str): The name of the temperature column.
    solar_radiation_column (str): The name of the solar radiation column.
    title (str): The title of the plot.
    figsize (tuple): Figure size of the plot.
    """
    plt.figure(figsize=figsize)
    sns.scatterplot(x=df[solar_radiation_column], y=df[temperature_column])
    plt.title(title)
    plt.xlabel('Solar Radiation (W/m²)')
    plt.ylabel('Temperature (°C)')
    plt.show()

def plot_rh_vs_solar_radiation(df, rh_column='RH', solar_radiation_column='GHI', title="Relative Humidity vs Solar Radiation", figsize=(10, 6)):
    """
    Plot a scatter plot to visualize the relationship between relative humidity and solar radiation.

    Parameters:
    df (pd.DataFrame): The input DataFrame.
    rh_column (str): The name of the relative humidity column.
    solar_radiation_column (str): The name of the solar radiation column.
    title (str): The title of the plot.
    figsize (tuple): Figure size of the plot.
    """
    plt.figure(figsize=figsize)
    sns.scatterplot(x=df[solar_radiation_column], y=df[rh_column])
    plt.title(title)
    plt.xlabel('Solar Radiation (W/m²)')
    plt.ylabel('Relative Humidity (%)')
    plt.show()
