#while 반복문
#- 조건문이 참인동안 하위 코드 블록을 반복 실행
#- 반복 범위가 설정되어 있지 않음 -> 무한 루프
# while 조건문 1 :
#   조건문은 참/거짓을 나타내는 논리 연산 결과값이 Boolean 데이터 값(true/false)인 조건 입력

contents = '사과'
while contents == '사과':
    print("사과가 맞습니다.")

##멈추는 방법 - 조건을 위반하게 만들어라

i = 10
count = 0
while i <100:
    i = i + 1
    count = count + 1
    print("i는 지금 값이", i,"이므로 100보다 작습니다.")
print(count)