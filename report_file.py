# 회사에서 매주 1회 작성하는 보고서 양식을 만들기
# 보고서 양식

# - x 주차 주간보고 - 
# 부서 :
# 이름 :
# 업무 요약 :

# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성

# 조건 : 파일명은 '1주차.txt','2주차.txt'...와 같이 작성


for day in range(1,51):
    file_name = str(day)+"주차"
    print(file_name)
    
    with open(file_name+".txt","w",encoding="utf8")as x주차_file:
        x주차_file.write("-"+file_name+ " 주간보고 -\n부서 :\n이름 :\n업무 요약 :\n")

    with open(file_name+".txt","r",encoding="utf8")as x주차_file:
        print(x주차_file.read())
        
    