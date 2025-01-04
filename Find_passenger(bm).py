# 50명의 승객과 탑승기회가 있을 때 총 탑승객의 수를 구하는 프로그램
# 조건 1 : 승객별 탑승시간은 5 ~ 50분 사이의 난수로 결정
# 조건 2 : 기사는 5 ~ 15분 사이의 승객만 매칭

# 출력문 예제 
# [o] 1번째 손님 (소요시간 : 00분)
# [o] 2번째 손님 (소요시간 : 00분)
# [ ] 3번째 손님 (소요시간 : 00분)
# [o] 4번째 손님 (소요시간 : 00분)
# ...
# [o] 50번째 손님 (소요시간 : 00분)

# 총 탑승 승객 : 00명

''' index를 50보다 작은수로 바꾸어도 50명이 출력되는 문제 발생 '''

from random import*

passenger = range(1,51)
# passenger = list(passenger)
# print(passenger)
index = 50
total = 0   # 총 탑승 승객
while index >= 1:
    for i in passenger:
        passenger = randint(5,50)   # 조건 1 : 각 승객에게 소요시간 부여(5~50분)
        if passenger >=5 and passenger <= 15:   #조건 2 : (5~15분)
            print("[o] {}번째 손님 (소요시간 : {}분)".format(i,passenger))
            total += 1
        else:
            print("[ ] {}번째 손님 (소요시간 : {}분)".format(i,passenger))
        
        index -= 1
        # print(passenger)
print("총 탑승 승객 : {}명".format(total))        