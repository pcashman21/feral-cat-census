import os
import sys
# import turtle
import matplotlib.pyplot as plt
import pandas as pd


def classify_usability_folder(image_path,folder_name):
    """
    This function takes in a folder of images and asks the user to classify each image as usable or not usable.
    The user input is saved in a csv file.
        image_path: path to folder of images
        folder_name: name of folder to save csv file
    """
    df = pd.DataFrame({'usable':[]})
    image_files = os.listdir(image_path)
    image_files = [image_file for image_file in image_files if image_file.endswith('.jpg')]
    image_files.sort()
    for image_file in image_files:
        # image_file_path = os.path.join(image_path,image_file)
        # image = plt.imread(image_file_path)
        # plt.ion()
        # plt.show()
        # plt.imshow(image)
        # plt.pause(0.001)
        # usability = turtle.textinput("Usability", 'Is the image usable? (y/n)')
        # if usability == 'y' or usability == '':
        #     usability = 1
        # else:
        #     usability = 0
        # Add row to dataframe at new index
        df.loc[image_file] = {'usable': 1}

    # Save dataframe to csv file
    last_item = folder_name.split('/')[-2]
    last_folder_number = last_item.split('_')[-1]
    df.to_csv(os.path.join(folder_name,'usability_' + last_folder_number + '.csv'),mode='w',header=True,index=True)

if __name__ == '__main__':
    images = sys.argv[1]
    folder = sys.argv[2]

    # Use turtle graphics to get the user input on usability.  Just using Python "input" method
    # causes an EOF error.  See the following link for more details:
    # See https://www.reddit.com/r/learnpython/comments/jht9pr/eof_error_while_calling_a_input_function_in/
    # sc = turtle.Screen()
    # sc.setup(800,600)
    classify_usability_folder(images,folder)

# Example usage:
# python manual_usability_classifier.py /Users/Paul/Documents/CAT_00/ /Users/Paul/Documents/CAT_00/
