# vechileClassification
vechile Classification Freelancing Task using Tensorflow Keras 

#installation Steps to environment
!pip install tensorflow
!pip install opencv-python
!pip install keras.models
!pip install keras.layers
!pip install sklearn
!pip install matplotlib
!pip install warnings
!pip install os


# change variables to required paths 
data_dir = '/content/vechileClassification/dataset/'  
output_dir = '/content/outputImages'
inputVideoPath = '/content/demo.mkv'
testImagesPath =  output_dir+'/testImages/'

# first run videoToImage Script using change varibles with paths
!python3 videoToImage.py inputVideoPath testImagesPath

# run vechileClassification Script 
