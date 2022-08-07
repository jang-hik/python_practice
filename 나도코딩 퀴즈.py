'''Quiz1 (level2)'''
# names=["송바둑", "장바둑", "송멍뭉", "송뭉이"]
# for i in names:
#     a=i+".txt"
#     with open(f"{a}", "w", encoding="utf-8") as f:
#         f.write(f'''
# 안녕하세요? {i}님.

# (주)나도출반 편집자 나코입니다.
# 현재 저희 출판사는 파이썬에 관한 주제로 책 출간을 기획 중입니다.
# {i}님의 유튜브 영상을 보고 연락을 드리게 되었습니다.
# 자세한 내용은 첨부드리는 제안서를 확인 부탁드리며, 긍정적인 회신 기다리겠습니다.

# 좋은 하루 보내세요^^
# 감사합니다.

# -장형익 드림. ''')


'''Quiz1 (level2) 나도코딩 풀이'''
# names=["송바둑", "장바둑", "송멍뭉", "송뭉이"]
# for i in names:
#     a=i+".txt"
#     contents=(f"안녕하세요? {i}님.\n"
#                 "\n"
#                 "(주)나도출반 편집자 나코입니다.\n"
#                 "현재 저희 출판사는 파이썬에 관한 주제로 책 출간을 기획 중입니다.\n"
#                 f"{i}님의 유튜브 영상을 보고 연락을 드리게 되었습니다.\n"
#                 "자세한 내용은 첨부드리는 제안서를 확인 부탁드리며, 긍정적인 회신 기다리겠습니다."
#                 "\n"
#                 "좋은 하루 보내세요^^"
#                 "감사합니다."
#                 "\n"
#                 "-장형익 드림.")
#     with open(f"{a}", "w", encoding="utf-8") as f:
#         f.write(contents)


'''Quiz2 (level4)'''
from random import *
fruit=["apple", "banana", "orange"]
ranmdom_number=randint(0,2)                #random_number에 0,1,2,중 하나가 들어감

word=fruit[ranmdom_number]                    #word에 fruit안에 있는 단어 중 하나가 들어감
lists=list(word)                              #lists로 단어가 한 글자씩 쪼개져서 리스트 형태가 됨

print(word)
print("행맨을 시작합니다.")
print(len(word)*"_")

cha=input("소문자로 입력하세요:")
if cha in lists:
    print("Correct")
    for i in lists:
        if cha==i:
            print(i, end="")
else:
    print("Wrong")




# print(len(word)*"_")             #_____가 출력됨
# cha=input("소문자로 글자를 입력하시오:")    #b를 넣엏다고 가정, cha안에 b가 들어가있음

# for i in range(11):
#     n=0
#     minus=1
#     print(len(word)*"_")            
#     cha=input("소문자로 글자를 입력하시오:") 
#     if cha==word[n]:
#         print("cha"+(len(word)-minus)*"_")
#     else 





