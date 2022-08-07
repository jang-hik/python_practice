'''print'''

# animal = "강아지"
# name = "바둑이"
# age = 4
# hobby = "산책"
# is_adult = age >= 3

# print("우리집 " + animal + "의 이름은 " + name + "예요")
# print(name + "는" + str(age) + "살이며," + hobby + "을 아주 좋아해요")
# print(name, "는", age, "살이며,", hobby, "을 아주 좋아해요")
# print(name, "는 어른일까요? ", is_adult)

#print()안에서 str끼리 연결할 때는 +로 연결하는데 이때 int나 boolean도 str로 바꿔줘야 된다. 띄어쓰기가 되지 않고 바로 연결이 된다.
#print()안에서 ,로 연결할 수도 있는데 이때는 int나 boolean도 str로 바꿔주지 않고 쓸 수 있다. 대신 띄어쓰기가 되서 연결이 된다. 


# for i in range(2,10):             #print(object1, object2, ... sep='', end = "")로 프린트문은 구성되어 있다. 
#      for j in range(1, 10):       #object는 출력될 개체로서 여러 개 출력 가능하며 ,로 구분한다.
#          print(i*j, end=" ")      #sep=""는 object가 여러 개 일때 object를 구분해주는 문자다. default는 ''이다.
#      print('홀라')                #end=""는 print문이 끝났을 때 어떻게 끝내주는지 정해주며 default값은  \n이다.

# for i in range(2,10):        
#      for j in range(1, 10):   
#          print(i*j, end=" ") 


'''수식'''

# print(3)
# print(2+3)
# print(5*2)
# print(10/2)

# print(2**3) #몇 제곱해줌
# print(5%3) #나머지를 구해줌
# print(10%3) 
# print(5//3) 몫을 구해줌
# print(10//3)

# print(10>3)
# print(4>=7)
# print(3+4 == 7)

# print(1 != 3)
# print(not(1!=3))

# print((3>0) and (3<5))
# print((3>0)&(3<5))

# print((3>0) or (3>5))
# print((3>0) | (3>5)) 

# print(5>4>3)
# print(5>4>7)

# print(2+3*4)
# print((2+3)*4)

# n = 2 +3*4
# print(n)

# n += 2
# print(n)

# n *=2
# print(n)

# n/=2
# print(n)

# n -=2
# print(n)

# n%=5
# print(n)

'''숫자 함수'''
# print(abs(-5)) 절댓값함수
# print(4**2) 앞에꺼를 뒤에꺼로 제곱
# print(pow(4,2)) #앞에꺼를 뒤에꺼로 제곱 함수
# print(max(1,2,3)) #최댓값함수
# print(min(1,2,3)) #최솟값함수
# print(round(3.4)) #반올림함수
# print(round(3.5)) 

# from math import *
# print(floor(4.77)) #내림함수
# print(ceil(3.13)) #올림함수
# print(sqrt(16)) #제곱근을 구해주는 함수


'''랜덤함수'''
#from random import *
#print(random()) #0부터 1미만의 수를 랜덤 생성
#print(random()*10) # 0부터 10미만 수를 랜덤 생성
#print(random()*2) # 0부터 2미만 수를 랜덤 생성
#print(int(random()*10)) #0부터 10미만의 정수를 랜덤으로 생성
#print(int(random()*3)+1) #1부터 3이하의 정수를 랜덤으로 생성
   
#print(randrange(1,5)) #1부터 5미만의 수를 int형으로 랜덤 생성

#print(randint(1,5)) #1부터 5이하의 수를 int형으로 랜덤생성


'''string 함수'''

# index
# p="Python is Amaizing"
# print(p.index("A")) #찾는 문자열의 위치를 알려주는 함수
# print(p.index('n',6)) #뒤는 시작위치, 시작위치도 포함해서 앞의 문자를 찾으라는 뜻

#index 응용
# p="Python is Amaizing"
# i = p.index("n")
# print(i)
# i=p.index('n', i+1)
# print(i)

#find
# p="Python is Amainzing"
# print(p.find("java")) #find는 index와 똑같지만 없는 값을 입력하면 -1이 나온다.
# print(p.index("java")) #하지만 index는 없는 값을 입력하면 오류가 뜬다.

