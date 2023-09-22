# feral-cat-census

# Source directory structure

Each directory under `/src/` has an `__init__.py` file, so `pytest` can find all
the source modules imported for tests.  See https://stackoverflow.com/questions/25827160/importing-correctly-with-pytest.

# Creating the usable/unusable images classification model

## Preparatory manual work

I obtained from `kaggle.com` a set of about 10K cat images (see https://www.kaggle.com/datasets/crawford/cat-dataset).  There are six folders named CAT_00, CAT_01, etc., with about 1600 images in each.  I went through the CAT_00 folder and created a dataframe (df) with columns `filename`, `usable`, and `folder`:

`filename`:     The name of the image file, e.g., `00000001_005.jpg`
`usable`:       1 if a usable image (i.e., exactly one cat), 0 if not
`folder`:       `CAT_00`, `CAT_01`, etc.

This df was stored in the `feral-cat-census/data/kaggle_cats` folder on my laptop with the name `usability_00_01.csv`.

I then went through the `CAT_01` folder and identified all the unusable images.  I added these to the `usability_00_01.csv` file.

At this point I moved all the files in CAT_00 and CAT_01 to my Google drive at `My Drive/Cat images/kaggle_cats`.

## Generating unusable images

The Kaggle dataset was heavily weighted to usable images (about 98%).  To remedy this, I wrote the notebook `src/notebooks/generate_unusable_images.ipynb`.  This reads the CSV file `usability_master.csv` (the renamed `usability_00_01.csv`), finds the unusable images, and applies a transformation to each one N times to create N transformed unusable images from the original one.  These are written to the folder of the original, and are recorded in the df with the added column `generated` set to 1 (the column is initialized to 0 for all rows).  After running this one-time notebook, `CAT_00` and `CAT_01` have a sufficient number of additional tramsformed copies of the unusable images so that, using the usable images in `CAT_00`, we have a balanced set of about 3400 images to use as training and test data.  Additionally, `usability_master.csv` has a record of the original and added files.

## Moving the files to an ImageDataGenerator structure

The `move_files_to_idg_folder.ipynb` notebook does the train/test split on the images named in the df created from `usability_master.csv` and moves them into a file structure appropriate for the Tensorflow ImageDataGenerator class.  This is found at the Google drive `My Drive/Cat images/ImageDataGenerator_images`.  The immediate subfolders are `train` and `test` and each one has the same substructure, namely, folders `usable` and `unusable`.  Within each of these folders, the files are numbered consecutively (`1.jpg`, `2.jpg`, etc.).

## Training the usable/unusable model

Once the images have been moved into the ImageDataGenerator file structure, I ran the `SelectUsableImages.ipynb` notebook.  This takes a pre-trained VGG model without its top layers, adds new classification layers, trains it on the `usable` and `unusable` images passed by the ImageDataGenerator, gets the classification and confusion matrices, and saves the model at `My Drive/Cat images/models/select_usable_images.keras`.  

It then loads the saved model and does a prediction on a selected (transformed) image.

# Google Drive file structure

Google Drive holds the data used in model creation and testing.  The directory structure is as follows:

`Cat images`                        Main folder for all feral-cat-census project data
    `original_images`               Raw jpegs of Cashman cats (not used)
    `resized_images`                Resized jpegs of Cashman cats (not used)
    `kaggle_cats`                   Folders with Kaggle cats images
    `ImageDataGenerator_images`     Subset of Kaggle cats images (from CAT_00 
                                    principally) organized into `train` and `test` 
                                    folders, and thence into the two classes `usable` and
                                    `unusable` for training the usable/unusable image 
                                    model
    `models`                        Holds the saved usable/unusable images model
    `cluster_test_data`             Folders to hold test data for image clustering code
        `case_1`,...,`case_N`       Folder holding data for each test case (see below)

# Image clustering test cases

Each dataset is assumed to be one geocluster, and the purpose is to figure out the number 
of unique cats in each geocluster.  The test cases aim to have different kinds of 
distributions of unique cats.

`Case` `Description`                        `Images` `Unique` `Im 1` `Im 2` `Im 3` `Im 4` `Im 5`
   1    All unique                              5       5        1      1      1      1      1
   2    All the same                            5       1        5
   3    Lopsided, with multiple unique         10       5        6      1      1      1      1
   4    Equal # of multiple image copies       10       5        2      2      2      2      2
   5    Very lopsided, 2 unique                10       2        9      1

The notebook `src/notebooks/generate_cluster_test_data.ipynb` will generate the test data 
as above.

# Image clustering notebook

`src/notebooks/cluster_images.ipynb` is the notebook for clustering images.  It is set up
to retrieve all the files in a given folder, extract rhe features from the image in each
file in the folder, do a principal components analysis on the features, do a
series of K-means clusterings where the number of clusters ranges from 1 to the number of 
images, and display a graph of the number of clusters vs. the inertia (the sum of 
distances, within a cluster, from the cluster centroid to each point in the cluster).  
The deflection point of this `elbow diagram` should indicate the optimal number of 
clusters, and thus the number of unique images (i.e., cats) within the dataset.




