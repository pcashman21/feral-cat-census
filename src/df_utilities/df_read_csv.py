import pandas as pd

def df_read_csv(file_path):
    """
    Read a csv file into a dataframe.
    
    file_path: The path to the csv file.
    :return: A dataframe.
    
    """
    
    df = pd.read_csv(file_path)
    return df