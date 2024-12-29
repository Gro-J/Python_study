domain = "http://naver.com"
my_str = domain.replace("http://","")   # http:// 제거 / 규칙1
my_str = my_str[:my_str.index(".")]     # . 이후 제거  / 규칙2
#print(my_str)                           # naver 출력

password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
#print(password) 

print(f"{domain}의 비밀번호는 {password}입니다.")