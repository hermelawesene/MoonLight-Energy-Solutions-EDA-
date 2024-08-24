import pandas as pd

def summary_statistics(df):
    print('reach here...')

    numeric_df = df.select_dtypes(include=['number'])
    print('reach here...')
    # Transpose summary statistics to add custom statistics
    summary = numeric_df.describe().transpose()
    
    
    print('reach here... goal')
    # #to calculate and add the mean
    # summary['mean'] = df.mean()

    # to calculate and add the median
    summary['median'] = numeric_df.median()
    print('reach here... goal1')

    #to calculate and add the standard deviation
    summary['std'] = numeric_df.std()

    # to calculate and add the variance
    summary['variance'] = numeric_df.var()
    
    return summary