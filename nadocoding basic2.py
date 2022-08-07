'''while'''

# cons = "토르"
# index = 5
# while index >= 1:
#     print(f"{cons} 씨 커피가 준비되었습니다. {index}번 남았어요")
#     index -= 1
#     if index == 0:
#         print("커피가 폐기되었습니다.")

# cons = "토르"
# person = "unknown"
# while person != cons:
#     print(f"{cons}씨 커피가 받아가세요")
#     person=input("이름이 어떻게 되세요? ")
#     if person == cons:
#         print("주문하신 커피나왔습니다.")
#     else:
#         print("죄송합니다. 손님 커피가 아닙니다.")


'''continue와 break'''

# #continue 밑에 내용을 실행하지 말고 반복으로 돌아가라는 뜻, break는 뒤에 반복값이 더 있어도 바로 반복문 탈출
# absent = [2,5]
# no_book = [7]
# for student in range(1,11):
#     if student in absent:
#         continue
#     print("{0}번, 책 읽어봐".format(student))
#     if student in no_book:
#         print("{0}번, 왜 책을 안읽나? 혹시 책을 안가져왔니? 안되겠다 오늘 수업은 여기까지다. {0}번은 교무실로 따라와라".format(student))
#         break


'''List comprehension'''

#[표현식 for 항목 in 반복가능객체 if 조건문]

#[표현식 for 항목1 in 반복가능객체1 if 조건문1
#        for 항목2 in 반복가능객체2 if 조건문2
#        ...
#        for 항목n in 반복가능객체n if 조건문n]

# students = [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students]
# print(students)

# students = ["장형익", "이혁", "베르다리오"]
# students = [len(i) for i in students]
# print(students)

# students = ["iron man", "thor", "widow"]
# students = [i.upper() for i in students]
# print(students)

# a = [1,2,3,4]
# result = [num*3 for num in a]
# print(result)

# a = [1,2,3,4]
# result = [num*3 for num in a if num%2==0]
# print(result)

# result = [x*y for x in range(2,10)
#               for y in range(1,10)]
# print(result)


'''함수'''
'''입력값과 반환값'''
# def open_account():
#     print("새로운 계좌가 생성되었습니다.")

# open_account()


# def deposit(balance, money):
#     print("입금이 완료되었습니다. 잔액은 {0}입니다.".format(balance+money))
#     return balance + money

# def withdraw(balance, money):
#     if balance >= money: #잔액이 출금액보다 많으면
#         print("{0}가 출금되었습니다.".format(balance-money))
#         return balance - money
#     else:
#         print("잔액이 부족합니다. 잔액은 {0}입니다.".format(balance))
#         return balance

# def withdraw_night(balance, money):
#     commission = 100
#     return commission, balance - money - commission

# balance = 0
# balance=deposit(balance, 1000)
# balance = withdraw(balance, 500)
# commission, balance = withdraw_night(balance, 500)
# print("수수료 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))


'''기본값'''

# def profile(name, age, main_lang):          
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}" \
#         .format(name, age, main_lang))    
#                         #\t는 탭을 띄워주는 escape code, print()안에서 \치고 엔터를 치면 줄바꿈해준다. 

# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")


# def profile(name, age=17, main_lang="파이썬"):  #age와 main_lang에 입력값이 없으면 기본값인 17과 파이썬이 나온다.          
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}" \
#         .format(name, age, main_lang))    

# profile("유재석")
# profile("김태호")


'''키워드값'''

# def profile(name, age, main_lang):
#     print(name, age, main_lang)

# profile(age="24", name="바둑이", main_lang="파이썬")
# profile(main_lang = "파이썬", name = "멍멍이", age=25)


'''가변인자'''

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t". format(name, age), end = " ")
#     print(lang1, lang2, lang3, lang4, lang5)

# profile("유재석", 20, "python", "java", "C", "C++", "C#")
# profile("김태호", 25, "kotlin", "swift", "", "", "")



# def profile(name, age, *language):
#     print("이름 : {0}\t나이 : {1}\t". format(name, age), end = " ")
#     for lang in language:
#         print(lang, end=" ")
#     print()

# profile("유재석", 20, "python", "java", "C", "C++", "C#", "javascript")
# profile("김태호", 25, "kotlin", "swift")


'''지역변수와 전역변수'''

# gun = 10

# def checkpoint(soldiers): 
#     gun = 20                        #local variable
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

# print("전체 총 : {0}".format(gun))
# checkpoint(2)
# print("남은 총 : {0}".format(gun))


# gun = 10

# def checkpoint(soldiers): 
#     global gun                        #전역 공간에 있는 gun사용
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

# print("전체 총 : {0}".format(gun))
# checkpoint(2)
# print("남은 총 : {0}".format(gun))


# gun = 10

# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun


# print("전체 총 : {0}".format(gun))
# gun = checkpoint_ret(gun,2)
# print("남은 총 : {0}".format(gun))


'''표준 입출력'''

# print("python"+"java")   #pythonjava 이 형태로 붙어서 나옴
# print("python", "java")  #python java 이 형태로 떨어져서 나옴
# print("python ", " java ", " javascript", sep="vs")

# print("python ", " java", sep="vs", end="? ")
# print("무엇이 더 재밌을까요?")

