import pandas as pd
import numpy as np

def handle_missing_values(df, columns):
    """
    Handle missing values in specified columns of the DataFrame.

    Parameters:
    df (pd.DataFrame): The input DataFrame.
    columns (list): List of column names to handle missing values.

    Returns:
    pd.DataFrame: DataFrame with missing values handled.
    """
    df = df.copy()
    for column in columns:
        if df[column].isnull().all():
            print(f"Column '{column}' is entirely null. Dropping it.")
            df.drop(columns=[column], inplace=True)
        else:
            print(f"Handling missing values in column '{column}'")
            # Optionally fill missing values with mean, median, or a placeholder value
            # For numeric columns, fill with median or mean
            if df[column].dtype in [np.float64, np.int64]:
                df[column].fillna(df[column].median(), inplace=True)
            # For categorical columns, fill with mode
            elif df[column].dtype == object:
                df[column].fillna(df[column].mode()[0], inplace=True)
    return df

def handle_anomalies(df, numeric_columns, threshold=3):
    """
    Handle anomalies by identifying outliers based on Z-scores and capping or removing them.

    Parameters:
    df (pd.DataFrame): The input DataFrame.
    numeric_columns (list): List of numeric columns to check for anomalies.
    threshold (float): The Z-score threshold to identify outliers.

    Returns:
    pd.DataFrame: DataFrame with anomalies handled.
    """
    df = df.copy()
    for column in numeric_columns:
        mean = df[column].mean()
        std_dev = df[column].std()
        z_scores = (df[column] - mean) / std_dev
        df[column] = np.where(np.abs(z_scores) > threshold, np.nan, df[column])  # Replace outliers with NaN
        # Optionally, fill NaNs in numeric columns after handling outliers
        df[column].fillna(df[column].median(), inplace=True)
    return df

def clean_comments_column(df):
    """
    Clean the 'Comments' column by removing it if it is entirely null.

    Parameters:
    df (pd.DataFrame): The input DataFrame.

    Returns:
    pd.DataFrame: DataFrame with 'Comments' column cleaned.
    """
    if 'Comments' in df.columns:
        if df['Comments'].isnull().all():
            print("Column 'Comments' is entirely null. Dropping it.")
            df.drop(columns=['Comments'], inplace=True)
    return df
