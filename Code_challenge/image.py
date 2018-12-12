# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from PIL import Image
import os
while(True): 
    try: 
        #Relative Path 
        img_name=input("Enter image name: ")
        extension_list=['.jpg','.jpeg','.png','.bmp']
        path="C:/Users/Krishna/Desktop/Python work/"
        list_file = os.listdir(path)
        for ext in extension_list:
            if (img_name+ext in list_file):
                img_name+=ext
                break
        img = Image.open(img_name)  
        img=img.convert("L")
        #Angle given 
        img = img.transpose(Image.ROTATE_90)  
        #img.show()
        weidth,height=img.size
        center_w,center_h=(weidth)/2,(height/2)
        print(weidth,height)
        area=(center_w-160,center_h-204,center_w+160,center_h+204)
        img=img.crop(area)
        img.thumbnail([75,75])
        img.show()
         #Saved in the same relative location 
        img.save("formatted_picture.jpg") 
        print("Successfully Formatted: formatted_picture.jpg")
    except Exception as e: 
        print(e)
    else:
        break

