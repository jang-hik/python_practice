
'''242'''
# from datetime import *          #datetime이라는 모듈이 있음. 
# now=datetime.now()              #모듈에 datetime이라는 클래스가 있음, 클래스 안에 현재 시간을 표시해주는 now()함수가 있음
# print(now, type(now))           

'''243'''
# from datetime import *
# now=datetime.now()                    
# a=timedelta(days=1)           #datetime이라는 모듈안에 timedelta라는 클래스가 있음
# print(now + a, type(now + a))     #timedelta클래스를 timedelta(days=숫자)로 써주면 숫자만큼 날짜가 뒤로 간다.(미래로)

# b=timedelta(days=-1)               #timedelta클래스를 timedelta(days=-숫자)로 써주면 숫자만큼 날짜가 앞으로로 간다.(과거로)
# print(now + b, type(now + b))     

# for i in range(-5,0):
#     c=timedelta(days=i)
#     print(now + c)


'''244'''
# from datetime import *            #datetime이라는 strftime이라는 시간값을 문자열형태로 바꿔주는 함수가 있음
# now = datetime.now()              
# a = now.strftime("%H:%M:%S")          
# print(a, type(a))

'''245'''
# from datetime import *               
# day = "2020-05-04"                       #datetime이라는 모듈안에 strptime이라는 함수가 있다.
# a=datetime.strptime(day, "%Y-%m-%d")          #strptime은 문자열을 시간값으로 바꿔준다.
# print(a, type(a))

'''246'''
# from time import *         #time모듈안에 sleep라는 함수가 있다.
# print("hello")             #python interpreter는 35, 36, 37을 동시에 읽어주는데 sleep(숫자)를 써주면 숫자만큼 다음 코드의 실행을 멈춰준다.
# sleep(4)                   #sleep(4)를 써줘서 hello를 출력하고 4초 뒤에 again을 출력해줬다.
# print("again")



'''247'''
#모듈을 임포트하는 4가지 방식에 대해 설명해보시오
#os모듈을 임포트해와서 그 안에 있는 rename 함수를 쓴다고 가정

# import os                  #os모듈을 임포트함,                                                함수를 쓰는 법 : os.rename()
# from os import rename      #os모듈의 rename함수만 임포트함,                                  함수를 쓰는 법 : rename()
# from os import *           #os모듈의 모든 함수를 임포트함,                                   함수를 쓰는 법 : rename()  
# import os as myos          #os모듈을 myos이름으로 임포트함, 기존 모듈의 이름이 너무 길때 씀,   함수를 쓰는 법 : myos.rename()

#권장되는 방법은 첫번째임, 세번째나 두번째 방식으로 함수를 수입하면 만약에 os와 requests라는 두개의 모듈을 수입해왔는데 두 개의 모듈안에 똑같이
#a()라는 함수가 있으면 a()로 함수를 써줄 때 이 함수가 어디에서 임포트해왔는지 헷갈림


'''248'''
# from os import *
# a = getcwd()                   #getcwd()는 current working directory의 줄임말로 현재 작업하는 디렉토리의 경로를 화면에 출력해준다.
# print(a, type(a))

'''249'''
# from os import *             #os는 운영체제에 관한 모듈이다                           
# rename("C:\\Users\\wkdgu\\OneDrive\\바탕 화면\\before.txt","C:\\Users\\wkdgu\\OneDrive\\바탕 화면\\after.txt")         
# rename("C:/Users/wkdgu/OneDrive/바탕 화면/before.txt")     

#rename(a,b)는 파일의 이름을 바꾸어준다.

#디렉토리 구분자를 /로 표현해도 된다. 
#문자열에서 \을 쓰고 싶으면 \\써야 \로 인식이 된다.


'''250'''
# for i in range(0, 10, 2):         #range(a,b,c)는 a~b-1까지 c단위로 int를 반환한다. c는 int만 가능하고 float형태는 불가능하다.
#     print(i)



'''254'''
# class human:
#     def __init__(self):
#         print("응애응애")

# areum=human()

'''255~256'''
# class human:
#     def __init__(self, name, age, sex):
#         self.name=name
#         self.age=age
#         self.sex=sex
        
# areum=human("조아름", 25, "여자")

# print(areum.name)
# print(areum.age)
# print(areum.sex)

