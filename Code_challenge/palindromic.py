def palin(num):
    lst=list(str(num))
    lst.reverse()
    #print (lst)
    num1=''.join(lst)
    num1=int(num1)
    return num1
while(True):
	try:
		check_lst=list(map(int,input().split()))
	except ValueError:
		print("Invalid Values Entered!, Please try again:")
	else:
		break
flag=True
flag1=False
for i in check_lst:
    rev=palin(i)
    if i<0:
        flag=False
        break
    elif i==rev:
        flag1=True
if flag and flag1:
    print ("True")
else:
    print ("False")
