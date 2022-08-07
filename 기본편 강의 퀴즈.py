'''Quiz1'''
# a = ["사당", "신도림", "인천공항"]
# for station in a:
#     print(station+"행 열차가 들어오고 있습니다.")


'''Quiz2'''
# from random import  *
# print("오프라인 스터디 모임 날짜는 매월 " + str(randint(4,28)) + "일로 선정되었습니다.")


'''Quiz3 내풀이'''
# a ="http://naver.com/"
# b=a[7:] #b=naver.com/
# c=b.index(".") #c=5
# d=b[:c] #d=naver
# print(d[:3]+str(len(d))+str(d.count('e'))+"!")

# #Quiz3 나도코딩풀이
# url="http://naver.com/"
# my_str=url.replace("http://", "") #my_str=naver.com/
# my_str=my_str[:my_str.index(".")] #my_str=naver
# password = my_str[:3] + str(len(my_str)) + str(my_str.count('e')) + '!' #password = nav51!
# print("생성된 비밀번호 : " + password) 


'''Quiz4'''
#from random import *
# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst) #shuffle은 순서를 무작위로 섞는 함수 
# print(lst)
# print(sample(lst,1)) #sample()은 lst에서 1개를 무작위로 추출

# #내풀이
# comments=range(1,21)
# comments=list(comments)
# shuffle(comments)

# print('--당첨자 발표--')
# print('치킨 당첨자 :'+ str(comments.pop()))
# print('커피당첨자 :' + str(sample(comments,3)))
# print('--축하합니다--') 

# #나도코딩풀이
# comments=range(1,21)
# comments=list(comments)
# shuffle(comments)
# winners = sample(comments, 4)

# print('--당첨자 발표--')
# print('치킨 당첨자 :{0}'.format(winners[0]) )
# print('커피당첨자 :{0}'.format(winners[1:]) )
# print('--축하합니다--') 


'''Quiz5'''
# from random import *
# a = 0
# i = 1
# while i <= 50:              # i는 승객수, 총 50명까지 있음
#     dtime=randint(5,50)     # dtime은 운행소요시간
#     if dtime<=15:
#         print("[o] "+ str(i) +"번째 손님 (소요시간 :" + str(dtime) + "분)")
#         a+=1 
#     elif dtime>15:
#         print("[]"+ str(i) +"번째 손님 (소요시간 : " + str(dtime)+"분)")
#     i+=1
# print("총 탑승 승객 :" + str(a) + "분")

#나도코딩 풀이
# from random import *
# cnt = 0 # 총 탑승 승객 수
# for i in range (1,51):  #승객 수 1~50
#     time = randrange(5,51) # 5~50분이라는 소요시간
#     if 5 <= time <= 15:
#         print("[0] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
#         cnt +=1
#     else:
#         print("[] {0}번째 손님 (소요시간 : {1}분)".format(i, time))

# print("총 탑승 승객 : {0} 분".format(cnt))


'''Quiz6'''
# #내풀이
# def std_weight(height, gender):
#     if gender == "men": 
#         weight=height*height*22
#         height = height*100
#         print(f"키 {height}cm 남자의 표준 체중은 {weight:0.2f}kg 입니다.")
#     elif gender == "women":
#         weight=height*height*21
#         height = height*100
#         print(f"키 {height}cm 여자의 표준 체중은 {weight:0.2f}kg 입니다.")        

# std_weight(1.75, "men")
# std_weight(1.75, "women")

# #나도코딩 풀이
# def std_weight(height, gender):
#     if gender == "남자":
#         return height * height * 22
#     else:
#         return height * height * 21

# height = 175
# gender = "남자"
# weight = round(std_weight(height / 100, gender), 2)
# print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))


'''Quiz7'''
# for i in range(1,51):
#     with open(f"{i}주차.txt", "w", encoding="utf8") as report:
#         report.write(f"- {i} 주차 주간보고 -\n부서 :\n이름 :\n업무 요약 :\n ")


'''Quiz8'''
# class house:
#     def __init__(self, location, house, deal, price, year):
#         self.location=location
#         self.house=house
#         self.deal=deal
#         self.price=price
#         self.year=year

#     def show(self):
#         print(self.location, self.house, self.deal, self.price, self.year)

# g=house("강남", "아파트", "매매", "10억", "2010년")
# g.show()


'''Quiz9'''
# chi=10
# wait=1          #홀 안은 현재 만석. 대기번호 1번부터 시작

# class SoldOutError(Exception):
#     pass

# try:
#     while True:
#         print(f"[남은치킨 : {chi}]")
#         order = int(input("치킨 몇 마리 주문하시겠습니까?"))
#         if order <=0:
#             raise ValueError
#         if order > chi: 
#             print("재료가 부족합니다.")
#         else:
#             print(f"[대기번호 {wait}] {order} 마리 주문이 완료되었습니다.")
#             wait +=1
#             chi -= order
#         if chi==0:
#             raise SoldOutError
#             break
# except ValueError:
#     print("잘못된 값을 입력하였습니다.")
# except SoldOutError:
#     print("재고가 소진되어 더 이상 주문을 받지 않습니다.")


'''Quiz10'''
# import byme
# byme.sign()


