'''257'''
# class human:
#     def __init__(self, name, age, sex):
#         self.name=name
#         self.age=age
#         self.sex=sex
        
#     def who(self):
#         print(f"이름 : {self.name}, 나이 : {self.age}, 성별 : {self.sex}")

# areum=human("조아름", 25, "여자")
# areum.who()

'''258'''
# class human:
#     def __init__(self, name, age, sex):
#         self.name=name
#         self.age=age
#         self.sex=sex
        
#     def who(self):
#         print(f"이름 : {self.name}, 나이 : {self.age}, 성별 : {self.sex}")

#     def setinfo(self, name, age, sex):
#         self.name=name
#         self.age=age
#         self.sex=sex

# areum=human("불명", "미상", "모름")
# areum.who()

# areum.setinfo("아름", 25, "여자")
# areum.who()

'''259'''                    #__del__(self) 는 소멸자로서 객체를 소멸시켜 준다.
# class human:
#     def __init__(self, name, age, sex):
#         self.name=name
#         self.age=age
#         self.sex=sex
        
#     def who(self):
#         print(f"이름 : {self.name}, 나이 : {self.age}, 성별 : {self.sex}")

#     def setinfo(self, name, age, sex):
#         self.name=name
#         self.age=age
#         self.sex=sex

#     def __del__(self):
#         print("객체가 소멸되었습니다.")

# a=human("송바둑", 25, "여자")
# a.who()
# del a

'''262'''
# class stock:
#     def __init__(self, name, code):
#         self.name=name
#         self.code=code

# s=stock("삼성전자", "005930")
# print(s.name)
# print(s.code)
        
'''263'''
# class stock:
#     def __init__(self, name, code):
#         self.name=name
#         self.code=code

#     def set_name(self, name):
#         self.name=name

# s=stock("none", "none")
# s.set_name("삼성전자")
# print(s.name, s.code)

'''264'''
# class stock:
#     def __init__(self, name, code):
#         self.name=name
#         self.code=code

#     def set_name(self, name):
#         self.name=name

#     def set_code(self, code):
#         self.code=code

# s=stock("none", "none")
# s.set_name("삼성전자")
# s.set_code("005930")
# print(s.name, s.code)

'''266~267'''
# class stock:
#     def __init__(self, name, code, per, pbr, div):
#         self.name=name
#         self.code=code
#         self.per=per
#         self.pbr=pbr
#         self.div=div

#     def set_name(self, name):
#         self.name=name

#     def set_code(self, code):
#         self.code=code

# samsung=stock("삼성전자", "005930", 15.79, 1.33, 2.83)

'''268'''
# class stock:
#     def __init__(self, name, code, per, pbr, div):
#         self.name=name
#         self.code=code
#         self.per=per
#         self.pbr=pbr
#         self.div=div

#     def set_name(self, name):
#         self.name=name

#     def set_code(self, code):
#         self.code=code   

#     def set_per(self, per):
#         self.per=per

#     def set_pbr(self, pbr):
#         self.pbr=pbr

#     def set_div(self, div):
#         self.div=div

# samsung=stock("삼성전자", "005930", 15.79, 1.33, 2.83)
# print(samsung.per)

# samsung.set_per(12.75)
# print(samsung.per)

'''270'''
# class stock:
#     def __init__(self, name, code, per, pbr, div):
#         self.name=name
#         self.code=code
#         self.per=per
#         self.pbr=pbr
#         self.div=div

# samsung=stock("삼성전자", "005930", 15.79, 1.33, 2.83)
# hyundai=stock("현대차", "005390", 8.70, 0.35, 4.27)
# lg=stock("LG전자", "0066570", 317.34, 0.69, 1.37)

# kospi=[]
# kospi.append(samsung)
# kospi.append(hyundai)
# kospi.append(lg)

# for i in kospi:
#     print(i.code, i.per)

'''271'''
# from random import *

# class account:
#     def __init__(self, name, deposit):
#         self.name=name
#         self.deposit=deposit
#         self.bank="SC제일은행"
#         num1=str(randint(0,999)).zfill(3)
#         num2=str(randint(0,99)).zfill(2)
#         num3=str(randint(0,999999)).zfill(6)
#         self.num=num1+"-"+num2+"-"+num3

