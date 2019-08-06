from keras.models import Sequential  # help to create model layer by layer
from keras.layers import Dense, Conv2D, Flatten	# to apply different layers
import matplotlib.pyplot as plt	# to plot image of dataset (to visualize) 
from keras.datasets import mnist	# dataset used is of MNIST digits classification(0-9)
from keras.utils import to_categorical # to categorize the labels

(X_train, y_train), (X_test, y_test) = mnist.load_data()# to load the dataset and split them to training and test data
X_train = X_train.reshape(60000,28,28,1)# MNIST dataset contains 60000 training images of 28 x 28 dimensions and 1 depicts they are of gray scale
X_test = X_test.reshape(10000,28,28,1)# MNIST dataset contains 10000 test images of 28 x 28 dimensions and 1 depicts they are of gray scale
y_train = to_categorical(y_train)# build vector based on label i.e for 2=[0,0,1,0,0,0,0,0,0,0]
y_test = to_categorical(y_test)# build vector based on label i.e for 2=[0,0,1,0,0,0,0,0,0,0]
model = Sequential()#it helps to build a model layer by layer
model.add(Conv2D(64, kernel_size=3, activation='relu', input_shape=(28,28,1)))# to add convolution layer to the model
model.add(Conv2D(32, kernel_size=3, activation='relu'))# to add convolution layer to model
model.add(Flatten())# it serve as a connection between the dense and convolution layer
model.add(Dense(10, activation='softmax'))# it works as neural network
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])# it adds optimizers and loss functions
model.fit(X_train, y_train,validation_data=(X_test, y_test), epochs=3)#to train the model
model.predict(X_test[:4])# prediction