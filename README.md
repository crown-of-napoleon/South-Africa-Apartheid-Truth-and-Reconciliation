# Historical Background

Apartheid was a system of institutionalized racial segregation and discrimination that was enforced in South Africa from 1948 until the early 1990s. It was a political and social policy that was designed to maintain white supremacy and keep the black majority population in a state of subjugation. Under apartheid, the rights and freedoms of black South Africans were severely curtailed, and they were forcibly separated from white South Africans in many areas of life, including where they could live, go to school, and even use public facilities. The system of apartheid was enforced through legislation, and it was upheld by the government, the police, and the military. The regime of apartheid was eventually dismantled in the 1990s, following a long and often violent struggle by black South Africans for their rights and freedoms.

The history of racial segregation in South Africa dates back to colonial times when the Dutch established a settlement in the Cape of Good Hope in 1652. The Dutch East India Company, which controlled the colony, imported slaves from Asia and Africa to work on farms and mines. Over time, the population grew, and tensions arose between the white settlers and the black African population.

In 1910, the Union of South Africa was established, bringing together four British colonies and two former Dutch colonies. The country's new government introduced segregationist policies, such as the Land Act of 1913, which restricted black people's ownership of land, and the Native Urban Areas Act of 1923, which enforced residential segregation in urban areas.

The National Party came to power in 1948 and implemented the apartheid system, a comprehensive system of racial segregation that was institutionalized in law. The apartheid system enforced separate living areas, schools, hospitals, and public facilities for different races, with black people subjected to inferior facilities and opportunities. The political stance of the National Party shifted to more radical, extreme right since the 1960s, with stricter segregation policies being enforced over time. 

The apartheid system was met with widespread opposition, both within South Africa and internationally. The African National Congress (ANC), a political organization formed in 1912, led the struggle against apartheid and was instrumental in securing its eventual downfall. International pressure, including economic sanctions and boycotts, also contributed to the end of apartheid.

In 1994, South Africa held its first multiracial democratic elections, and Nelson Mandela became the country's first black president, marking the end of apartheid. However, the legacy of apartheid persists, and the country still struggles with issues of inequality, poverty, and social unrest. The study of racial segregation policies in South Africa is important to understand the country's history and its ongoing struggles with social and economic inequality.

![ezgif-4-8e8e9a4c36](https://user-images.githubusercontent.com/112432640/233857455-2333d0c0-ea34-4945-93d3-5889df6dd5bf.jpg)

# Introduction

The purpose of this project is to study the evolution of racial segregation policies in South Africa under the control of the Nationalist Party. Racial segregation has been a long-standing issue in South Africa, with the apartheid system implemented in 1948. This system aimed to enforce racial segregation and political and economic control of the white minority over the black majority, leading to decades of discrimination, inequality, and social unrest.

In this project, we aim to leverage Machine Learning technologies to analyze historical photos of South Africa and generate insights on the evolvement of the apartheid system. By using image classification algorithms to classify historical photos depicting apartheid policies, we aim to reveal the historical truth behind the struggle against apartheid, its impact on society, and the evolution of policies over time.

Through this project, we hope to shed light on the historical truth of South Africa's apartheid system and contribute to promoting truth and reconciliation among the country's diverse communities. By providing insights into the evolution of apartheid policies, we aim to help heal the wounds caused by decades of discrimination and segregation and contribute to a more just and equitable society.

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

# Setup

## Prerequisites

1. Python 3.x
2. R

## Clone the repository

First, you need to clone the repository to your local machine. You can do this by running the following command in your terminal:

```
git clone https://github.com/crown-of-napoleon/South-Africa-Apartheid-Truth-and-Reconciliation.git
```
## Install dependencies

The project has a number of Python dependencies which are listed in setup.py. You can install these dependencies using pip. Navigate to the project directory and run the following command:

```
pip install .
```
This command needs to be run in the directory that contains the setup.py file. It will install the project along with its dependencies.

# Disclaimer

The results and opinions generated and concluded by the code are solely for illustrative purposes and do not reflect the opinions and beliefs of the members of the contributors team or their affiliates. The contributors do not endorse any form of racial discrimination, segregation, or speeches that violate principles of equity and human rights. The contributors hold firm belief that it is crucial to build a tolerant, diverse environment for everyone, regardless of race, gender, sexuality, etc. 

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

## How to Contribute

We welcome contributions from everyone. Here are a few ways you can help:

1. **Fork the repository**: Start by forking the [repository](https://github.com/crown-of-napoleon/South-Africa-Apartheid-Truth-and-Reconciliation).

2. **Create a new branch**: Create a new branch in your forked repository. The branch name should be descriptive of the changes you are going to make.

3. **Make your changes**: Make the changes you want to contribute. These could be adding new files, modifying existing ones, fixing bugs, etc.

4. **Commit your changes**: Commit your changes to your branch. Make sure to write a clear and detailed commit message explaining what you've done.

5. **Push your changes**: Push your changes to your forked repository on GitHub.

6. **Create a Pull Request**: Go to the original [repository](https://github.com/crown-of-napoleon/South-Africa-Apartheid-Truth-and-Reconciliation) on GitHub, and click on the "New Pull Request" button. Select your fork and the branch you've worked on. Submit your Pull Request with a comprehensive description of the changes you've made.

Before you submit your Pull Request, please ensure to follow our code of conduct and contribution guidelines.

Thank you for your interest in contributing!


# Contact

In case of questions, comments, concerns, etc, please contact Haolin Guo (g.haolin@columbia.edu).
