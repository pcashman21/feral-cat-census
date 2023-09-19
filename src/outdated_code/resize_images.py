from tensorflow.keras.preprocessing.image import load_img, save_img 
from tensorflow.keras.preprocessing.image import img_to_array 
from tensorflow.keras.applications.vgg16 import preprocess_input 

def resize_image(file, path_to_read, path_to_write):
    """
    Resizes and normalizes one image in a directory to 224x224 pixels and saves it to a new directory.
    file: name of file to resize
    path_to_read: path to directory containing file
    path_to_write: path to directory to save resized file
    """
    print('Resizing ' + file)
    image = load_img(path_to_read + file, target_size=(224, 224))
    image = img_to_array(image)

    # preprocess the image by scaling the pixel values to [-1, 1], 
    # and zero-centering each RGB channel with respect to the ImageNet dataset, without scaling
    image = preprocess_input(image)
    save_img(path_to_write + file, image)
