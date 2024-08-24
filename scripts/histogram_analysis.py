import pandas as pd
import matplotlib.pyplot as plt

def plot_histogram(df, column_name, bins=30, title=None, xlabel=None, ylabel='Frequency', figsize=(10, 6)):
    """
    Plot a histogram for a given column.

    Parameters:
    df (pd.DataFrame): The input DataFrame.
    column_name (str): The name of the column to plot.
    bins (int): Number of bins for the histogram.
    title (str): The title of the plot.
    xlabel (str): Label for the x-axis.
    ylabel (str): Label for the y-axis.
    figsize (tuple): Figure size of the plot.
    """
    plt.figure(figsize=figsize)
    plt.hist(df[column_name].dropna(), bins=bins, edgecolor='k', alpha=0.7)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()

def plot_multiple_histograms(df, columns, bins=30, figsize=(15, 10)):
    """
    Plot histograms for multiple columns in a single figure.

    Parameters:
    df (pd.DataFrame): The input DataFrame.
    columns (list): List of column names to plot.
    bins (int): Number of bins for the histograms.
    figsize (tuple): Figure size of the plot.
    """
    num_columns = len(columns)
    plt.figure(figsize=figsize)
    
    for i, column in enumerate(columns):
        plt.subplot(num_columns, 1, i + 1)
        plt.hist(df[column].dropna(), bins=bins, edgecolor='k', alpha=0.7)
        plt.title(f'Histogram of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.grid(True)
    
    plt.tight_layout()
    plt.show()
