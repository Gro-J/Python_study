from random import*

total = 0
for i in range(1,51):
    time = randint(5,50)
    if 5 <= time <= 15:
        print("[o] {}번째 손님 (소요시간 : {}분)".format(i,time))
        total += 1
    else:
        print("[ ] {}번째 손님 (소요시간 : {}분)".format(i,time))
print("총 탑승 승객 : {}명".format(total))
