from random import*

users = range(1,21)
# print(type(users))      # range class
users = list(users)

shuffle(users)
print(users)

winners = sample(users,4)   # 4명의 당첨자 

print(" -- 당첨자 발표 -- ")
print(" 치킨 당첨자 : {} ".format(winners[0]))  # 첫 번째 당첨자를 치킨
print(" 커피 당첨자 : {}".format(winners[1:]))  # 남은 세명 커피 
print(" -- 축하합니다 -- ")
