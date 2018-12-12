def show(function_list):
    print("Elements in shopping list:")
    [print(lst) for lst in function_list]
    return
def user_help():
    print('SHOW: It will display all the ITEMS contained by the list.')
    print('DONE: This will quit and take out from the program.')
shopping_list=[]
while(True):
    user_input=input()
    if(user_input=='DONE'):
        break
    elif user_input=="SHOW":
        show(shopping_list)
    elif user_input=='HELP':
        user_help()
    else:
        shopping_list.append(user_input)
show(shopping_list)