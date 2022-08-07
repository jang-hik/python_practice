# class unit:
#     def __init__(self, name, hp):        #클래스 안에서 메서드 맨 처음에는 항상 생성된 객체를 받는 self가 온다고 이해하면 된다.
#         self.name = name                         #__init__은 생성자로 객체가 생성되면 자동으로 호출되는 메서드다.
#         self.hp = hp
        
        
# wraith1=unit("레이스", 80, 5)                    #객체를 생성할 때는 객체=클래스()로 만들어 준다.
# print(f"유닛 이름 : {wraith1.name}, 공격력 : {wraith1.damage}")       #객체.객체변수로 객체변수를 클래스 외부로 호출할 수도 있다.

# wraith2=unit("빼앗은 레이스", 80, 5)
# wraith2.clocking = True

# if wraith2.clocking == True:                             
#     print(f"{wraith2.name}는 현재 클로킹 상태입니다.")
# #clocking은 클래스 안에 없는 객체변수다. 이처럼 클래수 외부에서 클래수 내부에 변수를 추가해 줄 수 있다.


# class attack_unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage

#     def attack(self, location):
#         print(f"{self.name}이 {location} 방향으로 공격합니다. [공격력 {self.damage}]")

#     def damaged(self, damage):
#         print(f"{self.name} : {damage} 데미지를 입었습니다.")
#         self.hp -= damage
#         if self.hp <=0:
#             print(f"{self.name}은 파괴되었습니다.")
#         else:
#             print(f"{self.name} : 현재 체력은 {self.hp}입니다.")

# fire_bat=attack_unit("파이어뱃", 50, 16)
# fire_bat.attack("5시") 
# fire_bat.damaged(25)
# fire_bat.damaged(25)

# #상속
# class attack_unit(unit):
#     def __init__(self, name, hp, damage):
#         unit.__init__(self, name, hp)
#         self.damage = damage

#     def attack(self, location):
#         print(f"{self.name}이 {location} 방향으로 공격합니다. [공격력 {self.damage}]")

#     def damaged(self, damage):
#         print(f"{self.name} : {damage} 데미지를 입었습니다.")
#         self.hp -= damage
#         if self.hp <=0:
#             print(f"{self.name}은 파괴되었습니다.")
#         else:
#             print(f"{self.name} : 현재 체력은 {self.hp}입니다.")

# fire_bat=attack_unit("파이어뱃", 50, 16)
# fire_bat.attack("5시") 
# fire_bat.damaged(25)
# fire_bat.damaged(25)


# #다중상속
# class unit:
#     def __init__(self, name, hp):        
#         self.name = name                        
#         self.hp = hp

# class attack_unit(unit):
#     def __init__(self, name, hp, damage):
#         unit.__init__(self, name, hp)
#         self.damage = damage

#     def attack(self, location):
#         print(f"{self.name}이 {location} 방향으로 공격합니다. [공격력 {self.damage}]")

#     def damaged(self, damage):
#         print(f"{self.name} : {damage} 데미지를 입었습니다.")
#         self.hp -= damage
#         if self.hp <=0:
#             print(f"{self.name}은 파괴되었습니다.")
#         else:
#             print(f"{self.name} : 현재 체력은 {self.hp}입니다.")

# class flyable: 
#     def __init__(self, flying_speed):
#         self.flying_speed=flying_speed

#     def fly(self, name, location):
#         print(f"{name} : {location} 방향으로 날아갑니다. [속도 : {self.flying_speed}]")

# class flyalbe_attack_unit(attack_unit, flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         attack_unit.__init__(self, name, hp, damage)
#         flyable.__init__(self, flying_speed)

# valkyrie=flyalbe_attack_unit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")


# #메소드 오버라이딩
# class unit:
#     def __init__(self, name, hp, speed):        
#         self.name = name                        
#         self.hp = hp
#         self.speed = speed

#     def move(self, location):
#         print("지상 유닛 이동")
#         print(f"{self.name}이 {location}으로 이동합니다.")

# class attack_unit(unit):
#     def __init__(self, name, hp, speed, damage):
#         unit.__init__(self, name, hp, speed)
#         self.damage = damage

#     def attack(self, location):
#         print(f"{self.name}이 {location} 방향으로 공격합니다. [공격력 {self.damage}]")

#     def damaged(self, damage):
#         print(f"{self.name} : {damage} 데미지를 입었습니다.")
#         self.hp -= damage
#         if self.hp <=0:
#             print(f"{self.name}은 파괴되었습니다.")
#         else:
#             print(f"{self.name} : 현재 체력은 {self.hp}입니다.")

# class flyable: 
#     def __init__(self, flying_speed):
#         self.flying_speed=flying_speed

