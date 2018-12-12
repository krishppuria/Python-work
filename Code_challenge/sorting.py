input_tuple=[]
while(True):
    try:
        for _ in range(5):
            name,age,score=input().split()
            age=int(age)
            score=int(score)
            lst=[name,age,score]
            input_tuple.append(tuple(lst))
    except ValueError:
        print("Invalid Input")
    else:
        break
input_tuple.sort()
print(input_tuple)