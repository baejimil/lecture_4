try: 
    a,b = input('두 수를 넣으시오').split()
    result = (int(a)/int(b))
    print(result)

except Exception as e:
    print('에러형태는{}'.format(e))

print('test')