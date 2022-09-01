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

# <span style="font-size:13px">- totalList : 비어있는 리스트를 생성해 줘야 됨(imageList와 labelList를 담아주고 return 시키기 위해서) </span> <br>  
# <span style="font-size:13px">- trainingFullPath : 상세분류 폴더 상위 경로 </span>  
# <span style="font-size:13px">- IMG_SIZE : 수정할 이미지 size </span>

# In[20]:


def inImgList(trainingFullPath, targetFolder, IMG_SIZE, totalList):
    imageList = []
    labelList = []
    for i in range (0, len(targetFolder)):
            print(targetFolder[i] + " start")

            eachPath = os.path.join(trainingFullPath, targetFolder[i])
            eachImages = os.listdir(eachPath)
            for j in range( 0 , len(eachImages)):
                try:
                    eachImagesPath = os.path.join(eachPath,eachImages[j])
                    eachImg = imread(eachImagesPath)
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


# #### 딕셔너리 value값으로 key값 불러오는 함수

# <span style="font-size:13px">- dictionary : 딕셔너리 값 </span>  
# <span style="font-size:13px">- val : 예측된 값 </span>  

# In[11]:


def getKey(dictionary, val):
    for key, value in dictionary.items():
         if val == value:
            return key


# ### 한글명 이미지 읽어오기

# <span style="font-size:13px">- filename : 파일명 </span>
# <span style="font-size:13px">- flags : 기본값 컬러 </span>   
# <span style="font-size:13px">- dtype : 기본값 데이터 타입 uint8 </span>  

# In[14]:


def imread(filename, flags=cv2.IMREAD_COLOR, dtype=np.uint8):
    try:
        n = np.fromfile(filename, dtype)
        img = cv2.imdecode(n, flags)
        return img
    except Exception as e:
        print(e)
        return None


# ### 한글명 이미지 저장하기

# <span style="font-size:13px">- filename : 파일명 </span>  
# <span style="font-size:13px">- img : 이미지 </span>  
# <span style="font-size:13px">- params : 기본값 None </span>  

# In[24]:


def imwrite(filename, img, params=None):
    try:
        ext = os.path.splitext(filename)[1]
        result, n = cv2.imencode(ext, img, params)

        if result:
            with open(filename, mode='w+b') as f:
                n.tofile(f)
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False


# In[ ]:




