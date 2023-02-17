def get_lower_and_upper_bounds(series,multiplier):
    Q3 = np.quantile(series, 0.75)
    Q1 = np.quantile(series, 0.25)
    iqr = Q3 - Q1
    
    upper_bound = Q3+(multiplier*iqr)
    lower_bound = Q1-(multiplier*iqr)
    
    return lower_bound, upper_bound

def isolate_outliers(series):
    '''
    Parameters
    ----------
    series : DataFrame column
        Array of sample data.

    Returns
    -------
    series : DataFrame column
        The outliers which are defined as
        being 3 standard deviations outside the mean.
    '''
    SD = df.std()
    norm_median = df.median()
    
    outside_of_three_sd = df[(df <= (norm_median-(SD*3))) & (df >= (norm_median+(SD*3)))]
    
    return outside_of_three_sd
