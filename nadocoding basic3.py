'''예외처리'''
# try:
#     num1=int(input("첫번째 숫자:"))
#     num2=int(input("두번째 숫자:"))
#     result=num1/num2
#     print(f"{num1}/{num2}={result}")
# except ValueError:
#     print("에러! 잘못된 값을 입력하였습니다.")
# except ZeroDivisionError as err:
#     print(err)
    
# try:
#     nums=[]
#     nums.append(int(input("첫번째 숫자:")))
#     nums.append(int(input("두번째 숫자:")))
#     # nums.append(nums[0]/nums[1]) 0번째와 1번째는 들어가있는데 2번째를 리스트에 안넣음
#     print(f"{nums[0]}/{nums[1]}={nums[2]}")
# except ValueError:
#     print("에러! 잘못된 값을 입력하였습니다.")
# except ZeroDivisionError as err:
#     print(err)
# except:                                          #위에서 찾지 못한 에러는 모두 여기서 처리한다.
#     print("알 수 없는 에러가 발생하였습니다.")

# try:
#     nums=[]
#     nums.append(int(input("첫번째 숫자:")))
#     nums.append(int(input("두번째 숫자:")))
#     # nums.append(nums[0]/nums[1]) 0번째와 1번째는 들어가있는데 2번째를 리스트에 안넣음
#     print(f"{nums[0]}/{nums[1]}={nums[2]}")
# except ValueError:
#     print("에러! 잘못된 값을 입력하였습니다.")
# except ZeroDivisionError as err:
#     print(err)
# except Exception as err:              #어떤 에러인지 에러 메세지를 표시해 준다.                              
#     print(err)


'''에러 발생시키기'''
#한 자리 숫자만 나누는 계산기를 만드는데 두자리 이상의 숫자가 입력되면 의도적으로 에러를 발생시키려고 함
# try:
#     num1=int(input("분자를 입력하세요:"))
#     num2=int(input("분모를 입력하세요:"))
#     result=num1/num2
#     if num1>=10 or num2>=10:
#         raise ValueError
#     else:
#         print(f"{num1}/{num2} = {result}")
# except ValueError:
#     print("한자리 숫자만 입력하세요")


'''사용자정의 예외처리'''
#한 자리 수만 나누는 계산기를 만들려고 함. 두자리 이상의 숫자를 입력하면 에러를 띄우고 싶은데 파이썬에서 제공하는 ValueError가 아니라
#내가 임의로 BigNumberError라는 에러를 만들고 싶음

# class BigNumberError(Exception):             #만들고 싶은 에러를 클래스로 만들고 Exception이라는 클래스를 상속받음
#     pass

# try:
#     num1=int(input("분자를 입력하세요:"))
#     num2=int(input("분모를 입력하세요:"))
#     result=num1/num2
#     if num1>=10 or num2>=10:
#         raise BigNumberError            #raise로 임의로 만든 에러를 발생시킴
#     else:
#         print(f"{num1}/{num2} = {result}")
# except ValueError as err:
#     print(err)
# except BigNumberError:
#     print("두자리 이상의 숫자를 입력하셨습니다. 한 자리 숫자를 입력하세요")



# class BigNumberError(Exception):             
#     def __init__(self, msg):
#         self.msg=msg
    
#     def __str__(self):                   
#         return self.msg

# try:
#     num1=int(input("분자를 입력하세요:"))
#     num2=int(input("분모를 입력하세요:"))
#     result=num1/num2
#     if num1>=10 or num2>=10:
#         raise BigNumberError(f"입력값 : {num1}, {num2}")       
#     else:
#         print(f"{num1}/{num2} = {result}")
# except ValueError as e:
#     print(e)
# except BigNumberError as e:
#     print(e)


'''예외처리 finally'''
# class BigNumberError(Exception):             
#     def __init__(self, msg):
#         self.msg=msg
    
#     def __str__(self):                   
#         return self.msg

# try:
#     num1=int(input("분자를 입력하세요:"))
#     num2=int(input("분모를 입력하세요:"))
#     result=num1/num2
#     if num1>=10 or num2>=10:
#         raise BigNumberError(f"입력값 : {num1}, {num2}")       
#     else:
#         print(f"{num1}/{num2} = {result}")
# except ValueError as e:
#     print(e)
# except BigNumberError as e:
#     print(e)
# finally:                                              #finally는 에러가 뜨든 안뜨는 무조건 실행시켜준다.
#     print("계산기를 이용해주셔서 감사합니다.")


'''모듈'''
# import theater
# theater.price(3)
# theater.price_morning(4)
# theater.price_soldier(5)

# import theater as th
# th.price(3)
# th.price_morning(4)
# th.price_soldier(5)

# from theater import *
# price(3)
# price_morning(4)
# price_soldier(5)

# from theater import price, price_morning
# price(4)
# price_morning(4)

# from theater import price_soldier as ps
# ps(4)

'''모듈, 패키지 위치 확인'''
# import inspect
# import random
# print(inspect.getfile(random))


'''내장함수'''         #파이썬이 자체적으로 가지고 있으며 함수를 쓰기위해서 module을 import할 필요가 없다.
#dir()은 객체가 자체적으로 가지고 있는 변수나 함수를 보여준다.
#print(dir([1,2,3]))            #리스트가 가지고 있는 변수나 함수를 보여준다.
#print(dir({'1':'a'}))           #딕셔너리가 가지고 있는 변수나 함수를 보여준다.

# import random                 
# print(dir(random))                 #radom모듈이 가지고 있는 변수나 함수를 보여줌

# name="jim"                  #name이라는 변수가 "jim"이라는 string을 가지고 있으니 string에 쓸 수 있는 것들을 보여줌
# print(dir(name))


'''외장함수'''           #파이썬 안에 있지만 쓰고 싶으면 외장함수가 들어있는 module을 import해야한다. 
# import glob           #glob모듈안에 glob이라는 함수가 있는데 glob함수는 디렉토리 안에 있는 파일들의 이름을 모두 읽어서 리스트로 돌려준다.
# print(glob.glob(r"C:\Users\wkdgu\OneDrive\바탕 화면\nadocoding\*basic*"))  #파일 이름에 nadocoding이 들어가는 모든 파일들을 보여준다.
# a=glob.glob(r"C:\Users\wkdgu\OneDrive\바탕 화면\nadocoding\*.py")        #확장자가 py로 끝나는 모든 파일들을 보여준다.
# for i in a:
#     print(i)


# import os         #운영체제에서 제공하는 기본 기능들이 들었는게 os module이다
# print(os.getcwd())      #getcwd()는 현재 작업이 진행되는 디렉토리를 보여준다.

# f="fold1"
# os.makedirs(f)             #makedirs는 디렉토리를 생성해 주는 함수다. 디렉토리명은 string형태만 가능하다.
# print(f"{f} 폴더를 생성하였습니다.")

# a=os.path.exists("Quiz.py")    #os.path.exists()는 파일이나 폴더가 존재하면 True, 없으면 False를 반환한다.
# print(a)

#os.makedirs("faa")
# os.rmdir("faa")           #rmdir은 디렉터리를 삭제해준다.

# print(os.listdir()) 
# #listdir() method in python is used to get the list of all files and directories in the specified directory.
# #listdir()은 ()안에 경로가 없으면 현재 작업이 진행되는 디렉토리 안에 있는 파일과 폴더들을 리스트 형태로 보여준다.

# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))


# import datetime
# print("오늘 날짜는", datetime.date.today())    

# today = datetime.date.today()
# td=datetime.timedelta(days=100)
# print(today+td)




