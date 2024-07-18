# while문을 사용하여 1부터 45사이의 랜덤한 수 6개를 생성하고, 이를 result리스트 변수에 추가하는 코드를 작성하라.
import random

#random.randint(1,45)
#1부터 45까지의 랜덤한 정수를 뽑는다.

i = 0
result = []
while i < 6 :
    i = i + 1
    result.append(random.randint(1, 45))
    # 1부터 45까지의 랜덤한 정수를 뽑는다.
print(result)



