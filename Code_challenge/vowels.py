lst=['Alabama','California','Oklahoma','Florida']
for a in('a','e','i','o','u','A','E','I','O','U'):
    lst=[s.replace(a,'') for s in lst]
print(lst)
