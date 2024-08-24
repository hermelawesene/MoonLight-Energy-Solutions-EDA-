import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def calculate_z_scores(df, column_name):
    """
    Calculate Z-scores for a specified column in the DataFrame.

    Parameters:
    df (pd.DataFrame): The input DataFrame.
    column_name (str): The name of the column for which Z-scores are calculated.

    Returns:
    pd.Series: Z-scores for the specified column.
    """
    mean = df[column_name].mean()
    std_dev = df[column_name].std()
    z_scores = (df[column_name] - mean) / std_dev
    return z_scores

def flag_outliers(df, column_name, threshold=3):
    """
    Flag outliers in the DataFrame based on Z-scores.

    Parameters:
    df (pd.DataFrame): The input DataFrame.
    column_name (str): The name of the column to check for outliers.
    threshold (float): The Z-score threshold to flag outliers.

    Returns:
    pd.DataFrame: DataFrame with an additional column 'Outlier_Flag' indicating outliers.
    """
    df = df.copy()
    z_scores = calculate_z_scores(df, column_name)
    df['Outlier_Flag'] = np.where(np.abs(z_scores) > threshold, 'Outlier', 'Normal')
    return df

def print_outlier_summary(df, column_name):
    """
    Print a summary of outliers for the specified column.

    Parameters:
    df (pd.DataFrame): The input DataFrame.
    column_name (str): The name of the column to summarize.
    """
    outlier_count = df[df['Outlier_Flag'] == 'Outlier'].shape[0]
    normal_count = df[df['Outlier_Flag'] == 'Normal'].shape[0]
    print(f"Outliers in '{column_name}': {outlier_count}")
    print(f"Normal values in '{column_name}': {normal_count}")



def plot_z_scores(df, column_name):
    """
    Plot Z-scores for a given column.

    Parameters:
    df (pd.DataFrame): The input DataFrame.
    column_name (str): The name of the column to plot.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df[column_name + '_Z_Score'], label=f'Z-Scores of {column_name}', color='blue')
    plt.axhline(y=3, color='red', linestyle='--', label='Threshold')
    plt.axhline(y=-3, color='red', linestyle='--')
    plt.title(f'Z-Scores for {column_name}')
    plt.xlabel('Date')
    plt.ylabel('Z-Score')
    plt.legend()
    plt.show()
