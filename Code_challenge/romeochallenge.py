#Code Challenge to print the total number of water need by elephant / tiger / lion / zebra / kangaroo
while (True):
    try:
        file = open('C:/Users/Krishna/Desktop/Python work/Files/romeo.txt', 'r')
        itter_list=file.readlines()
        animals_dict={}
        for lines in itter_list:
            #lines=lines.strip()
            new_list=lines.split()
            for words in new_list:
                if words in animals_dict.keys():
                    animals_dict[words]+=1
                else:
                    animals_dict[words]=1
        for key,value in animals_dict.items():
            print(key,value,sep=":")
    except Exception as e:
        print("Exception Occur: ", e)
    else:
        break
    finally:
        file.close()
