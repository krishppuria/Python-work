lst=[chr(ord('a')+i) for i in range(0,26)]
lst1=input()
lst1=lst1.lower()
flag=True
for i in lst:
    if i not in lst1:
        flag=False
if flag:
    print ("PANGRAM")
else:
    print("NOT PANGRAM")