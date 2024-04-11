import glob
import os
import pandas as pd
from geo_cluster.get_all_gps import get_all_gps
from geo_cluster import geo_cluster

def main():
    """
    Main function.  Takes photos from a given location and generates geoclusters.

    Output: a CSV file named image_index_with_gps_and_clusters.csv, in the directory with the photos,
    where the CSV file has columns:

        filename: Full pathname of a photo file
        gps: (latitude, longitude) of photo, or (None, None) if no GPS data present
        cluster: integer cluster ID from DBSCAN, starting at 1 if photo had GPS data.
            If photo had no GPS data, cluster ID is 0.
    
    """
    # Prefix for the image path.
    original_photo_path_prefix = '/Users/Paul/Documents/Documents - Paul Cashman’s MacBook Pro/Machine Learning/feral-cat-census/data/box_downloads/'
    # Radius in miles of the roaming area of a cat.
    roaming_radius = 1
    # Minimum number of images in a cluster.
    min_cluster_size = 3
    
    # Get a list of all the original photos and make a dataframe out of it
    files_jpg = glob.glob(os.path.join(original_photo_path_prefix, '*.jpg')) + glob.glob(os.path.join(original_photo_path_prefix, '*.JPG'))
    files_jpeg = glob.glob(os.path.join(original_photo_path_prefix, '*.jpeg')) + glob.glob(os.path.join(original_photo_path_prefix, '*.JPEG'))
    files_png = glob.glob(os.path.join(original_photo_path_prefix, '*.png')) + glob.glob(os.path.join(original_photo_path_prefix, '*.PNG'))
    original_photo_names = sorted(files_jpg + files_jpeg + files_png)
    df = pd.DataFrame(original_photo_names, columns=['filename'])

    # Get the image coordinates.  Some photos may not have GPS data.
    df_with_gps, df_without_gps = get_all_gps(df)
    print(f'Loaded {len(df_with_gps)} photos with GPS data and {len(df_without_gps)} without GPS data')
    
    # Cluster the data for photos with GPS data
    if len(df_with_gps) > 0:
        df_with_gps = geo_cluster.geo_cluster(df_with_gps, epsilon = roaming_radius, min_samples=min_cluster_size)
    
    # Set cluster ID to 0 for photos without GPS data
    df_without_gps['cluster'] = 0

    # Merge the dataframes
    df_merged = pd.concat([df_without_gps, df_with_gps], ignore_index=True)
    # Force the cluster ID to be an integer, not a float
    df_merged['cluster'] = df_merged['cluster'].astype(int)
    
    # Write the data to a csv file.
    df_merged.to_csv(os.path.join(original_photo_path_prefix, 'image_index_with_gps_and_clusters.csv'), index=False)


main()