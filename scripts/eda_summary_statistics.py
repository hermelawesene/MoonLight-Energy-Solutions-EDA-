import pandas as pd

def summary_statistics(df):
    print('reach here...')
    summary = df.describe().transpose()
    
    #to calculate and add the mean
    summary['mean'] = df.mean()

    # to calculate and add the median
    summary['median'] = df.median()

    #to calculate and add the standard deviation
    summary['std'] = df.std()

    # to calculate and add the variance
    summary['variance'] = df.var()
    
    return summary