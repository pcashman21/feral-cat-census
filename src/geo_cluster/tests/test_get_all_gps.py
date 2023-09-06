import pandas as pd
from geo_cluster.get_all_gps import get_all_gps

def test_get_all_gps():
    """
    Test the get_all_gps function.
    """
    df = pd.DataFrame([{'file_path': 'src/geo_cluster/tests/data/gps_data.jpeg'}, {'file_path': 'src/geo_cluster/tests/data/no_gps_data.jpeg'}])
    df = get_all_gps(df,'')
    assert df['gps'][0] == (42.58085277777778, 71.08258888888888)
    assert len(df) == 1