# #그외 함수
# p="Python is Amaizing"
# print(p.count('n')) #count는 찾는 문자열의 개수를 세준다.
# print(p.lower()) #lower는 문자열을 소문자로 만들어준다.
# print(p.upper()) #upper는 문자열을 대문자로 만들어준다.
# print(p[0].isupper()) #isupper는 문자가 대문자이면 True 값을 준다. 
# print(p[0].islower()) #islower는 문자가 소문자이면 True 값을 준다.
# print(len(p)) #len은 문자열의 길이를 나타내준다.
# print(p.replace("is", "as")) #replace는 앞에꺼를 뒤에꺼로 바꿔준다.


'''슬라이스'''

# j = "981117-1398415"
# print("성별 :" +j[7])
# print("생년원일 :" +j[:6]) #0부터 6번째 자리 직전까지
# print("뒷자리:" +j[7:]) #7부터 뒤에 끝까지
# print("주민번호 :" +j[:]) #전체 다 가져옴
# print("뒷자리:" +j[-7:]) #뒤에서부터 -1, 앞은 0부터 센다


'''formating'''

# print("나는 %d살입니다." %20) # %d는 int포맷팅이다.
# print("나는 %s을 좋아해요." %"파이썬") # %s는 문자열 포맷팅이다.
# print("나는 %s살입니다." %24) # %s는 모든 형태가 다 올수있다. 왜냐하면 전부 str로 바뀌버리기 때문이다.
# print("Apple은 %c로 시작해요" %"A") # %c는 캐릭터이다. 한 글자만 올 수 있다.
# print("나는 %s색과 %s색을 좋아해요." %("파란", "빨강")) #여러개도 가능, 순서대로 들어온다.
# print("나는 %d%%의 지분을 가지고 있다." %80) #포맷팅을 한 상태에서 %를 그대로 출력하고 싶으면 %%로 쓴다.
# print("나는 80%의 지분을 가지고 있다.")

#format함수를 이용한 포맷팅
# print("나는 {}살 입니다.".format(20)) 
# print("나는 {}색과 {}색을 좋아해요".format("파란", "빨강"))
# print("나는 {0}색과 {1}색을 좋아해요".format("파란", "빨강"))
# print("나는 {1}색과 {0}색을 좋아해요".format("파란", "빨강"))

# print("나는 {age}살이여 {color}색을 좋아해요".format(age=20, color="빨강"))
# print("나는 {age}살이여 {color}색을 좋아해요".format(color="빨강", age=20))

# age = 20
# color = "빨강"
# print(f"나는 {age}살이며, {color}색을 좋아해요")


'''escape code'''

# print("저는 '파이썬'입니다") #""안에 ''를 써주면 ''가 그대로 나온다.
# print('저는 "파이썬"입니다') #''안에 ""를 써주면 ""가 그대로 나온다.
# print("저는 \"나도코딩\"입니다") #\"를 쓰면 \뒤에 "가 그대로 나온다. 
# print("저는 \'나도코딩\'입니다") #\'를 쓰면 \뒤에 '가 그대로 나온다.

#C:\Users\wkdgu\OneDrive\바탕 화면\nadocoding> 경로를 표현하고 싶어서 이 문장을 프린트함수로 출력할라하면 \때문에 오류가 뜬다.
# print("C:\\Users\\wkdgu\\OneDrive\\바탕 화면\\nadocoding> ") #\\로 써주면 첫번째\뒤의 두번째\가  \ 자체로 인식이 되서 오류없이 출력이 된다.

# print("안녕\하세요") #위의 경로에서는 \때문에 오류가 떠서 \만 써주면 안 됐는데 이 문장은 오류없이 출력이 된다.
# print("안녕\\하세요") #\\를 두 번 써줘서 \가 하나만 출력이 된다. 

# print("백문이 불여인결\n 백견이 불여일타") #\n은 줄을 바꿔준다.

#\r 뒤에 나오는 문자를 맨 앞으로 옮겨준다. 근데 자리를 추가해서 넣어주는게 아니라 \r 뒤에 나오는 문자만큼 앞에 있는 문자를 대체해 준다.
# print("는 재무회계가 에이쁠이다. \r나")
# print("은 재무회계가 에이쁠이다. \r장형익")

# print("redd\bapple") #\b는 백스페이스 역할을 해서 \b 뒤에 나오는 문자를 \b앞에 한 글자를 지워주고 넣어준다.

# print("red\tapple") #\t는 탭과 같은 역할을 한다.


'''리스트 []'''

# subway = [10, 20, 30]
# print(subway)
# subway=['유재석', '조세호', '박명수']
# print(subway)

# print(subway.index('조세호')) #index

# subway.append('하하') #append()는 객체를 리스트 맨 뒤에 첨부함, 어떤 자료형태도 다 첨부 가능
# print(subway)

