''' 추첨 시스템 '''
# 이벤트 참여자 중 1명은 치킨, 3명은 커피 수령

# 조건 1) 이벤트 참여자는 20명
# 조건 2) 무작위 추첨하되 중복 수령 불가
# 조건 3) random 모듈의 shuffle과 sample을 활용

# 출력 예제
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
# -- 축하합니다 --

# from random import*

# <try 1>
# 20명의 참가자를 일일이 쓰기 싫어 randint로 추출하였더니 sample에서 오류
# participant = [randint(1,21)]
# shuffle(participant)
# print(sample(participant, 1))

#<try 2>
# participant = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# shuffle(participant)
# coffee = sample(participant,3)
# print(coffee)

# participant = participant.pop(coffee)
# chicken = sample(participant,1)
# print(chicken)

#<try3>
# coffee 와 chicken의 당첨자가 겹침
# 당첨자를 다음 추첨에서 제거할 방법을 찾아야함
# participant = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# shuffle(participant)
# coffee = sample(participant,3)
# print(coffee)

# chicken = sample(participant, 1)
# print(chicken)

#<try 4>
from random import*

participant = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]  # 20명의 참가자자
shuffle(participant)
coffee = sample(participant,3)             # coffee 당첨자 3명 
# print(coffee)

participant = set(participant)             # difference 사용을 위해서 list를 set으로 변경 
coffee = set(coffee)
participant = participant.difference(coffee)      # 차집합을 이용하여 커피 당첨자 제외외
# participant.remove(coffee)
participant = list(participant)            # sample 사용을 위해 set을 list로 변경 


chicken = sample(participant, 1)           # 치킨 당첨자 1명
# print(chicken)

print("-- 당첨자 발표 --\n치킨 당첨자 :",chicken,"\n커피 당첨자 :",coffee,"\n-- 축하합니다 -- ")
# print(participant)

