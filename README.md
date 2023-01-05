#Historical Background

Apartheid was a system of institutionalized racial segregation and discrimination that was enforced in South Africa from 1948 until the early 1990s. It was a political and social policy that was designed to maintain white supremacy and keep the black majority population in a state of subjugation. Under apartheid, the rights and freedoms of black South Africans were severely curtailed, and they were forcibly separated from white South Africans in many areas of life, including where they could live, go to school, and even use public facilities. The system of apartheid was enforced through legislation, and it was upheld by the government, the police, and the military. The regime of apartheid was eventually dismantled in the 1990s, following a long and often violent struggle by black South Africans for their rights and freedoms.

#Introduction

This project serves to use Machine Learning technologies (Convulutional Neural Networks, etc) to analyze historical photos that were reflective of the situations of racial segregation in South Africa. Through analyzing pictures and drawing conclusions about trends, we can gain more insights using quantitative methodologies. This sheds light on the past, which paves the way for truth and reconciliation in the present.

# Technologies Used

## Tensorflow

In the code, the primary technology used is TensorFlow, which is an open-source machine learning library developed by Google. TensorFlow provides a powerful set of tools for training and deploying machine learning models, including a wide variety of pre-built model architectures and optimization algorithms.

The code uses several key features of TensorFlow, including the tf.keras API, which provides a high-level interface for building and training machine learning models, and the Sequential model, which is a simple stack of layers that can be used to build a CNN.

## Convolutional Neural Network (CNN)

In this code, a convolutional neural network (CNN) is used to identify racial segregation in images. A CNN is a type of machine learning model that is particularly well-suited for image classification tasks. It is composed of multiple layers, including convolutional layers, pooling layers, and fully-connected (dense) layers.

The convolutional layers in the CNN are responsible for extracting features from the input images. They do this by applying a set of filters to the input images, which scan over the images and detect patterns and features at different scales and orientations. These filters are learned during training, and they become more and more specialized at detecting certain patterns and features as training progresses.

The pooling layers in the CNN are responsible for reducing the size of the feature maps and helping the model to focus on the most important features. They do this by applying a pooling operation to a small region of the feature map, such as taking the maximum or average value of the elements in the region.

The dense layers in the CNN are responsible for making the final classification decision based on the features extracted by the convolutional and pooling layers. They do this by taking the output of the previous layers and passing it through one or more fully-connected (dense) layers, which apply a linear transformation to the data and produce a final prediction.

## Image Capturing

The code you provided uses the requests library in Python to make an HTTP request to the Unsplash API to search for images related to a given search term. The Unsplash API is a service that allows developers to access a large collection of high-quality images for use in their projects.

The code makes an HTTP GET request to the endpoint https://api.unsplash.com/search/photos and includes a number of parameters in the query string:

query: The search term to use when searching for images.
per_page: The number of images to return in the response.
The code also includes an Authorization header with an API key, which is required to use the Unsplash API. The API key is used to identify the developer making the request and to track the usage of the API.

If the request is successful (i.e., if the HTTP status code is 200), the code processes the response data by iterating through the list of images and downloading each image using an HTTP GET request to the image URL. The image is then saved to a file on the local filesystem.
