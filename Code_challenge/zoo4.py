#Code Challenge to print the total number of water needed by all the animals
while (True):
    try:
        file = open('C:/Users/Krishna/Desktop/Python work/Files/zoo.csv', 'r')
        itter_list=file.readlines()
        sum=0
        #animals_dict={'elephant':0,'zebra':0,'lion':0,'kangaroo':0,'tiger':0}
        for lines in itter_list:
            new_list=lines.split(",")
            if new_list[2]!='water_need\n':
                sum+=int(new_list[2])
        print("Total water needed:",sum)
    except Exception as e:
        print("Exception Occur: ", e)
    else:
        break
    finally:
        file.close()
