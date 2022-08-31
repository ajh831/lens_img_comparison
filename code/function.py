#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np

import os # 경로 합치기 위한 라이브러리
import glob as glob # jpg파일 찾기 위한 라이브러리
import cv2 # 이미지를 위한 라이브러리


# #### 폴더 생성 함수

# <span style="font-size:13px">- directory : 폴서 생성할 경로 </span>

# In[2]:


def createFolder(directory): 
    try: 
        if not os.path.exists(directory): 
            os.makedirs(directory) 
    except OSError: 
        print ('Error: Creating directory. ' + directory)


# #### 이미지 리스트에 담는 함수

# <span style="font-size:13px">- trainingFullPath : 상세분류 폴더 상위 경로 </span>  
# <span style="font-size:13px">- IMG_SIZE : 수정할 이미지 size </span>

# In[1]:


def inImgList(trainingFullPath, IMG_SIZE):
    imageList = []
    labelList = []
    for i in range (0, len(targetFolder)):
            print(targetFolder[i] + " start")

            eachPath = os.path.join(trainingFullPath, targetFolder[i])
            eachImages = os.listdir(eachPath)
            for j in range( 0 , len(eachImages)):
                try:
                    eachImagesPath = os.path.join(eachPath,eachImages[j])
                    eachImg = cv2.imread(eachImagesPath)
                    eachImg = cv2.cvtColor(eachImg, cv2.COLOR_RGB2GRAY)
                    outImg = cv2.resize(eachImg, (IMG_SIZE,IMG_SIZE))
                    imageList.append(outImg)
                    labelList.append(targetFolder[i])
                except Exception as e:
                    print(e)
                    pass

    totalList.append(imageList)
    totalList.append(labelList)
    
    return totalList


# #### 이미지 정제 함수

# <span style="font-size:13px">- inImg : 이미지 경로 </span>  
# <span style="font-size:13px">- IMG_SIZE : 수정할 이미지 size </span>  
# <span style="font-size:13px">- channel : 이미지 채널 </span>  

# In[6]:


def imgClean(inImg, IMG_SIZE, channel) :
    outImg = cv2.cvtColor(inImg, cv2.COLOR_BGR2GRAY)
    outImg = cv2.resize(outImg, (IMG_SIZE, IMG_SIZE))
    outImg = outImg/255
    outImg = outImg.reshape(channel, IMG_SIZE, IMG_SIZE)
    return outImg


# #### 딕셔너라 value값으로 key값 불러오는 함수

# <span style="font-size:13px">- dictionary : 딕셔너리 값 </span>  
# <span style="font-size:13px">- val : 예측된 값 </span>  

# In[9]:


def getEmotion(dictionary, val):
    for key, value in dictionary.items():
         if val == value:
             return key


# In[ ]:




