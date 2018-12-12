#Code Challenge to print only the elephant / tiger / lion / zebra / kangaroo
while (True):
    try:
        file = open('C:/Users/Krishna/Desktop/Python work/Files/zoo.csv', 'r')
        itter_list=file.readlines()
        for lines in itter_list:
            new_list=lines.split(",")
            print(new_list[0])
    except Exception as e:
        print("Exception Occur: ", e)
    else:
        break
    finally:
        file.close()
