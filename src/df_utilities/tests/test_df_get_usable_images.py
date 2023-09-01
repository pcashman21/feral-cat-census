import pandas as pd
from df_utilities import df_get_usable_images

def test_get_usable_images():
    df = pd.DataFrame({'usable': [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]})
    original_length = len(df)
    usable_df = df_get_usable_images.df_get_usable_images(df)
    assert usable_df['usable'].sum() == 5
    # Insure that the original dataframe was not modified.
    assert len(df) == original_length