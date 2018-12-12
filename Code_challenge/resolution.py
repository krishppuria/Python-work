# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 16:13:21 2018

@author: Krishna
"""

from PIL import Image
while(True): 
    try: 
        #Relative Path 
        img_name=input("Enter image name: ")
        path="C:/Users/Krishna/Desktop/Python work/"
        img = Image.open(img_name)
        weidth,height=img.size
        print(weidth,height,sep='*')
        #img.show()
         #Saved in the same relative location 
        #print("Successfully Formatted: formatted_picture.jpg")
    except Exception as e: 
        print(e)
    else:
        break