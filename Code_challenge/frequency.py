user_input=input()
dictionary={}
for char in user_input:
    if char in dictionary.keys():
        dictionary[char]+=1
    else:
        dictionary[char]=1
print(dictionary)