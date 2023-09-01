from sklearn.cluster import DBSCAN
import numpy as np
import pandas as pd

def geo_cluster(df,epsilon,min_samples,**kwargs):
    """
    Cluster the data.
    df: A dataframe with column 'gps' which is a list of (lat, long) tuples.
    epsilon: The maximum distance between two samples for one to be considered, in miles
    min_samples: The number of samples in a neighborhood for a point to be  
    considered a core point.
    :return: The dataframe with a new column 'cluster' with the cluster labels.
    """
    
    # convert epsilon from miles to radians
    miles_per_radian = 3963.2
    epsilon /= miles_per_radian
    
    # set up the algorithm
    dbscan = DBSCAN(
        eps = epsilon,
        min_samples = min_samples,
        algorithm = 'ball_tree',
        metric = 'haversine',
        **kwargs
    )
    
    # fit the algorithm
    dbscan.fit(np.radians(df['gps'].values.tolist()))
    
    # set the cluster labels in a column in the dataframe
    df['cluster'] = dbscan.labels_

    return df