# 표준 체중을 구하는 프로그램

# (성별에 따른 공식)
# 남자 : 키(m) x 키 x 22
# 여자 : 키(m) x 키 x 21

# 조건 1) 표준 체중은 별도의 함수 내에서 계산
#     * 함수명 : std_weight
#     * 전달값 : 키(height), 성별(gender)

# 조건 2) 표준 체중은 소수 둘째자리까지 표시

# (출력예제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.

def std_weight(height, gender):
    if gender == "남자":
        std_weight = height*height*22
        return std_weight
        print("키 {}cm {}의 표준체중은 {:.2f}kg 입니다.".format(int(height*100),gender,std_weight))
        
    
    elif gender == "여자":
        std_weight = height*height*21
        return std_weight

        print("키 {}cm {}의 표준체중은 {:.2f}kg 입니다.".format(int(height*100),gender,std_weight))
        
    else:
        print("성별을 제대로 입력해주세요.")

gender = input("성별을 입력하세요.")
height = float(input("키를 입력하세요."))
std_weight(height,gender)
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

# def std_weight(height, gender):
#     if gender == "남자":
#         return height*height*22
#     else:
#         return height*height*21


# gender = input("성별을 입력하세요.")
# height = float(input("키를 입력하세요."))
# weight = std_weight(height,gender)
# print("키 {}cm {}의 표준체중은 {:.2f}kg 입니다.".format(int(height*100),gender,weight))




# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# gender = input("성별을 입력해주세요.")
# height =  float(input("키를 입력해주세요."))
# if gender == "남자":
#         std_weight = height*height*22
        
# elif gender == "여자":
#         std_weight = height*height*21
        
# else:
#         print("성별을 제대로 입력해주세요.")

# print("키 {}cm {}의 표준체중은 {:.2f}kg 입니다.".format(int(height*100),gender,std_weight)) 
# # 중괄호에 :.2f 를 통해 소수점 두자리까지만 출력

