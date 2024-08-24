import pandas as pd
import matplotlib.pyplot as plt

def plot_line_graph(df, columns, title="Time Series Line Plot", xlabel="Timestamp", ylabel="Value", figsize=(10, 6)):
    """
    Plot line graphs for specified columns over time.

    Parameters:
    df (pd.DataFrame): The input DataFrame with a datetime index.
    columns (list): List of column names to plot.
    title (str): The title of the plot.
    xlabel (str): Label for the x-axis.
    ylabel (str): Label for the y-axis.
    figsize (tuple): Figure size of the plot.
    """
    df[columns].plot(figsize=figsize)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend(columns)
    plt.show()

# def plot_area_graph(df, columns, title="Time Series Area Plot", xlabel="Timestamp", ylabel="Value", figsize=(10, 6)):
#     """
#     Plot area graphs for specified columns over time.

#     Parameters:
#     df (pd.DataFrame): The input DataFrame with a datetime index.
#     columns (list): List of column names to plot.
#     title (str): The title of the plot.
#     xlabel (str): Label for the x-axis.
#     ylabel (str): Label for the y-axis.
#     figsize (tuple): Figure size of the plot.
#     """
#     df[columns].plot.area(figsize=figsize, alpha=0.6)
#     plt.title(title)
#     plt.xlabel(xlabel)
#     plt.ylabel(ylabel)
#     plt.legend(columns)
#     plt.show()
def plot_area_graph(df, columns, title="Time Series Area Plot", xlabel="Timestamp", ylabel="Value", figsize=(10, 6)):
    # Separate positive and negative values
    df_positive = df[columns].clip(lower=0)
    df_negative = df[columns].clip(upper=0)
    
    # Use valid color names or HEX codes
    ax = df_positive.plot.area(figsize=figsize, alpha=0.6, color=['blue', 'green', 'red', 'orange'])
    df_negative.plot.area(ax=ax, figsize=figsize, alpha=0.6, color=['lightblue', 'lightgreen', 'lightcoral', '#FFA07A'])  # '#FFA07A' is light orange
    
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()