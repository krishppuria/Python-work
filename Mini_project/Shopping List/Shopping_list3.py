def show(function_list,):
    print("Total Elements in shopping list :",len(function_list))
    i=0
    for lst in function_list:
        print("\t", i, lst.strip())
        i+=1
    return
def user_help():
    print("To add ITEM simply enter the element name seprated by comma.")
    print('SHOW: It will display all the ITEMS contained by the list.')
    print('DONE: This will quit and take out from the program.')
    print('REMOVE: seprated space with index to remove the value at given Index.')
    print('ADD: followed by index and item name to add item at given position.')
    print("HELP: To show the help menu")
shopping_list=[]
file=open('shopping.txt','r+')
initial_list=file.readlines()
show(initial_list)
while(True):
    try:
        user_input = input("\nEnter Item: \n").split(",")
        #if user_input[0]=='':
         #   print("Invalid Input!!")
        if '' in user_input:
            raise Exception
        elif len(user_input) == 1:
            user_input[0] = user_input[0].upper()
            if user_input[0] == 'DONE':
                [file.write(items+"\n") for items in shopping_list]
                break
            elif user_input[0] == "SHOW":
                show(shopping_list)
            elif user_input[0] == 'HELP':
                user_help()
            else:
                shopping_list.append(user_input[0])
        elif len(user_input) == 2 and user_input[0].upper() == 'REMOVE' and user_input[1].isdigit():
            del (shopping_list[int(user_input[1])])
            print("Element removed.")
        elif len(user_input) == 3 and user_input[0].upper() == 'ADD' and user_input[1].isdigit():
            index = int(user_input[1])
            value = user_input[2]
            shopping_list.insert(index, value.upper())
            print("Element added.")
        else:
            chk_lst=user_input[1]
            if chk_lst[0]=='-' and chk_lst[1:].isdigit():
                print("invalid index")
            else:
                [shopping_list.append(value.upper()) for value in user_input]
    except Exception as e:
        print("Invalid Input ",e)
show(shopping_list)
file.close()