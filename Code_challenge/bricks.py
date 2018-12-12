while(True):
    try:
        lst=list(map(int,input("Enter elements of brick").split()))
    except ValueError:
        print("Invalid Input")
    else:
        break
flag=False
for i in range(1,lst[0]+1):
    for j in range(1,lst[1]+1):
        check=i*1+j*5
        if check==lst[2]:
            flag=True
            break
print(flag)
