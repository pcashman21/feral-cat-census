# Test the get_gps function.
from geo_cluster.get_gps import get_gps

test_cases = [
    { 
        "file_path": "src/geo_cluster/tests/data/gps_data.jpeg", "expected": (42.58085277777778, 71.08258888888888) 
    },
    { 
        "file_path": "src/geo_cluster/tests/data/no_gps_data.jpeg", "expected": (None, None) 
    },
]


def test_get_gps():
    """
    Test the get_gps function.
    """
    for test_case in test_cases:
        assert get_gps(test_case["file_path"]) == test_case["expected"]