def adult_func(n):
    if n>=19:
        return '성인입니다'
    else:
        return '미성년자입니다'

print(adult_func(18))


ages = [34, 25, 17, 13 , 54]
print('성인리스트')
print(filter(adult_func,ages))
for a in filter(adult_func,ages):
    print(a)