#     def fly(self, name, location):
#         print(f"{name} : {location} 방향으로 날아갑니다. [속도 : {self.flying_speed}]")

# class flyalbe_attack_unit(attack_unit, flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         attack_unit.__init__(self, name, hp, 0, damage)
#         flyable.__init__(self, flying_speed)

#     def move(self, location):
#         print("공중 유닛 이동")
#         self.fly(self.name, location)

# vulture = attack_unit("벌쳐", 80, 10, 20)
# battle_crusier = flyalbe_attack_unit("배틀크루져", 500, 25, 3)

# vulture.move("11시")
# battle_crusier.move("5시")


# class unit:
#     def __init__(self, name, hp, speed):        
#         self.name = name                        
#         self.hp = hp
#         self.speed = speed
#         print(f"{name}이 생성되었습니다.")

#     def move(self, location):
#         print("지상 유닛 이동")
#         print(f"{self.name}이 {location}으로 이동합니다.")

#     def damaged(self, damage):
#         print(f"{self.name} : {damage} 데미지를 입었습니다.")
#         self.hp -= damage
#         if self.hp <=0:
#             print(f"{self.name}은 파괴되었습니다.")
#         else:
#             print(f"{self.name} : 현재 체력은 {self.hp}입니다.")

# class attack_unit(unit):
#     def __init__(self, name, hp, speed, damage):
#         unit.__init__(self, name, hp, speed)
#         self.damage = damage

#     def attack(self, location):
#         print(f"{self.name}이 {location} 방향으로 공격합니다. [공격력 {self.damage}]")

# class flyable: 
#     def __init__(self, flying_speed):
#         self.flying_speed=flying_speed

#     def fly(self, name, location):
#         print(f"{name} : {location} 방향으로 날아갑니다. [속도 : {self.flying_speed}]")

# class flyalbe_attack_unit(attack_unit, flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         attack_unit.__init__(self, name, hp, 0, damage)
#         flyable.__init__(self, flying_speed)

#     def move(self, location):
#         print("공중 유닛 이동")
#         self.fly(self.name, location)

# class marine(attack_unit):
#     def __init__(self):
#         attack_unit.__init__(self, "마린", 40, 1, 5)

#     def stimpack(self):
#         if self.hp > 10:
#             self.hp -= 10
#             print(f"{self.name}스팀팩을 사용합니다.")
#         else:
#             print(f"{self.name}의 체력이 부족합니다.")

# class tank(attack_unit):

#     def __init__(self):
#         attack_unit.__init__(self, "탱크", 150, 1, 35)
#         self.seize_mode = False

#     def set_seize_mode(self):
#         if self.seize_mode == False:
#             print(f"{self.name} : 시즈모드로 전환합니다.")
#             self.damage *=2
#             self.seize_mode == True
#         else:
#             print(f"{self.name} : 시즈모드를 해제합니다.")
#             self.damage /=2
#             self.seize_mode = False

# class wraith(flyalbe_attack_unit):
#     def __init__(self):
#         flyalbe_attack_unit.__init__(self, "레이스", 80, 20, 5)
#         self.clocked = False

#     def clocking(self):
#         if self.clocked == True:
#             print(f"{self.name} : 클로킹 모드 해제합니다.")
#             self.clocked = False
#         else:
#              print(f"{self.name} : 클로킹 모드 해제합니다.")
#              self.clocked = True

# def game_start():
#     print("게임을 시작합니다.")

# def game_over():
#     print("gg")

# game_start()

# m1=marine()
# t1=tank()
# w1=wraith()

# attack_units = []
# attack_units.append(m1)
# attack_units.append(t1)
# attack_units.append(w1)

# for i in attack_units:
#     if isinstance(i, marine):
#         i.stimpack()
#     elif isinstance(i, tank):
#         i.set_seize_mode()
#     elif isinstance(i, wraith):
#         i.clocking()


# #__str__        인스턴스가 문자열로 어떻게 표현될지 결정해 주는 함수

# #__str__을 쓰지 않은 클래스
# class cha():
#     def __init__(self, name, level):
#         self.name=name
#         self.level=level

# a=cha("장형익", 100)
# print(a.name)
# print(a.level)
# #__str__을 쓰지 않으면 인스턴스.객체변수 의 형태로 입력해야 한다.

# #__str__을 쓴 클래스
# class cha():
#     def __init__(self, name, level):
#         self.name=name
#         self.level=level

#     def __str__(self):
#         return f"닉네임 {self.name}, 레벨 {self.level}"

# a=cha("장형익", 100)
# print(a)
# #__str__로 인스턴스가 문자열로 어떻게 출력될지 정해줘서 위에처럼 써주지 않고 print(인스터스)을 입력하면
# #__str__메서드의 return값에서 지정한 방식으로 출력이 된다.