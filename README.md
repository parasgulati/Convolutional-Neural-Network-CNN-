# Digits Recognition using CNN

CNN is a Neural network that is used for image classification.<br/>
Here I have used MNIST Hand written digits dataset.<br/><br/>

![dataset](https://github.com/parasgulati/Convolutional-Neural-Network-CNN-/blob/master/we.jpg)

<br/>It contains 60,000 training images and 10,000 testing images each of 28 x 28 dimensions represented by pixel matirx.
<br/>The model of cnn is shown<br/> 
there are various layers.It recognises digits image with an accuracy of 97.58 %
<br/>
![mode](https://github.com/parasgulati/Convolutional-Neural-Network-CNN-/blob/master/c.jpeg)

input image is of (m X n).
<h4>filter</h4> this multiply corresponding element of filter matrix and image matrix pixel values and sum them all and keep it in new image matrix.It is also known as kernel or weight matrix.
<h4>convolutional layer</h4>Applyfilter of (x X y).
<h5>padding</h5>you can apply padding its not compulsory.Padding is used to add zero pixel values at the corner to retain the previous image size else number of pixels will be decreased.
<h5>Stride</h5>you can also apply stride.It is also not compulsory.It is the number of pixels to leave while applying filter.
<h2>After applying filter of order (x X y) and applying no padding the image size dimensions shrinks to (m-x-1 ,n-y-1) </h2>
Convolutional layer basically zooms that part of image that has features.
<h2>ReLU activation function</h2>
ReLU stands for Rectified Linear unit.This changes all negative values to zero.This makes the image linear.
<h5>The problem with negative pixel values is that if negative values depitcs light color of that pixel.and if we pass it to neural network then it wolud learn that this light color should be present if it does not find it then it would stuck.So to make learning easier we make it zero.</h5>
<h3>pooling</h3>This is used to extract the broader view of the image pixel matrix.It takes filter, all the values coming under that filter, out of that maximum pixel intensity value is selected this is called max pooling.Let's suppose filter size is (l,k), then the image size will be reduced to (m-x-1-l-1,n-y-1-k-1).
<br>
Now the extracted pixel value matrix is converted into a list of pixel intensity values.
This list has (m-x-l-2 * n-y-2-k) pixel values and it is feed into a fully connected neural network having  (m-x-l-2 * n-y-2-k) neurons in input layer.

![denselayer](https://github.com/parasgulati/Convolutional-Neural-Network-CNN-/blob/master/dense%20layer.png)
We can take any number of neurons in hidden layer,it is a hyper parameter
Weights tells how much feature of corresponding neuron will be inherited to the corresponding neuron in the next layer. 

![img1](https://github.com/parasgulati/Convolutional-Neural-Network-CNN-/blob/master/img1.jpg)

<h3>softmax activation function</h3>
This will give probabilty of an image to be a image of different number. whose probability is higher that's our anser.

![softmax](https://github.com/parasgulati/Convolutional-Neural-Network-CNN-/blob/master/softmax.png)

<h3>But one important thing how to update weight matrix of neural network, this helps to minimize the error i.e by gradient descent</h3>

![gradientdescent](https://github.com/parasgulati/Convolutional-Neural-Network-CNN-/blob/master/gradient%20descent.jpg)

![gradientfunction](https://github.com/parasgulati/Convolutional-Neural-Network-CNN-/blob/master/gradient%20function.png)

![cost](https://github.com/parasgulati/Convolutional-Neural-Network-CNN-/blob/master/cost.jpg)

The theta is updates till we get minimum cost function i.e till it converges to global minima.
<h3>Applying Regularization</h3>
To overcome the problem of over fitting we randomly put the weights of any neuron to zero. 
