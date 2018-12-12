#Code Challenge to take input of 25 students name and create a text file
while(True):
    try:
        file=open('C:/Users/Krishna/Desktop/Python work/Files/students.txt','w')
        print("Enter 5 students name: ")
        name_list=[]
        for i in range(0,5):
            user_name=input()
            file.write(user_name+'\n')
    except Exception as e:
        print("Exception Occur: ",e)
    else:
        break
    finally:
        file.close()
