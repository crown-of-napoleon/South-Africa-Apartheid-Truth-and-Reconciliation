# Historical Background

Apartheid was a system of institutionalized racial segregation and discrimination that was enforced in South Africa from 1948 until the early 1990s. It was a political and social policy that was designed to maintain white supremacy and keep the black majority population in a state of subjugation. Under apartheid, the rights and freedoms of black South Africans were severely curtailed, and they were forcibly separated from white South Africans in many areas of life, including where they could live, go to school, and even use public facilities. The system of apartheid was enforced through legislation, and it was upheld by the government, the police, and the military. The regime of apartheid was eventually dismantled in the 1990s, following a long and often violent struggle by black South Africans for their rights and freedoms.

# Introduction

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

# Disclaimer

The results and opinions generated and concluded by the code are solely for illustrative purposes and do not reflect the opinions and beliefs of the members of the contributors team or their affiliates. The contributors do not endorse any form of racial discrimination, segregation, or speeches that violate equity and human rights. The contributors hold firm beliefs that it is crucial to build a tolerant, diverse environment for everyone, regardless of race, gender, sexuality, etc. 

# Contributor Covenant Code of Conduct

## Our Pledge

We as members, contributors, and leaders pledge to make participation in our
community a harassment-free experience for everyone, regardless of age, body
size, visible or invisible disability, ethnicity, sex characteristics, gender
identity and expression, level of experience, education, socio-economic status,
nationality, personal appearance, race, religion, or sexual identity
and orientation.

We pledge to act and interact in ways that contribute to an open, welcoming,
diverse, inclusive, and healthy community.

## Our Standards

Examples of behavior that contributes to a positive environment for our
community include:

* Demonstrating empathy and kindness toward other people
* Being respectful of differing opinions, viewpoints, and experiences
* Giving and gracefully accepting constructive feedback
* Accepting responsibility and apologizing to those affected by our mistakes,
  and learning from the experience
* Focusing on what is best not just for us as individuals, but for the
  overall community

Examples of unacceptable behavior include:

* The use of sexualized language or imagery, and sexual attention or
  advances of any kind
* Trolling, insulting or derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or email
  address, without their explicit permission
* Other conduct which could reasonably be considered inappropriate in a
  professional setting

## Enforcement Responsibilities

Community leaders are responsible for clarifying and enforcing our standards of
acceptable behavior and will take appropriate and fair corrective action in
response to any behavior that they deem inappropriate, threatening, offensive,
or harmful.

Community leaders have the right and responsibility to remove, edit, or reject
comments, commits, code, wiki edits, issues, and other contributions that are
not aligned to this Code of Conduct, and will communicate reasons for moderation
decisions when appropriate.

## Scope

This Code of Conduct applies within all community spaces, and also applies when
an individual is officially representing the community in public spaces.
Examples of representing our community include using an official e-mail address,
posting via an official social media account, or acting as an appointed
representative at an online or offline event.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported to the community leaders responsible for enforcement at
wuzheyuan.86@gmail.com.
All complaints will be reviewed and investigated promptly and fairly.

All community leaders are obligated to respect the privacy and security of the
reporter of any incident.

## Enforcement Guidelines

Community leaders will follow these Community Impact Guidelines in determining
the consequences for any action they deem in violation of this Code of Conduct:

### 1. Correction

**Community Impact**: Use of inappropriate language or other behavior deemed
unprofessional or unwelcome in the community.

**Consequence**: A private, written warning from community leaders, providing
clarity around the nature of the violation and an explanation of why the
behavior was inappropriate. A public apology may be requested.

### 2. Warning

**Community Impact**: A violation through a single incident or series
of actions.

**Consequence**: A warning with consequences for continued behavior. No
interaction with the people involved, including unsolicited interaction with
those enforcing the Code of Conduct, for a specified period of time. This
includes avoiding interactions in community spaces as well as external channels
like social media. Violating these terms may lead to a temporary or
permanent ban.

### 3. Temporary Ban

**Community Impact**: A serious violation of community standards, including
sustained inappropriate behavior.

**Consequence**: A temporary ban from any sort of interaction or public
communication with the community for a specified period of time. No public or
private interaction with the people involved, including unsolicited interaction
with those enforcing the Code of Conduct, is allowed during this period.
Violating these terms may lead to a permanent ban.

### 4. Permanent Ban

**Community Impact**: Demonstrating a pattern of violation of community
standards, including sustained inappropriate behavior,  harassment of an
individual, or aggression toward or disparagement of classes of individuals.

**Consequence**: A permanent ban from any sort of public interaction within
the community.

# Contributions

All contributions, bug reports, bug fixes, documentation improvements, enhancements, and ideas are welcome.