# a=account("장형익", "1억")
# print(a.name, a.bank, a.deposit, a.num)

'''272'''
# from random import *

# class account:
#     account_count =0
#     def __init__(self, name, deposit):
#         self.name=name
#         self.deposit=deposit
#         self.bank="SC제일은행"
#         num1=str(randint(0,999)).zfill(3)
#         num2=str(randint(0,99)).zfill(2)
#         num3=str(randint(0,999999)).zfill(6)
#         self.num=num1+"-"+num2+"-"+num3

#         account.account_count +=1

# kim=account("김민수", "100만원")
# print(account.account_count)
# lee=account("이민수", "200만원")
# print(account.account_count)

'''273'''
# from random import *

# class account:
#     account_count =0
#     def __init__(self, name, deposit):           #앞에 self가 오면 instance 메서드다
#         self.name=name
#         self.deposit=deposit
#         self.bank="SC제일은행"
#         num1=str(randint(0,999)).zfill(3)
#         num2=str(randint(0,99)).zfill(2)
#         num3=str(randint(0,999999)).zfill(6)
#         self.num=num1+"-"+num2+"-"+num3

#         account.account_count +=1

#     def get_account_num(cls):               #앞에 cls가 오면 class 메서드다. 
#         print(cls.account_count)

# kim=account("김민수", "100만원")
# lee=account("이민수", "200만원")            # class로 지정한 객체 아무거나 클래서 메서드에 써도 괜찮다.
# kim.get_account_num()                      # kim이라는 객체가 메서드로 넘어오지 못한다.

'''274'''
# from random import *

# class account:
#     account_count =0
#     def __init__(self, name, balance):          
#         self.name=name
#         self.balance=balance
#         self.bank="SC제일은행"
#         num1=str(randint(0,999)).zfill(3)
#         num2=str(randint(0,99)).zfill(2)
#         num3=str(randint(0,999999)).zfill(6)
#         self.num=num1+"-"+num2+"-"+num3

#         account.account_count +=1

#     def get_account_num(cls):              
#         print(cls.account_count)

#     def deposit(self, money):
#         if money >= 1:
#             self.balance+=money

'''275'''
# from random import *

# class account:
#     account_count =0
#     def __init__(self, name, balance):          
#         self.name=name
#         self.balance=balance
#         self.bank="SC제일은행"
#         num1=str(randint(0,999)).zfill(3)
#         num2=str(randint(0,99)).zfill(2)
#         num3=str(randint(0,999999)).zfill(6)
#         self.num=num1+"-"+num2+"-"+num3

#         account.account_count +=1

#     def get_account_num(cls):              
#         print(cls.account_count)

#     def deposit(self, money):
#         if money >= 1:
#             self.balance+=money

#     def withdraw(self, money):
#         if money<=self.balance:
#             self.balance-=money

'''276'''
# from random import *

# class account:
#     account_count =0
#     def __init__(self, name, balance):          
#         self.name=name
#         self.balance=balance
#         self.bank="SC제일은행"
#         num1=str(randint(0,999)).zfill(3)
#         num2=str(randint(0,99)).zfill(2)
#         num3=str(randint(0,999999)).zfill(6)
#         self.num=num1+"-"+num2+"-"+num3

#         account.account_count +=1

#     def get_account_num(cls):              
#         print(cls.account_count)

#     def deposit(self, money):
#         if money >= 1:
#             self.balance+=money

#     def withdraw(self, money):
#         if money<=self.balance:
#             self.balance-=money

#     def display_info(self):
#         print(f"은행이름: {self.bank}")
#         print(f"예금주: {self.name}")
#         print(f"계좌번호: {self.num}")
#         print(f"잔고: {self.balance}")

# kim=account("피카츄", 10000)
# kim.display_info()

'''277'''
# from random import *

# class account:
#     account_count =0
    
#     def __init__(self, name, balance):          
#         self.deposit_count = 0
#         self.name=name
#         self.balance=balance
#         self.bank="SC제일은행"
#         num1=str(randint(0,999)).zfill(3)
#         num2=str(randint(0,99)).zfill(2)
#         num3=str(randint(0,999999)).zfill(6)
#         self.num=num1+"-"+num2+"-"+num3

#         account.account_count +=1

#     def get_account_num(cls):              
#         print(cls.account_count)

