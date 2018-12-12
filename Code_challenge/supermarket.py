from collections import OrderedDict
check='hello'
oddict=OrderedDict()
while(True):
    try:
        while(check!='QUIT'):
            string=input()
            initial=0
            item_name,net_price=string.split()
            item_name=item_name.upper()
            print(item_name)
            check=item_name
            if check!='QUIT':
                if item_name in oddict.keys():
                    initial=oddict[item_name]
                    oddict[item_name]=initial+int(net_price)
                else:
                    oddict[item_name]=int(net_price)
                
    except ValueError:
        if item_name=='quit':
            break
        print ("exception")
    else:
        break
for key,value in oddict.items():
    print(key,value)