# subway.insert(1,"정형돈") #insert()는 객체를 몇 번째 자리에 삽입함
# print(subway)

# print(subway.pop()) #pop()은 리스트 맨 뒤의 객체를 밖으로 끄집어내줌
# print(subway)

# print(subway.count('유재석')) #count는 리스트 안의 객체의 수를 세줌

# num=[1,8,3,4,6,9] #sort()는 오름차순으로 정렬해줌
# num.sort()
# print(num)

# num=[1,8,3,4,6,9] #reverse()는 순서를 뒤집어줌
# num.reverse() 
# print(num)

# num=[1,8,3,4,6,9] #clear()는 리스트 안의 객체를 모두 지워줌
# num.clear()
# print(num)

# a_list=['파이썬', 20, True]  #extend()는 리스트를 확장해줌. extend안에는 리스트밖에 못옴
# b_list=[1,2,3,4,5]
# a_list.extend(b_list)
# print(a_list)


# #다양한 자료들도 리스트 안에 함께 들어갈 수 있음
# a_list=['파이썬', 20, True]
# print(a_list)


'''딕셔너리{}'''

#cabinet = {3:"유재석", 100:"김태호"}
# print(cabinet[3])
# print(cabinet[100])
# print(cabinet.get(3))

# #print(cabinet[5]) #[]을 써서 딕셔너리 안에서 없는 키값을 가져오면 오류가 나온다.
# print(cabinet.get(5)) #하지만 get()을 쓰면 없는 키값을 가져와도 None이라는 메세지가 뜨고 오류가 나지 않는다.
# print(cabinet.get(5, "5가 없으면 이 메세지를 띄워라")) #get()은 찾는 키값이 없을 때 대신 띄우는 메세지도 설정할 수 있다.
# print("hi")

# print(3 in cabinet) #in을 이용해서 딕셔너리에서 키값이 있는지 없는지 찾을 수도 있다.
# print(5 in cabinet)

# print(cabinet)
# cabinet[3] = "김종국" #기존에 있던 값을 업데이트도 가능
# cabinet[10] = "조세호" #딕셔너리에 추가도 가능
# print(cabinet)

# del cabinet[3] #del을 이용해서 삭제도 가능
# print(cabinet)

# print(cabinet.keys()) #keys()을 이용해 키값만 출력가능. dict_keys([키값, 키값, 키값, ....])의 형태로 나옴
# print(cabinet.values()) #values()을 이용해 value값만 출력가능. dict_values([value값, value값, ...])의 형태로 나옴

# print(cabinet.items()) #items()을 이용해 key,value 쌍으로 출력가능. dict_items([(키,밸류), (키,밸류)...])의 형태로 나옴

# cabinet.clear()
# print(cabinet) #clear()을 이용해 모든 값을 다 지울 수 있음


'''튜플()'''
# #튜플은 수정이나 삭제가 안된다.

# menu = ("돈까스", "치즈까스")
# print(menu[0])
# print(menu[1])

# t1 = ()
# print(t1, type(t1))

# t2 = (1,)
# print(t2, type(t2))

# t21 = (1)             #()안에 int하나만 들어가면 (1)은 int형이다.
# print(t21, type(t21))

# t3 = 1, 2, 3
# print(t3, type(t3))

# (name, age, major) = ("장형익", "24", "경제")
# print((name, age, major))

# (name, age, major) = "장형익", "24", "경제"
# print((name, age, major))


'''집합'''
#집합은 중복이 안되고 순서가 없다.

# s0={1,2,3}
# print(s0)

# s1 = set([1,2,3, "바둑이", "멍멍이",6,6,6]) #s1 = set(1,2,3)이렇게 하면 오류가 뜬다. 
# print(s1)

# s2 = set("Hello") 
# print(s2)

# s3 = set(["Hello"]) 
# print(s3)

# my_set = {1,2,3,3,3,3}
# print(my_set)

# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석", "박명수","김종국", "바둑이", "멍멍이", "멍멍이"]) #set("유재석", "박명수") 이렇게 하면 오류가 뜬다. 
# print(java)
# print(python)

# my_set = {1,2,3,3,3,3}
# print(my_set)

# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석", "박명수"])
# print(java)
# print(python)

# #교집합이다.
# print(java & python) 
# print(java.intersection(python)) 

# #합집합
# print(java | python)
# print(java.union(python))

# #차집합
# print(java - python)
# print(java.difference(python))

# python.add("김태호") #추가
# print(python)

# java.remove("김태호") #제거
# print(java)







