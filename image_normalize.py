import numpy as np
import h5py
import os
import glob
from PIL import Image

def imageProcess():
    currPath="/home/qw2208/research/training/"
    os.chdir(currPath+"image_0/")
    nameL=glob.glob("*_10.png")
    os.chdir(currPath+"image_1/")
    nameR=glob.glob("*_10.png")
    os.chdir(currPath+"disp_noc/")
    namesG=glob.glob("*_10.png")
    
    with h5py.File("/home/qw2208/research/trainImgs.hdf5", "w") as f:
        print "Normalizing and saving left images..."
        grp = f.create_group("left")
        for img in nameL:
            s = int(img.split('_')[0])
            trainImg = np.array(Image.open(currPath + 'image_0/' + img))
            trainImg = (trainImg - np.mean(trainImg)) * 1.0 / np.std(trainImg)
            grp.create_dataset(name=str(s), data=trainImg)
        
        print "Normalizing and saving right imges..."
        grp = f.create_group("right")
        for img in nameR:
            s = int(img.split('_')[0])
            trainImg = np.array(Image.open(currPath + 'image_1/' + img))
            trainImg = (trainImg - np.mean(trainImg)) * 1.0 / np.std(trainImg)
            grp.create_dataset(name=str(s), data=trainImg)
        
        print "Saving groundtruth..."
        grp = f.create_group("groundtruth")
        for img in namesG:
            s = int(img.split('_')[0])
            grp.create_dataset(name=str(s), data=np.array(Image.open(currPath + 'disp_noc/' + img)))

if __name__ == '__main__':
    imageProcess()
