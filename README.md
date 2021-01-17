# InstaVis Checker

**InstaVis Checker** is a small application which can 

:small_blue_diamond: evaluate the quality of visual concept of your Instagram profile    
:small_blue_diamond: provide some cute recommendations    
:small_blue_diamond: provide examples of the good similar profiles for your inspiration.    

### Creators
:small_orange_diamond: Anastasiya Belykh    
:small_orange_diamond: Anastasiya Filatova    

## About InstaVis Checker

InstaVis Checker app was created as a final project in the course: "Architecture of neural networks for deep learning" in ITMO University.

#### What main frameworks and libraries are used

☑️ Keras library for all interaction with the neural network model    
☑️ Streamlit library if you want to work with the application    
☑️ Basic libraries for data analysis and processing like Numpy and Pandas    
☑️ PIL library for images processing

#### What is the underlying neural network architecture?

Project is based on the Residual Attention Network architecture which was implemented by us based on the original article:
> [**F. Wang et al.** "Residual Attention Network for Image Classification"](https://arxiv.org/pdf/1704.06904.pdf)

#### Why Residual Attention Network?

:heavy_check_mark: We needed NN architecture that can extract features from images almost like human (that's why attention modules)    
:heavy_check_mark: We wanted to implement real deep neural network architecture (that's why residual units)    
:heavy_check_mark: Selected architecture supports scaling and expansion by several hundred layers, and also adapts to any state-of-the-art structure for feature selection (in trunk branch of the Attention module), which will be useful if we decide to expand the project    

As in an original article, in our implementation, we use `pre-activation Residual Unit` as the network basic unit to construct Attention Module. It was first described at original article:

> [K. He et al. "Identity mappings in deep residual networks"](https://arxiv.org/abs/1603.05027)

And also we found useful GitHub repo of the articles' authors:
> [Original article's implementation Github repo](https://github.com/KaimingHe/resnet-1k-layers)

Despite the fact that their implementation was not in Keras, it helped us to create ours.

## Project structure

1️⃣ `images_data_processing` directory contains files for images data uploading and processing (this data is used for model training and validation)    
2️⃣ `model` directory contains jupyter notebook with Attention Residual Network-56 implementation and training    
3️⃣ `app` directory contains python file with the application code and auxiliary python file with the function for images concatenation    

**NB!** If you see the following structure in the code: `<data_path>`, it means that you should place the path to your real directory here 
