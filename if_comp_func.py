n_lists = range(1,101)

#짝수만 제곱하여 배열 만들기
square_arr = [x**2 for x in n_lists if x%2==0]

#2와 3의 공배수만 제곱하여 배열 만들기
square_arr_1 = [x**2 for x in n_lists if x%2==0 and x%3==0]
print(square_arr)
print(square_arr_1)