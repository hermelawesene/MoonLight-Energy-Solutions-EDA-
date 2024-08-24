import matplotlib.pyplot as plt

def plot_bubble_chart(df, x_column, y_column, size_column, title=None, xlabel=None, ylabel=None, size_scale=100, figsize=(10, 6)):
    """
    Plot a bubble chart for the specified columns in the DataFrame.

    Parameters:
    df (pd.DataFrame): The input DataFrame.
    x_column (str): The column name for the x-axis.
    y_column (str): The column name for the y-axis.
    size_column (str): The column name for the bubble size.
    title (str): The title of the plot.
    xlabel (str): Label for the x-axis.
    ylabel (str): Label for the y-axis.
    size_scale (int): Scaling factor for bubble sizes.
    figsize (tuple): Figure size of the plot.
    """
    plt.figure(figsize=figsize)
    
    # Normalize the size column to make bubbles appropriately scaled
    sizes = df[size_column].fillna(0) * size_scale
    
    plt.scatter(df[x_column], df[y_column], s=sizes, alpha=0.5, edgecolors='w', linewidth=0.5)
    
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()
