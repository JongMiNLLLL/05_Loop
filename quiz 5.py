# while문을 사용하여 1부터 100까지 수에 존재하는 모든 홀 수의 합을 구하시오.
# 1. 1부터 100까지의 수를 반복 출력
# index 변수가 하는 역할: 수열 만들기, 반복문 제어
# result 변수가 하는 역할: 연산결과 값을 저장
index = 1
result = []
while index < 100 :
    index = index + 1
# 2. 반복되는 수가 홀수인지를 확인
    if index % 2 == 1 :
# 3. 홀수라면 그 값을 저장
        result.append(index)
       #result = result + index
# 4. 저장된 값들의 합을 구함
print(sum(result))
#print(result)