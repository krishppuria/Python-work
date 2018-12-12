#Code challenge to create a command to copy a file
import os
import shutil
while(True):
    try:
        path="C:/Users/Krishna/Desktop/Python work/Files/"
        list_file = os.listdir(path)
        for file_name in list_file:
            print(file_name)
        user_path=input()
        new_path= path+'copy'+user_path
        shutil.copy(path+user_path,new_path )
    except ValueError:
        print ("hello")
    else:
        break
