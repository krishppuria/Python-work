#Code Challenge to print the total number of water need by elephant / tiger / lion / zebra / kangaroo
while (True):
    try:
        file = open('C:/Users/Krishna/Desktop/Python work/Files/zoo.csv', 'r')
        itter_list=file.readlines()
        animals_dict={'elephant':0,'zebra':0,'lion':0,'kangaroo':0,'tiger':0}
        for lines in itter_list:
            new_list=lines.split(",")
            if new_list[0] in animals_dict.keys():
                animals_dict[new_list[0]]+=int(new_list[2])
        for key,value in animals_dict.items():
            print(key,value,sep=":")
    except Exception as e:
        print("Exception Occur: ", e)
    else:
        break
    finally:
        file.close()
