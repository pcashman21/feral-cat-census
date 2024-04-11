from geo_cluster.get_gps import get_gps

def get_all_gps(df):
    """
    Get the gps data for all of the images in a dataframe.
    
    df: The dataframe to read.
    :return: A dataframe with the filenames and gps data for all of the images which have gps data,
       and another dataframe with the filenames and (None, None) for photos without gps data.
    
    """
    
    df['gps'] = df['filename'].apply(get_gps)
    df_with_gps = df[df['gps'] != (None, None)]
    df_without_gps = df[df['gps'] == (None, None)]
    return df_with_gps, df_without_gps