from tensorflow.keras.models import Model
import matplotlib.pyplot as plt

# Choose a sample image from your dataset
sample_image = x_train[0]
sample_image = np.expand_dims(sample_image, axis=0)

# Create a new model for each layer you want to visualize
outputs = [layer.output for layer in model.layers]
vis_model = Model(inputs=model.inputs, outputs=outputs)

# Get the feature maps for the sample image
feature_maps = vis_model.predict(sample_image)

# Function to plot feature maps
def plot_feature_maps(feature_maps):
    plt.figure(figsize=(15, 15))
    for i, feature_map in enumerate(feature_maps):
        plt.subplot(6, 6, i+1) # assuming the model has 36 layers
        plt.imshow(feature_map[0, :, :, 0], cmap='viridis')
        plt.axis('off')
    plt.tight_layout()
    plt.show()

# Visualize feature maps
plot_feature_maps(feature_maps)
