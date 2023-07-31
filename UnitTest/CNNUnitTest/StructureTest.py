import unittest
import tensorflow as tf

class TestModelStructure(unittest.TestCase):
    def setUp(self):
        '''
        Define the model architecture.
        '''
        self.model = tf.keras.Sequential([
            tf.keras.layers.Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(224, 224, 3)),
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
            tf.keras.layers.Dense(2, activation='softmax')
        ])

    def test_number_of_layers(self):
        self.assertEqual(len(self.model.layers), 11)  # CNN model should have 11 layers.

    def test_first_layer(self):
        layer = self.model.layers[0]
        self.assertEqual(type(layer), tf.keras.layers.Conv2D)  # First layer should be Conv2D
        self.assertEqual(layer.filters, 32)  # The number of filters should be 32
        self.assertEqual(layer.kernel_size, (3, 3))  # The kernel size should be 3x3

    # Add more tests as needed to check other layer properties


# Run the tests
unittest.main(argv=[''], exit=False)
