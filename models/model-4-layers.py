import numpy as np
import tensorflow as tf
from PIL import Image
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

# Load and preprocess the data
def load_data():
    (x_train, y_train), (x_test, y_test) = cifar10.load_data()
    return (x_train, y_train), (x_test, y_test)

def preprocess_data(x_train, x_test):
    x_train = x_train.astype('float32') / 255.0
    x_test = x_test.astype('float32') / 255.0

    y_train = to_categorical(y_train)
    y_test = to_categorical(y_test)

    return x_train, x_test

(x_train, y_train), (x_test, y_test) = load_data()
x_train, x_test = preprocess_data(x_train, x_test)

BATCH_SIZE = 64
EPOCHS = 50
IMG_HEIGHT, IMG_WIDTH = 32, 32

# Data augmentation
datagen = ImageDataGenerator(
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    horizontal_flip=True,
    validation_split=0.2
)

train_generator = datagen.flow(x_train, y_train, batch_size=BATCH_SIZE, subset='training')
validation_generator = datagen.flow(x_train, y_train, batch_size=BATCH_SIZE, subset='validation')

# Improved model architecture
model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(IMG_HEIGHT, IMG_WIDTH, 3)),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
    tf.keras.layers.Dropout(0.25),
    
    tf.keras.layers.Conv2D(64, kernel_size=(3, 3), activation='relu'),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
    tf.keras.layers.Dropout(0.25),
    
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Compile the model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Early stopping and model checkpoint callbacks
early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)
model_checkpoint = ModelCheckpoint('best_model.h5', monitor='val_loss', save_best_only=True)

callbacks = [early_stopping, model_checkpoint]

# Train the model using the data generators
model.fit(train_generator,
          steps_per_epoch=len(train_generator),
          epochs=EPOCHS,
          validation_data=validation_generator,
          validation_steps=len(validation_generator),
          callbacks=callbacks)

# Evaluate the model
_, accuracy = model.evaluate(x_test, y_test)
print('Accuracy:', accuracy)

# Save the best model
model.save('cifar10_best_model.h5')

# Functions for loading, processing, and predicting an image
def load_image(image_path, target_size):
    image = Image.open(image_path)
    image = image.resize(target_size, Image.ANTIALIAS)
    return image

def process_image(image):
    image_array = np.array(image) / 255.0
    image_array = np.expand_dims(image_array, axis=0)
    return image_array

def predict_image(model, image_path, target_size=(IMG_HEIGHT, IMG_WIDTH)):
    image = load_image(image_path, target_size)
    image_array = process_image(image)
    prediction = model.predict(image_array)
    return prediction

# Load a JPEG image, preprocess it, and make a prediction using the trained model
image_path = "path/to/your/image.jpg"
prediction = predict_image(model, image_path)
predicted_class = np.argmax(prediction)

print("Prediction:", prediction)
print("Predicted class:", predicted_class)
