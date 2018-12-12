while(True):
    try:
        path="C:/Users/Krishna/Desktop/Python work/Files/"
        file_open = open(path+'etc_passwd.txt', 'r')
        read_list=file_open.readlines()
        user_dictionary={}
        for words in read_list:
            if words[0]!='#':
                words=words.split(':')
                user_dictionary[words[0]]=int(words[2])
    except Exception as e:
        print (e)
    else:
        break
for key,value in user_dictionary.items():
    print(key,value)