ages = [34, 25, 17, 13 , 54]
print('성인리스트')

for a in filter(lambda x: x>=19 , ages): 
    print(a)