import numpy as np
import tensorflow as tf
from PIL import Image
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from preprocess_data import preprocess_data
from tensorflow.keras.applications import EfficientNetB0

BATCH_SIZE = 64
EPOCHS = 50
IMG_HEIGHT, IMG_WIDTH = 224, 224
NUM_CLASSES = 2

(x_train, y_train), (x_test, y_test) = preprocess_data()

y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

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

# Load the EfficientNetB0 model
base_model = EfficientNetB0(input_shape=(IMG_HEIGHT, IMG_WIDTH, 3), include_top=False, weights='imagenet')

# Construct the new model
model = tf.keras.Sequential([
    base_model,
    tf.keras.layers.GlobalAveragePooling2D(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(NUM_CLASSES, activation='softmax')
])

# Freeze the base model layers
for layer in base_model.layers:
    layer.trainable = False

# Compile the model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Early stopping and model checkpoint callbacks
early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)
model_checkpoint = ModelCheckpoint('south_africa_segregation_best_model.h5', monitor='val_loss', save_best_only=True)

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
model.save('south_africa_segregation_best_model.h5')
