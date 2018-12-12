shopping_list=[]
while(True):
    user_input=input()
    if(user_input=='DONE'):
        break
    else:
        shopping_list.append(user_input)
print("Elements in shopping list:")
[print(lst) for lst in shopping_list]