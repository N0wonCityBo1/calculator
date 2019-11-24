while True :
    print("(a+b)(a-b)(a*b)(a/b) 방식으로 각 값을 따로 받아계산을하는 계산기입니다! 종료를 원한다면 연산자 입력에 '@'를 입력해주세요!")
    a = int(input("첫번째숫자를 입력해주세요:"))
    b = input("연산자를 입력해주세요:")
    c = int(input("두번째 숫자를 입력해주세요:"))

    what = ''

   
    if b=='+':
        what = a+c
        print(what)
    elif b == '-':
        what = a-c  
        print(what) 
    elif b == '*':
        what = a*c 
        print(what)
    elif b == '/':
        what = a/c 
        print(what)
    elif b == '@':
        print("종료합니다.")
        break    
    else:
         print("+,-,*,/ 중 하나만 입력해주세요!!") 

