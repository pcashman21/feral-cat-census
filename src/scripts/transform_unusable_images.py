import os
import sys
import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf
from tensorflow.keras import layers


def transform_one_unusable_image(row, path_to_read, path_to_write, transformer, number_of_transforms):
    """
    This function takes in an image and creates a number of transforms of the image.

    row: row of dataframe with image name and usability
    path_to_read: path to folder of images
    path_to_write: path to folder to save transformed images
    transformer: image transformer object
    number_of_transforms: number of transforms to create
    Returns:
        dataframe with transformed images
    """

    image_file = row['filename']
    image_folder = row['folder']
    image_file_path = os.path.join(path_to_read,image_folder,image_file)
    image = plt.imread(image_file_path)
    image_file_name = image_file.split('.')[0]
    image_file_extension = image_file.split('.')[1]
    image_file_name_transformed_root = image_file_name + '_transformed_'
    df_generated_unusable = pd.DataFrame({'filename':[], 'usable':[], 'folder':[], 'generated': []})
    
    for i in range(number_of_transforms):
        image_file_name_transformed = image_file_name_transformed_root + str(i) + '.' + image_file_extension
        image_file_path_transformed = os.path.join(path_to_write,image_folder, image_file_name_transformed)
        image_transformed = transformer(image)
        # Convert tensor to numpy array and save
        plt.imsave(image_file_path_transformed,image_transformed.numpy())
        gen_df = pd.DataFrame({'filename':[image_file_name_transformed], 'usable':[0], 'folder':[image_folder], 'generated': [1]})
        df_generated_unusable = pd.concat([df_generated_unusable, gen_df], axis=0, ignore_index=True)
    return df_generated_unusable


def transform_unusable_images(df, path_to_read, path_to_write, transformer, number_of_transforms):
    """
    This function takes in a dataframe, selects the unusable images, creates a number of 
    transforms of each unusable image, and saves the transforms to a folder.

    df: dataframe with image names and usability
    path_to_read: path to folder of images
    path_to_write: path to folder to save transformed images
    transformer: image transformer object
    number_of_transforms: number of transforms to create

    Returns:
        updated dataframe with transformed images
    """

    # Select unusable images and transform them
    df['generated'] = 0 # Add column to indicate if image is generated
    # Since transform_one_unusable_image returns a dataframe with multiple rows, we can't
    # use a lambda to iterate, as 'apply' will try to stuff the result in the row
    # which is the lambda argument. 
    for i in range(len(df)):
      if df['usable'].iloc[i] == 0 and df['generated'].iloc[i] == 0:
        df_generated_unusables = transform_one_unusable_image(df.iloc[i], path_to_read, path_to_write, transformer, number_of_transforms)
        df = pd.concat([df, df_generated_unusables], axis=0, ignore_index=True)
    return df


if __name__ == '__main__':
    IMG_SIZE = 244
    NUMBER_OF_TRANSFORMS = 20

    transformer_nn = tf.keras.Sequential([
        layers.Resizing(IMG_SIZE, IMG_SIZE),
        layers.Rescaling(1./255),
        layers.RandomFlip("horizontal_and_vertical"),
        layers.RandomRotation(0.2),
        layers.RandomTranslation(0.3, 0.3),
        layers.RandomZoom(0.2)
    ])

    path_to_read_arg = sys.argv[1]
    path_to_write_arg = sys.argv[2]
    df = pd.read_csv(os.path.join(path_to_read_arg,'usability_00_01_done.csv'))
    df.columns = ['filename','usable','folder']
    df = transform_unusable_images(df, path_to_read_arg, path_to_write_arg, transformer_nn, NUMBER_OF_TRANSFORMS)
    df.to_csv(os.path.join(path_to_write_arg,'usability_00_01_augmented_done.csv'),mode='w',header=True,index=False)
