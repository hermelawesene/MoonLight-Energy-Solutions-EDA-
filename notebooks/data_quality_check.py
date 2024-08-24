import pandas as pd
import numpy as np

def check_missing_values(df):
    """
    Check for missing values in the DataFrame.

    Parameters:
    df (pd.DataFrame): The input DataFrame.

    Returns:
    pd.DataFrame: A DataFrame showing the count and percentage of missing values per column.
    """
    missing_count = df.isnull().sum()
    missing_percentage = (missing_count / len(df)) * 100
    missing_data = pd.DataFrame({'Missing Count': missing_count, 'Missing Percentage': missing_percentage})
    
    return missing_data[missing_data['Missing Count'] > 0]

def check_incorrect_entries(df):
    """
    Check for incorrect entries, such as negative values where only positives should exist.

    Parameters:
    df (pd.DataFrame): The input DataFrame.

    Returns:
    pd.DataFrame: A DataFrame indicating any columns with incorrect entries.
    """
    incorrect_entries = pd.DataFrame()

    # Check for negative values in columns that should only have positive values
    columns_to_check = ['GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'WS', 'WSgust']
    for column in columns_to_check:
        incorrect_entries[column] = df[column].apply(lambda x: x if x >= 0 else np.nan)

    return df[incorrect_entries.isnull().any(axis=1)]

def detect_outliers(df, columns):
    """
    Detect outliers using the Z-score method.

    Parameters:
    df (pd.DataFrame): The input DataFrame.
    columns (list): List of columns to check for outliers.

    Returns:
    pd.DataFrame: A DataFrame with outliers flagged in the specified columns.
    """
    outliers = pd.DataFrame()
    
    for column in columns:
        z_scores = (df[column] - df[column].mean()) / df[column].std()
        outliers[column] = df[column].where(z_scores.abs() <= 3, np.nan)
        
    return df[outliers.isnull().any(axis=1)]