#     def deposit(self, money):
#         if money >= 1:
#             self.balance+=money
#             self.deposit_count+=1
#             if self.deposit_count%5==0:
#                 self.balance+=self.balance*1.01

#     def withdraw(self, money):
#         if money<=self.balance:
#             self.balance-=money

#     def display_info(self):
#         print(f"은행이름: {self.bank}")
#         print(f"예금주: {self.name}")
#         print(f"계좌번호: {self.num}")
#         print(f"잔고: {self.balance}")

# p=account("파이썬", 10000)
# p.deposit(500)
# p.deposit(500)
# p.deposit(500)
# p.deposit(500)
# p.deposit(500)
# print(p.balance)

'''279'''
# from random import *

# class account:
#     account_count =0
    
#     def __init__(self, name, balance):          
#         self.deposit_count = 0
#         self.name=name
#         self.balance=balance
#         self.bank="SC제일은행"
#         num1=str(randint(0,999)).zfill(3)
#         num2=str(randint(0,99)).zfill(2)
#         num3=str(randint(0,999999)).zfill(6)
#         self.num=num1+"-"+num2+"-"+num3

#         account.account_count +=1

#     def get_account_num(cls):              
#         print(cls.account_count)

#     def deposit(self, money):
#         if money >= 1:
#             self.balance+=money
#             self.deposit_count+=1
#             if self.deposit_count%5==0:
#                 self.balance+=self.balance*1.01

#     def withdraw(self, money):
#         if money<=self.balance:
#             self.balance-=money

#     def display_info(self):
#         print(f"은행이름: {self.bank}")
#         print(f"예금주: {self.name}")
#         print(f"계좌번호: {self.num}")
#         print(f"잔고: {self.balance}")

# data=[]
# p=account("파이썬", 10000)
# j=account("자바", 100000000)
# c=account("c언어", 100000000)

# data.append(p)
# data.append(j)
# data.append(c)

# for i in data:
#     if i.balance>=1000000:
#         i.display_info()
    
'''280'''
# from random import *

# class account:
#     account_count =0
    
#     def __init__(self, name, balance):          
#         self.deposit_count = 0
#         self.withdraw_count = 0
#         self.name=name
#         self.balance=balance
#         self.bank="SC제일은행"
#         num1=str(randint(0,999)).zfill(3)
#         num2=str(randint(0,99)).zfill(2)
#         num3=str(randint(0,999999)).zfill(6)
#         self.num=num1+"-"+num2+"-"+num3

#         account.account_count +=1

#     def get_account_num(cls):              
#         print(cls.account_count)

#     def deposit(self, money):
#         if money >= 1:
#             self.balance+=money
#             self.deposit_count+=1
#             if self.deposit_count%5==0:
#                 self.balance+=self.balance*1.01

#     def deposit_history(self):
#         print(f"총 {self.deposit_count}번 입금했습니다.")

#     def withdraw(self, money):
#         if money<=self.balance:
#             self.balance-=money
#             self.withdraw_count+=1

#     def withdraw_history(self):
#         print(f"총 {self.withdraw_count}번 출금했습니다.")

#     def display_info(self):
#         print(f"은행이름: {self.bank}")
#         print(f"예금주: {self.name}")
#         print(f"계좌번호: {self.num}")
#         print(f"잔고: {self.balance}")
    
# p=account("파이썬", 10000)
# p.deposit(500)
# p.deposit(500)
# p.deposit(500)
# p.deposit(500)
# p.deposit(500)
# p.withdraw(100)
# p.withdraw(100)
# p.withdraw(100)
# p.deposit_history()
# p.withdraw_history()

'''281'''
# class 차:
#     def __init__(self, 바퀴, 가격):
#         self.바퀴=바퀴
#         self.가격=가격

# car=차(2, 1000)
# print(car.바퀴)
# print(car.가격)

'''282'''
# class 차:
#     def __init__(self, 바퀴, 가격):
#         self.바퀴=바퀴
#         self.가격=가격

# class 자전차(차):
#     passclass 차:

'''283'''
# class 차:
#     def __init__(self, 바퀴, 가격):
#         self.바퀴=바퀴
#         self.가격=가격

# class 자전차(차):
#     def __init__(self, 바퀴, 가격):
#         self.바퀴=바퀴
#         self.가격=가격

