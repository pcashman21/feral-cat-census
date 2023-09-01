def df_write_csv(df, file_path):
    """
    Write a dataframe to a csv file.
    
    df: The dataframe to write.
    file_path: The path to the csv file.

    """
    
    df.to_csv(file_path, index=False)