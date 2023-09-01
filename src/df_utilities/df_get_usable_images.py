def df_get_usable_images(df):
    """
    Get the usable images from a dataframe.
    
    df: The dataframe to read.
    :return: A dataframe with only the usable images.

    NOTE that this function does not modify the original dataframe.
    
    """
    
    return df[df['usable'] == 1]
    