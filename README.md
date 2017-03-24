# Lecun_stereo_rebuild
This project is to try to recreate Jure Zbontar and Yann Lecun's paper of Stereo Matching by "Training a Convolutional Neural Network to Compare Image Patches".  
**Environement: Keras with the backend of Theano**
1. preprocess.py is to get the patches. This should be a brute-force way to crop the images. We only manage to get 100,000 pairs of positive-matching and negative-matching patches in total.
2. mc-cnn-rebuild.ipynb is the major neural network.
`This is a code by Qingwei Wu and Shixin Li`.