# import sys
# print("python", "java", file=sys.stdout)  #표준출력 : 잘 출력되는 부분이라 크게 신경 쓸 필요 없음
# print("python", "java", file=sys.stderr)  #표준에러 : 확인하고 수정같은 거를 해서 출력해야 함

# #왼쪽정령, 오른쪽정렬
# scores = {"수학":100, "통계":100, "영어":90, "코딩":100 }
# for subject, score in scores.items():   #딕셔너리의 키와 밸류를 쌍으로 튜플로 보내준다.
#     print(subject.ljust(4), str(score).rjust(4), sep=":")       

# #.ljust(4)는 4개의 공간을 만들어주고 subject를 왼쪽으로 정렬, .rjust(4)는 4개의 공간을 만들어주고 score을 오른쪽으로 정렬

# for num in range(1,21):
#     print("대기번호 :  " + str(num).zfill(3))   #.zfill(3)은 3개의 공간을 만들어서 남는 공간에 0을 채워넣는 함수

# answer = input("아무 값이나 입력하세요 : ")        #input함수는 입력받는 모든 값을 str로 인식한다.
# print("입력하신 값은 " + answer + "입니다.")


'''다양한 출력포맷'''

# print("{0: >10}".format(500))   #빈자리는 빈 공간으로 두고, 오른쪽 정렬을 하되, 총 10차리 공간을 확보
# print("{0:*>10}".format(500))   #빈자리는 *을 채우고, 오른쪽 정렬을 하되, 총 10차리 공간을 확보

# print("{0: >+10}".format(500))  #빈자리는 빈 공간으로 두고, 오른쪽 정렬, 총 10차리 공간을 확보하고, 양수일 때는 +, 음수일 때는 -로 표시
# print("{0: >+10}".format(-500))

# print("{0:_<+10}".format(-500)) #빈자리는 _로 두고, 왼쪽 정렬, 총 10차리 공간을 확보하고, 양수일 때는 +, 음수일 때는 -로 표시

# print("{0:,}".format(1000000000)) #3자리 마다 콤마를 찍어주기

# print("{0:+,}".format(1000000000))   #3자리 마다 콤마를 찍고 양수는 +, 음수는 -로 표시
# print("{0:-,}".format(-1000000000))

# #빈자리는 ^로 채우고, 왼쪽정렬, 부호표시해주고, 10자리수 확보, 3자리마다 콤마로 찍어주기
# print("{0:^<+10,}".format(100000))

# print("{0:f}".format(5/3))  #소수점 출력
# print("{0:0.4f}".format(5/3)) #소수점 4번째 자리까지 출력
# print("{0:10.4f}".format(5/3)) #10자리 공간을 만들고 소수점 4번째 자리까지 출력


'''파일 입출력'''

# score_file = open("score.txt", "w", encoding="utf8")  #w는 덮어쓰기를 뜻함, encoding="utf8"로 해줘야 한글도 안깨지고 잘 읽을 수 있음
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()                                #파일을 열었으면 닫아줘야 됨

# score_file = open("score.txt", "a", encoding="utf8")   #a는 덧붙여줌. 기존에 있던 거를 지워주지 않음
# score_file.write("과학 : 80")                          #
# score_file.write("\n코딩 : 100")                       #print()는 자동으로 줄바꿈을 해주지만 .write()는 자동줄바꿈이 없어서 앞에 \n을 붙여서 필요하면 줄바꿈을 해준다.                                 
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")  #r는 파일을 읽어줌
# print(score_file.read())   #파일에 있는 모든 내용을 다 읽어와서 출력해줌
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline())  #줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline())  #한줄만 읽어옴. 그리고 커서를 다음줄로 이동
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="") 
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line)

# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end = "")

# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines()  #list 형태로 저장
# for line in lines:
#     print(line)
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines()  #readlines는 파일의 모든 줄을 읽어서 각각의 줄을 요소로 갖는 리스트로 돌려준다. 근데 각각의 요소 뒤에 \n을 붙여준다.
# for line in lines:
#     print(line, end = "")
# score_file.close()


'''pickle'''             

# #pickle은 프로그램상에서 사용하는 데이터를 파일 형태로 저장, binary형태로 저장해야 한다.
# #리스트나 클래스같은 텍스트 이외의 자료들은 파일 입출력을 사용할 수 없다. 그래서 pickle을 사용한다.

# import pickle
# profile_file = open("nnnaaa.pickle", "wb")    #profile_file은 변수다. open()을 이용해 nnnaaa.pickle을 연 다음에 profile_file에 저장하는 거다.
# profile = {"이름":"박명수", "나이":30, "취미":["축구", "콜프", "코딩"]}
# pickle.dump(profile, profile_file)         #dump(data, file), profile에 있는 정보를 profile_file(nnnaaa.pickle)에 저장
# profile_file.close()

# profile_file = open("nnnaaa.pickle", "rb")
# profile = pickle.load(profile_file)     #profile_file(nnnaaa.pickle)에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()


'''with'''

#with...as을 사용하면 파일을 열고 해당 구문이 끝나면 자동으로 파일이 닫힌다.
#오류가 발상하든 안하든 마지막에 close()를 자동으로 해준다.

# import pickle

# with open("nnnaaa.pickle", "rb") as profile_file:    #with open(파일, 모드) as 파일 객체:, open()으로 불러온 파일을 파일 객체에 저장한다.
#     print(pickle.load(profile_file))

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")

# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())