while(True):
    try:
        user_input=list(map(int,input().split()))
    except ValueError:
        print("Invalid Input")
    else:
        break
user_input.sort()
sum_input=sum(user_input[1:-1])
print(sum_input)