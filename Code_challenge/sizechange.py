# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 15:43:51 2018

@author: Krishna
"""

from PIL import Image
import os
while(True): 
    try: 
        #Relative Path 
        #img_name=input("Enter image name: ")
        path="C:/Users/Krishna/Desktop/Python work/"
        list_file = os.listdir(path)
        for file in list_file:
            if '.bmp' in file:
                img = Image.open(file)
                weidth,height=img.size
                img=img.resize((100,100))
                img.save(file) 
        #img.show()
         #Saved in the same relative location 
        print("Successfully Formatted: formatted_picture.jpg")
    except Exception as e: 
        print(e)
    else:
        break