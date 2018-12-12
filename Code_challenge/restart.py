string_i='RESTART'
index=string_i.index('R')+1
string_f=string_i[0:index]+string_i[index:].replace('R','$')
print(string_f)