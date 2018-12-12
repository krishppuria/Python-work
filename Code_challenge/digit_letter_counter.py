user_input=input()
dictionary={'Letters':0,'Digits':0}
for char in user_input:
    if char.isdigit():
        dictionary['Digits']+=1
    elif char.isalpha():
        dictionary['Letters']+=1
for key,value in dictionary.items():
    print(key,value)