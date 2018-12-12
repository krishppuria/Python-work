lst2=[12,24,35,24,88,120,155,88,120,155]
final_list=[]
for elements in lst2:
    if elements not in final_list:
        final_list.append(elements)
print(final_list)