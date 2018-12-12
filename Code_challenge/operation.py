def add(function_list):
    return sum(function_list)
def multiply(function_list):
    mul_list=1
    for count in function_list:
        mul_list=mul_list*count
    return mul_list
def largest(function_list):
    value=max(function_list)
    return value
def smallest(function_list):
    value=min(function_list)
    return value
def sorting(function_list):
    function_list.sort()
    return function_list
def remove_duplicates(function_list):
    return set(function_list)
def Print(function_list):
    print("Sum=",add(function_list))
    print("Multiply =",multiply(function_list))
    print("Largest =",largest(function_list))
    print("Smallest=",smallest(function_list))
    print("sorted =",sorting(function_list))
    print("Without Duplicates =",remove_duplicates(function_list))
while(True):
    try:
        input_list=list(map(int,input("Enter values of list.").split()))
    except ValueError:
        print("Invalid Input.")
    else:
        break
Print(input_list)
