try: 
    a,b = input('두 수를 넣으시오').split()
    result = (int(a)/int(b))
    print(result)

except:
    print('대입한 수가 정확한지 확인하세요')

print('test')