import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

def plot_correlation_heatmap(df, columns, title="Correlation Heatmap", figsize=(10, 8)):
    """
    Plot a heatmap to visualize correlations between specified columns.

    Parameters:
    df (pd.DataFrame): The input DataFrame.
    columns (list): List of column names to include in the correlation matrix.
    title (str): The title of the heatmap.
    figsize (tuple): Figure size of the heatmap.
    """
    correlation_matrix = df[columns].corr()
    plt.figure(figsize=figsize)
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title(title)
    plt.show()

def plot_pairplot(df, columns, title="Pair Plot"):
    """
    Plot pair plots to visualize pairwise relationships between specified columns.

    Parameters:
    df (pd.DataFrame): The input DataFrame.
    columns (list): List of column names to include in the pair plot.
    title (str): The title of the pair plot.
    """
    sns.pairplot(df[columns])
    plt.suptitle(title, y=1.02)
    plt.show()

def plot_scatter_matrix(df, columns, title="Scatter Matrix", figsize=(12, 10)):
    """
    Plot a scatter matrix to visualize relationships between specified columns.

    Parameters:
    df (pd.DataFrame): The input DataFrame.
    columns (list): List of column names to include in the scatter matrix.
    title (str): The title of the scatter matrix.
    figsize (tuple): Figure size of the scatter matrix.
    """
    scatter_matrix(df[columns], figsize=figsize, diagonal='kde')
    plt.suptitle(title)
    plt.show()
