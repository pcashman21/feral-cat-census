from tensorflow.keras.preprocessing.image import load_img, save_img 
from tensorflow.keras.preprocessing.image import img_to_array 
from tensorflow.keras.applications.vgg16 import preprocess_input 

def move_image(x, path_to_read, path_to_write, train_class_limits, test_class_limits, train_class_counts, test_class_counts):
    """
    Move image from resized_images folder to a folder structure that 
        can be used by the ImageDataGenerator class.
    x: row of dataframe containing the image file name and its class label
    path_to_read: path to directory from which to read images
    path_to_write: path to directory to save images
    train_class_limits: number of images to use for training in each class
    test_class_limits: number of images to use for testing in each class
    train_class_counts: number of images written to training directory for each class
    test_class_counts: number of images written to testing directory for each class
    """
        
    # Read in image
    image = load_img(path_to_read + x['file_path'], target_size=(224, 224))
        
    # Write image to appropriate directory.  Note that the file name is 
    # sequentially numbered in each class, which is an ImageDataGenerator requirement.
    if x['usable'] == 0:
        if train_class_counts[0] < train_class_limits[0]:
            train_class_counts[0] += 1
            save_img(path_to_write + 'train/0/' + str(train_class_counts[0]) + '.jpeg', image)  
        elif test_class_counts[0] < test_class_limits[0]:
            test_class_counts[0] += 1
            save_img(path_to_write + 'test/0/' + str(test_class_counts[0]) + '.jpeg', image)
            
    else:
        if train_class_counts[1] < train_class_limits[1]:
            train_class_counts[1] += 1
            save_img(path_to_write + 'train/1/' + str(train_class_counts[1]) + '.jpeg', image)
        elif test_class_counts[1] < test_class_limits[1]:
            test_class_counts[1] += 1
            save_img(path_to_write + 'test/1/' + str(test_class_counts[1]) + '.jpeg', image)


def make_folder_for_image_generator(df, path_to_read, path_to_write, train_test_split=0.7):
    """
    Move images from resized_images folder to a folder structure that 
        can be used by the ImageDataGenerator class.
    df: dataframe containing the image file names and their class labels
    path_to_read: path to directory from which to read images
    path_to_write: path to directory to save images
    train_test_split: proportion of images to use for training
    """
    
    # Count number of images in each class
    class_counts = df['usable'].value_counts()
    train_class_limits = [int(class_counts[0] * train_test_split), int(class_counts[1] * train_test_split)]
    test_class_limits = [class_counts[0] - train_class_limits[0], class_counts[1] - train_class_limits[1]]
    train_class_counts = [0,0]
    test_class_counts = [0,0]
    df[['usable', 'file_path']].apply(lambda x: move_image(x, path_to_read, path_to_write, train_class_limits, test_class_limits, train_class_counts, test_class_counts), axis=1)