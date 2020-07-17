list_a = [10,20,30]
list_b = [10,20,30]

num_a =3
num_b = 3

if num_a is num_b:
    print('num_a is num_b')

else:
    print('num_a is not num_b')

if list_a == list_b:
    print('list_a is list_b')

else:
    print('list_a is not list_b')

print(id(list_a))
print(id(list_b))