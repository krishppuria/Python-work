#Code Challenge to read the zoo.csv file using readlines and print integrating the list
while (True):
    try:
        file = open('C:/Users/Krishna/Desktop/Python work/Files/zoo.csv', 'r')
        #print("Enter 5 students name: ")
        itter_list=file.readlines()
        for lines in itter_list:
            #user_name = input()
            #file.write(user_name + '\n')
            print(lines)
    except Exception as e:
        print("Exception Occur: ", e)
    else:
        break
    finally:
        file.close()
