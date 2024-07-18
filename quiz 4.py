# while무늘 사용하여 대기버호를 출력하느 프로그램을 작성하시오. 최대 대기번호 발행수는 1000이다.
number = 0
while number < 1000:
    number = number + 1
    if number == 500 :
        break    #break는 작업 중단 명령어
    print('대기번호는 ',number,'번 입니다.')

number = 0
while number < 1000:
    number = number + 1
    print('대기번호는 ', number, '번 입니다.')
else :
    print("대기번호가 1000번 초과입니다.")