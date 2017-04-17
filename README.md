# Lecun_stereo_rebuild
**This project is to try to recreate Jure Zbontar and Yann Lecun's paper of Stereo Matching by "Training a Convolutional Neural Network to Compare Image Patches".**  

Environement: Keras with the backend of Theano  

1. preprocess.py is to get the patches. This should be a brute-force way to crop the images. We create 11\*11 pixel windows and train the neural networks on these training samples.
2. mc-cnn-rebuild.ipynb is the first version of our neural network. We merge two CNN subnets and apply fully-connected layers on training patches of 11\*11. testCNN.ipynb is where the disparity map is derived and the whole image is tested based on the network which has been trained. The fully-connected layer is converted into CNN layers equally to enable the different input dimensions.
3. mc-cnn-rebuildONE.ipynb is a second version of our neural network. Fully-connected layers are replaced with CNN layers (same as the test network).
`This is a code by Qingwei Wu and Shixin Li`.
