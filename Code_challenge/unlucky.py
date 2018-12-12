while(True):
    try:
        user_input=list(map(int,input().split()))
    except ValueError:
        print("Invalid Input")
    else:
        break
num=0
user_sum=0
while(num<len(user_input)):
    if user_input[num]==13:
        num+=2
    else:
        user_sum=user_sum+user_input[num]
        num+=1
print(user_sum)