from geo_cluster.get_gps import get_gps

def get_all_gps(df, image_path_prefix):
    """
    Get the gps data for all of the images in a dataframe.
    
    df: The dataframe to read.
    image_path_prefix: The prefix for the image path.
    :return: A dataframe with the gps data for all of the images.
    If any images have no gps data, they are removed from the dataframe.
    
    """
    
    df['gps'] = df['file_path'].apply(lambda fp: get_gps(image_path_prefix + fp))
    df = df[df['gps'] != (None, None)]
    return df