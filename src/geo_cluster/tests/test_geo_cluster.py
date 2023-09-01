from geo_cluster.geo_cluster import geo_cluster
import pandas as pd

def test_geo_cluster():
    """
    Test the geo_cluster function.
    """
    # Create a dataframe with a column 'gps' which is a list of (lat, long) tuples.
    df = pd.DataFrame({'gps': [(42.263818, -73.062077),(42.263818, -73.062077),(42.5, -73.0),(42.263818, 73.062077),(42.263818, 73.062077)]})
    # Cluster the data.
    df = geo_cluster(df, epsilon = 1, min_samples=2)
    # Check that the cluster labels are as expected.
    assert df['cluster'].tolist() == [0,0,-1,1,1]