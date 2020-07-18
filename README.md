# Pneumonia Detection using CNN based classification 

Pneumonia Detection using CNN based classification model trained on chest x-ray scans of normal and people diagnosed with pneumonia. We trained a Convolutional Neural Network designed to process these x-ray images of the chest with pre-classified labels from the training set to replicate those results on the test set.



## Data Visualization & Preprocessing


We trained on a dataset of:

- over 5216 total x-ray images
- 1341 x-ray images of normal class
- 3875 x-ray images of pneumonia class
- highly imbalanced

We tested on a dataset of:

- over 624 total x-ray images
- 234 x-ray images of normal class
- 390 x-ray images of pneumonia class


For more info on the data: https://data.mendeley.com/datasets/rscbjbr9sj/2

License: https://creativecommons.org/licenses/by/4.0/


Images from both the classes

<img src="nb_images/normal.png" style="width:700px;height:400;">
<img src="nb_images/pnm.png" style="width:700px;height:400;">


Visualizing the data

<img src="nb_images/index.png" style="width:700px;height:400;">

As you can clearly see the data is imbalanced. Training a model on this imbalanced data would result in naive behaviour where the model would be always favoring the pneumonia class and still produce a decent accuracy but such results would be useless. To avoid this overfitting, we will increase the number of training examples using data augmentation.



## Model details


Model: "sequential_1"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d_5 (Conv2D)            (None, 150, 150, 32)      320       
_________________________________________________________________
max_pooling2d_5 (MaxPooling2 (None, 75, 75, 32)        0         
_________________________________________________________________
conv2d_6 (Conv2D)            (None, 75, 75, 64)        18496     
_________________________________________________________________
max_pooling2d_6 (MaxPooling2 (None, 38, 38, 64)        0         
_________________________________________________________________
conv2d_7 (Conv2D)            (None, 38, 38, 128)       73856     
_________________________________________________________________
max_pooling2d_7 (MaxPooling2 (None, 19, 19, 128)       0         
_________________________________________________________________
conv2d_8 (Conv2D)            (None, 19, 19, 128)       147584    
_________________________________________________________________
max_pooling2d_8 (MaxPooling2 (None, 10, 10, 128)       0         
_________________________________________________________________
flatten_1 (Flatten)          (None, 12800)             0         
_________________________________________________________________
dropout_4 (Dropout)          (None, 12800)             0         
_________________________________________________________________
dense_2 (Dense)              (None, 512)               6554112   
_________________________________________________________________
dense_3 (Dense)              (None, 1)                 513       
=================================================================
Total params: 6,794,881
Trainable params: 6,794,881
Non-trainable params: 0
_________________________________________________________________



#### Inputs and output

- The **input** is a batch of images and each image has a shape (150,150,1).
- The **output** represents a binary classification of the input images as 1 (Pneumonia) or 0 (Normal).


##Results

On the test set, we achieved:

- 0.92 accuracy
- 0.92 f1-score
- 0.93 recall
- 0.91 precision