# bicycle = 자전차(2,100)
# print(bicycle.가격)

'''284'''
# class 차:
#     def __init__(self, 바퀴, 가격):
#         self.바퀴=바퀴
#         self.가격=가격

# class 자전차(차):
#     def __init__(self, 바퀴, 가격, 구동계):
#         self.바퀴=바퀴
#         self.가격=가격
#         self.구동계=구동계

'''285'''
# class 차:
#     def __init__(self, 바퀴, 가격):
#         self.바퀴=바퀴
#         self.가격=가격

# class 자동차(차):
#     def __init__(self, 바퀴, 가격):
#         self.바퀴=바퀴
#         self.가격=가격
    
#     def 정보(self):
#         print(f"바퀴수 {self.바퀴} \n가격 {self.가격}")

# car=자동차(4,1000)
# car.정보()

'''286'''
# class 차:
#     def __init__(self, 바퀴, 가격):
#         self.바퀴=바퀴
#         self.가격=가격

# class 자전차(차):
#     def __init__(self, 바퀴, 가격, 구동계):
#         self.바퀴=바퀴
#         self.가격=가격
#         self.구동계=구동계

#     def 정보(self):
#         print(f"바퀴수 {self.바퀴} \n가격 {self.가격} \n구동계 {self.구동계}")

# bicycle=자전차(2, 100, "시마노")
# bicycle.정보()

'''291'''
# with open("매수종목1.txt", "w") as f:          #write()에는 string만 입력가능하다.
#     f.write("005930\n")
#     f.write("005930\n")
#     f.write("035420\n")

'''292'''
# with open(r"C:\Users\wkdgu\OneDrive\바탕 화면\매수종목2.txt", "wt", encoding="utf8") as f:
#     f.write("005930 삼성전자\n")
#     f.write("005380 현대차\n")
#     f.write("035423 NAVER\n")

'''293'''   #csv파일은 엑셀 파일의 한 종류고 사실은 텍스트 파일이다. 약자난 comma seperated value이다
# import csv

# with open(r"C:\Users\wkdgu\OneDrive\바탕 화면\매수종목.csv", "wt", encoding="cp949", newline="") as f:  #엑셀에서 한글을 잘 인식하기 위해 만든 cp949로 인코딩함
#     writer=csv.writer(f)
#     writer.writerow(["종목명", "종목코드", "PER"])
#     writer.writerow(["삼성전자", "005930", 15.79])
#     writer.writerow(["NAVER", "035420", 55.82])

'''294'''
# with open("매수종목1.txt", "r") as f:        
#     a=[]
#     lines=f.readlines()
#     for i in lines:
#         a.append(i.strip())
# print(a)

# #whitespace란 띄어쓰기, 탭(\t), 엔터(\n)까지 포괄적으로 애기하는 것.
# #whitespace를 제거하기 위해서는 strip()을 이용하면 된다.
# #strip()은 문자열 맨 앞과 맨 뒤의 whitespace를 제거해주며 중간에 있는 whitespace는 제거가 안된다.  

'''295'''
# data={}
# with open(r"C:\Users\wkdgu\OneDrive\바탕 화면\매수종목2.txt", "r", encoding="utf8") as f:
#     liens=f.readlines()
#     for i in liens:
#         a=i.strip()
#         k,v=a.split()
#         data[k]=v
# print(data)

'''296'''
# per = ["10.31", "", "8.00"]

# for i in per:
#     try:
#         print(float(i))
#     except:
#         print(0)

'''297'''
# per = ["10.31", "", "8.00"]
# a=[]
# for i in per:
#     try:
#         a.append(float(i))
#     except:
#         a.append(0)
# print(a)

'''298'''
# a=[2,4,6,0,2,4,6,0]
# b=12
# for i in a:
#     try:
#         result=b/i
#         print(result)
#     except ZeroDivisionError as er:
#         print(er)

'''299'''
# data = [1, 2, 3]

# for i in range(5):
#     try:
#         print(data[i])
#     except IndexError as e:
#         print(e)

'''300'''
# per = ["10.31", "", "8.00"]

# for i in per:
#     try:
#         print(float(i))
#     except:
#         print("에러가 발생했습니다.")
#     else:
#         print("clean data")
#     finally:
#         print("데이터가 출력됩니다.")








