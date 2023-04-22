import os
import numpy as np
from PIL import Image
from sklearn.model_selection import train_test_split

TARGET_SIZE = (224, 224)  # Adjust this based on your model's input size
DATA_DIR = 'data'

def resize_image(image, target_size):
    return image.resize(target_size, Image.ANTIALIAS)

def load_and_preprocess_image(image_path, target_size):
    image = Image.open(image_path)
    image = resize_image(image, target_size)
    image_array = np.array(image) / 255.0
    return image_array

def load_and_preprocess_dataset(data_dir, target_size):
    image_paths = []
    labels = []

    for label in os.listdir(data_dir):
        label_dir = os.path.join(data_dir, label)
        for image_name in os.listdir(label_dir):
            image_path = os.path.join(label_dir, image_name)
            image_paths.append(image_path)
            labels.append(label)

    images = [load_and_preprocess_image(path, target_size) for path in image_paths]
    images = np.stack(images, axis=0)

    return images, np.array(labels)

def preprocess_data():
    images, labels = load_and_preprocess_dataset(DATA_DIR, TARGET_SIZE)

    x_train, x_test, y_train, y_test = train_test_split(images, labels, test_size=0.2, stratify=labels, random_state=42)

    return (x_train, y_train), (x_test, y_test)

if __name__ == '__main__':
    (x_train, y_train), (x_test, y_test) = preprocess_data()
    print('Training data:', x_train.shape, y_train.shape)
    print('Testing data:', x_test.shape, y_test.shape)
