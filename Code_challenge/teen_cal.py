def fix_teen(n):
    if n>14 and n<17:
        return n
    elif n>12 and n<20:
        return 0
    else:
        return n
    return teen_sum
dictionary={}
for i in range(3):
    while(True):
        try:
            key,value=input().split()
            value=int(value)
            dictionary[key]=value
        except ValueError:
            print ("Invalid Input")
        else:
            break
teen_sum=0
for value in dictionary.values():
    return_value=fix_teen(value)
    teen_sum=teen_sum+return_value
print(teen_sum)