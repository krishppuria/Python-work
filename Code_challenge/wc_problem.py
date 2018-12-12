#Code challenge to create a command to copy a file
import os
import shutil
def wc(file_open):
    sum_words=0
    sum_char=0
    lst=file_open.readlines()
    sum_lines=len(lst)
    file_open.seek(0,0)
    unique_list=file_open.read()
    #print(set(unique_list))
    for i in lst:
        sum_char+=len(i)
        sum_words+=len(i.split())
    sum_unique_list=len(set(unique_list.split()))
    print(sum_lines,sum_char,sum_words,sum_unique_list)
while(True):
    try:
        path="C:/Users/Krishna/Desktop/Python work/Files/"
        list_file = os.listdir(path)
        print("Enter Filename:")
        for file_name in list_file:
            print(file_name)
        user_path=input()
        file_open = open(path+user_path, 'r')
        wc(file_open)
    except Exception as e:
        print (e)
    else:
        break
