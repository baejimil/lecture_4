def add(x,y):
    return x+y

add_other = lambda x,y : x+y

print(add_other(10,50))

def add_plus(x,y,z):
    # result_1 = x+y
    result_2 = lambda z : z**3

    return result_2

print(add_plus(10,30,20))