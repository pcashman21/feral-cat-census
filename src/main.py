from df_utilities.df_get_usable_images import df_get_usable_images
from df_utilities.df_read_csv import df_read_csv
from df_utilities.df_write_csv import df_write_csv
from geo_cluster.get_all_gps import get_all_gps
from geo_cluster import geo_cluster

def main():
    """
    Main function.
    
    """
    # Prefix for the image path.
    image_path_prefix = '/Users/Paul/Documents/Documents - Paul Cashman’s MacBook Pro/Machine Learning/feral-cat-census/data/original_images/'
    # Radius in miles of the roaming area of a cat.
    roaming_radius = 1
    # Minimum number of images in a cluster.
    min_cluster_size = 3


    # Read the image index into a dataframe.
    df = df_read_csv(image_path_prefix + 'image_index.csv')

    # Get only rows with usable images (i.e., images that have
    # only one cat).
    usable_df  = df_get_usable_images(df)

    # Get the image coordinates.
    usable_df = get_all_gps(usable_df, image_path_prefix)
    
    # Cluster the data.
    df = geo_cluster.geo_cluster(usable_df, epsilon = roaming_radius, min_samples=min_cluster_size)
    
    # Write the data to a csv file.
    df_write_csv(usable_df, image_path_prefix + 'image_index_with_gps_and_clusters.csv')


main()