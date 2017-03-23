import os
import re
import png
import sys
import numpy as np
import random
import cv2
from scipy import misc
import glob
from PIL import Image

NEGATIVE_LOW = 4
NEGATIVE_HIGH = 10
cal = [0]
def storePatch(imgL,imgR, imgGround):
    i = random.choice([m for m in xrange(370)])
    j = random.choice([m for m in xrange(1226)])
    try:
        o_positive = random.randint(-1,1)
        sign = random.choice([-1,1])
        o_negative = sign * random.randint(NEGATIVE_LOW, NEGATIVE_HIGH)
        
        print cal

        imgLPatch = imgL.crop((j-5, i-5, j+6, i+6))
        disp = int(imgGround[i][j])
        print disp
        if np.sum(np.array(imgLPatch))==0 or disp== 0:
            storePatch(imgL, imgR, imgGround)
            return
        cal[0] += 1
        imgRPatchPos = imgR.crop((j+o_positive-disp-5,i-5,j+o_positive-disp+6,i+6))
        nameRightPos = "/Volumes/Myspace/Courses/Project/mynetwork/patches/{}RPositive.png".format(cal[0])
        imgRPatchPos.save(nameRightPos)
        nameLeft = "/Volumes/Myspace/Courses/Project/mynetwork/patches/{}L.png".format(cal[0])
        imgLPatch.save(nameLeft)
        
        imgRPatchNeg = imgR.crop((j+o_negative-disp-5, i-5, j+o_negative-disp+6, i+6))
        nameRightNeg = "/Volumes/Myspace/Courses/Project/mynetwork/patches/{}RNegative.png".format(cal[0])
        imgRPatchNeg.save(nameRightNeg)
    except:
        storePatch(imgL,imgR,imgGround)
        return

def readImage(pathL, pathR, pathGround):
    imgL = Image.open(pathL)
    imgR = Image.open(pathR)
    imgGround = Image.open(pathGround)
    imgGround = np.array(imgGround)
    imgGround = imgGround*1.0/256
    # print list(imgGround)
    return imgL, imgR, imgGround

def loadImage():
    currPath = "/Volumes/Myspace/Courses/Project/mynetwork/training/"
    os.chdir(currPath + "image_0/")
    namesL = glob.glob("*_10.png")
    os.chdir(currPath + "image_1/")
    namesR = glob.glob("*_10.png")
    os.chdir(currPath + "disp_noc/")
    namesGroundTruth = glob.glob("*_10.png")
    while (cal[0]!=100):
        randomNumber = random.randint(0,193)
        pathL = currPath + "image_0/" + namesL[randomNumber]
        pathR = currPath + "image_1/" + namesR[randomNumber]
        pathGound = currPath + "disp_noc/" + namesGroundTruth[randomNumber]
        imgL, imgR, imgGround = readImage(pathL, pathR, pathGound)
        storePatch(imgL, imgR, imgGround)

if __name__=='__main__':
    loadImage()











