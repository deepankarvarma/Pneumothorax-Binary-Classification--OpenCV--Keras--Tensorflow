# Pneumothorax Detection Using Binary Image Classification

This repository contains code for generating a model to detect pneumothorax from user-uploaded images using the ResNet-50 V2 architecture. The project focuses on binary image classification, specifically distinguishing between images with pneumothorax and images without pneumothorax. The repository includes several essential steps to train and evaluate the model.

## Dataset

The dataset used in this project can be downloaded from [this link](https://www.kaggle.com/datasets/volodymyrgavrysh/pneumothorax-binary-classification-task?select=small_train_data_set). It provides a collection of images for both classes: with pneumothorax and without pneumothorax.

## Repository Structure and Steps

1. `imagesplitting.py`: This step involves splitting the dataset images into training and validation sets. It ensures proper allocation of data for training and evaluation purposes.

2. `imageaugmentation.py`: The augmentation step enhances the dataset by applying transformations to existing images. It helps improve the model's ability to generalize and handle variations in input images.

3. `train_val_split.py`: This step splits the augmented dataset into training and validation subsets. It enables model training on the training set and validation for evaluating model performance.

4. `model.py`: The model creation step involves defining and building the binary classification model architecture. It utilizes the ResNet-50 V2 pre-trained model as the base architecture for detecting pneumothorax.

5. `app.py`: The Streamlit application allows users to upload their own images and utilizes the trained model to predict if the image contains pneumothorax or not.

## Usage

To use this repository and detect pneumothorax from images, follow these steps:

1. Download the dataset from the provided link and place it in a folder named `dataset`.

2. Execute the scripts in the given order: `imagesplitting.py`, `imageaugmentation.py`, `train_val_split.py`, `model.py`.

3. Once the model is trained, run the Streamlit application using `app.py`. It will open a web interface where you can upload your own images.

4. Upload an image through the application and click the "Predict" button. The model will analyze the image and provide a prediction if the image contains pneumothorax or not.

Feel free to explore the code, modify it, and experiment with different model architectures or techniques to improve the detection accuracy.

## Contributing

Contributions to this repository are highly welcome. If you have any ideas, suggestions, or improvements, please feel free to fork the repository and submit a pull request. Let's collaborate to enhance the pneumothorax detection model!

## License

This project is licensed under the [MIT License](LICENSE). You are free to use and modify the code for your own purposes.
