#Code challenge to create a command to copy a file
import os
import shutil
while(True):
    try:
        path="C:/Users/Krishna/Desktop/Python work/Files/"
        list_file = os.listdir(path)
        print("Enter Filename:")
        for file_name in list_file:
            print(file_name)
        user_path=input()
        file_open = open(path+user_path, 'r')
        read_list=file_open.readlines()
        print(read_list[-1])
    except Exception as e:
        print ("e")
    else:
        break
