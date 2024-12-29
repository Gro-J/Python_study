''' 도메인 주소로 비밀번호 만들기 '''
# ex) http://naver.com 
# 규칙 1 : http:// 삭제
# 규칙 2 : 처음 나오는 . 이후 삭제
# 규칙 3 : 남은 글자중 첫 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + " ! " 로 비밀번호 완성

domain = "http://naver.com"
domain = domain[7:]     # naver.com
domain = domain[0:5]    # naver

three_let = domain[0:3]     # 앞 세 자리

length = len(domain)    # 글자 갯수

count_e = domain.count("e")     # 글자 내 'e' 갯수

password = three_let + str(length) + str(count_e) + "!"     # 비밀번호 최종

print("생성된 비밀번호 : %s" %password)     # 비밀번호 출력