user_input=input()
lst=['a','e','i','o','u','A','E','I','O','U']

converted_string=''
for char in user_input:
    if char in lst or char==' ':
        converted_string=converted_string+char
    else:
        converted_string=converted_string+char+'o'+char
print(converted_string)