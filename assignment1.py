# -*- coding: utf-8 -*-
"""assignment1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Es-PQWKyy4d6L9t4J2ShEvLxGWinfqu1
"""

from keras.datasets import fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

# What are the dimensions of train_images, train_labels, test_images, and test_labels?
print("train_images dimensions:", train_images.shape)
print("train_labels dimensions:", train_labels.shape)
print("test_images dimensions:", test_images.shape)
print("test_labels dimensions:", test_labels.shape)

#What are the lengths of train_labels and test_labels?
print("Length of train_labels:", len(train_labels))
print("Length of test_labels:", len(test_labels))

#Please show some of train and test labels.
print("Train labels:", train_labels[:10])
print("Test labels:", test_labels[:10])

#Please show the digital content of image index 5 in the training dataset

print(train_images[5])

#Plot the image of index 5 in the training dataset

import matplotlib.pyplot as plt

plt.imshow(train_images[5], cmap='gray')
plt.title("Image at index 5 in the training dataset")
plt.show()

#6 What is the label for the index 5 in the train_label and looking up in the above list, what does it mean?
label_index = train_labels[5]
#mapping of labels to fashion items
label_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
print("Label for index 5:", label_names[label_index])

#You'll need a corresponding list or dictionary that maps these indices to their fashion item names.

# 7 Please show the digital content of image index 500 in the testing dataset.
# Digital content
print(test_images[500])

#8 Please plot the image of the index 500 in the testing dataset.
plt.imshow(test_images[500], cmap='gray')
plt.title("Image at index 500 in the testing dataset")
plt.show()

#9 What is the label for the index 500 in the test_label and looking up in the above
#list, what does it mean?

label_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
label_index_500 = test_labels[500]
print("Label for index 500:", label_names[label_index_500], "and index", label_index_500)

#10 Please import models and layers from the keras library.
from tensorflow.keras import models, layers

#11 Define a sequential model and call it myNetwork.
myNetwork = models.Sequential()

#12 Reshape the images from 28x28 to one column with 784 neurons
#(flattening) (use 2 methods, one from the book and one from the 20-minute video).

myNetwork.add(layers.Flatten(input_shape=(28, 28)))

#13 Also, please normalize the image by dividing the image by 255
#(use 2 methods, one from the book and one from the 20-minute video).
train_images_normalized = train_images / 255.0
test_images_normalized = test_images / 255.0

#13
#method1
train_images_normalized1 = train_images / 255.0
test_images_normalized1 = test_images_normalized/ 255.0
#method2
train_images_normalized2 = train_images.astype('float32') / 255
test_images_normalized2 = test_images.astype('float32') / 255

#14 Add one hidden layer that has 512 neurons, using ‘relu’ activation function.
myNetwork.add(layers.Dense(512, activation='relu'))

#15 Add another hidden layer that has 128 neurons, using ‘relu’ activation function
myNetwork.add(layers.Dense(128, activation='relu'))

#16 Add the last layer as a 10-neuron dense layer that uses the ‘softmax’ as the
#activation function. Why we use softmax for the last layer? How does it work under the hood?
myNetwork.add(layers.Dense(10, activation='softmax'))

#Softmax is used for multi-class classification problems. It converts logits to probabilities by
#taking the exponential of each output and normalizing these values by dividing by the sum of all the exponentials.
#This ensures that the output values sum up to 1 and can be interpreted as class probabilities.

#17 Use the following two settings for the compiler and run them separately and see what the differences are.
#Optimizer ➔  adam,  loss➔ 'sparse_categorical_crossentropy', metrics➔[‘accuracy’]
#Optimizer ➔  rmsprop,  loss➔ 'categorical_crossentropy', metrics➔[‘accuracy’]
myNetwork.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

#myNetwork.compile(optimizer='rmspro', loss='categorical_crossentropy', metrics=['accuracy'])

#18Now after the compilation, please try to find the pattern using the fit command. The epochs need to be 10 for this example.
history_adam = myNetwork.fit(train_images_normalized, train_labels, epochs=10, validation_split=0.2)

#19 How do you compare the fashion_MNIST with what we learned in the class using the MNIST? What can we infer
#from the differences in the accuracy? What could be the reasons for that?

# The higher complexity of Fashion MNIST compared to MNIST explains the differences in accuracy; fashion items
# have more varied and intricate features than digits, making classification more challenging.

#20 Use the evaluate to calculate the achieved accuracy and loss over the test images and labels. Do we have overfitting?
test_loss_adam, test_acc_adam = myNetwork.evaluate(test_images_normalized, test_labels)
print(f"Test accuracy with Adam optimizer: {test_acc_adam}, Test loss: {test_loss_adam}")
#we do not have overfitting. The model's performance is consistently low across training, validation, and testing datasets, which suggests underfitting.



