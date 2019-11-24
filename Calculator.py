#-*- coding:UTF-8-*-



print("(a+b)(a-b)(a*b)(a/b) 방식으로 각 값을 따로 받아계산을하는 계산기입니다!")
a = int(input("첫번째숫자를 입력해주세요:"))
b = input("연산자를 입력해주세요:")
c = int(input("두번째 숫자를 입력해주세요:"))




what = ''

if b=='+':
    what = a+c
elif b == '-':
    what = a-c   
elif b == '*':
    what = a*c 
elif b == '/':
    what = a/c 
else:
    print("+,-,*,/ 중 하나만 입력해주세요!!")   
    
 
print(what)



