import pandas as pd
import matplotlib.pyplot as plt

def calculate_cleaning_impact(df, sensor_column, cleaning_column='Cleaning'):
    """
    Calculate the difference in sensor readings before and after cleaning events.

    Parameters:
    df (pd.DataFrame): The input DataFrame with a datetime index.
    sensor_column (str): The name of the sensor column (ModA or ModB).
    cleaning_column (str): The name of the cleaning column, default is 'Cleaning'.

    Returns:
    pd.DataFrame: A DataFrame showing the sensor readings before and after cleaning events.
    """
    # Find the index of rows where cleaning occurred
    cleaning_indices = df[df[cleaning_column] == 1].index
    
    # Calculate sensor readings before and after cleaning
    before_cleaning = df[sensor_column].shift(1).loc[cleaning_indices]
    after_cleaning = df[sensor_column].loc[cleaning_indices]

    impact_df = pd.DataFrame({
        'Before Cleaning': before_cleaning,
        'After Cleaning': after_cleaning,
        'Difference': after_cleaning - before_cleaning
    })
    
    return impact_df

def plot_cleaning_impact(impact_df, sensor_column, title="Impact of Cleaning on Sensor Readings", figsize=(10, 6)):
    """
    Plot the impact of cleaning on sensor readings.

    Parameters:
    impact_df (pd.DataFrame): The DataFrame returned by calculate_cleaning_impact().
    sensor_column (str): The name of the sensor column (ModA or ModB).
    title (str): The title of the plot.
    figsize (tuple): Figure size of the plot.
    """
    impact_df[['Before Cleaning', 'After Cleaning']].plot(kind='bar', figsize=figsize)
    plt.title(title)
    plt.xlabel("Cleaning Event")
    plt.ylabel(sensor_column + " Reading")
    plt.show()
