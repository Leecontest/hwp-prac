import turtle as t


t.bgcolor("skyblue")
t.color("brown")

            #에펠탑그리기
t.speed(0)
t.lt(90)
t.up()      #꼭대기를 위로 올리기 위해 올라가는 과정은 펜을 닿지 않게하기 위함
t.fd(300)
t.rt(180)
t.down()    # 펜을 위로 올렸으니 이제 부터 그리기 시작
t.fd(20)
t.lt(90)
t.begin_fill()  #색을 채우기 위함
t.fd(5)
t.rt(90)
t.fd(5)
t.rt(90)
t.fd(10)
t.rt(90)
t.fd(5)
t.rt(90)
t.fd(10)
t.end_fill()    #색 채우기 끝
t.rt(90)        # 꼭대기와 상단부 사이의 모형
t.fd(5)
t.rt(90)
t.fd(5)
t.lt(90)
t.fd(5)
t.rt(90)
t.fd(4)
t.rt(90)
t.fd(5)
t.rt(90)
t.fd(8)
t.rt(90)
t.fd(5)
t.rt(90)
t.fd(4)
t.lt(90)

for x in range(1,11):   #점차 넓어지는 에펠탑의 상단부를 표현하기 위함
    t.fd(2*x+2) #점차 넓어지는 것을 표현하기 위해 2*x 만큼 크게 만듬
    t.rt(90)
    t.fd(2*x+2)
    t.rt(90)
    t.fd(2*x+2)
    t.rt(90)
    t.fd(2*(2*x+2))
    t.rt(90)
    t.fd(2*x+2)
    t.rt(90)
    t.fd(2*x+2)
    t.rt(45)
    t.fd(1.4142135623730951*(2*x+2))    # 네모 칸 안에 x자를 그리기 위해
    t.lt(135)                           # 루트 2 의 값을 곱한 길이를 구함
    t.fd(2*x+2)
    t.lt(135)
    t.fd(1.4142135623730951*(2*x+2))
    t.rt(90)
    t.fd(1.4142135623730951*(2*x+2))
    t.lt(135)
    t.fd(2*x+2)
    t.lt(135)
    t.fd(1.4142135623730951*(2*x+2))
    t.lt(45)

t.lt(90)        # 상단부와 중단부를 나누기 위한 도형
t.begin_fill()
t.fd(25)
t.rt(90)
t.fd(8)
t.rt(90)
t.fd(50)
t.rt(90)
t.fd(8)
t.rt(90)
t.fd(25)
t.end_fill()
t.back(25)

t.rt(90)
t.fd(8)
t.lt(90)
t.fd(25)
t.rt(90)


t.rt(90)
t.fd(21)
t.lt(90)
t.fd(7)
t.lt(90)
t.fd(42)
t.lt(90)
t.fd(7)

for x in range(3):      #중단부의 칸을 6개로 나누기 위함
    t.lt(90)
    t.fd(7)
    t.lt(90)
    t.fd(7)
    t.rt(90)
    t.fd(7)
    t.rt(90)
    t.fd(7)
t.back(7)
t.rt(45)

for x in range(6):  # 6칸의 네모에 x자를 치기 위함
    t.fd(1.4142135623730951*7)
    t.lt(135)
    t.fd(7)
    t.lt(135)
    t.fd(1.4142135623730951*7)
    t.lt(90)
    
t.rt(135)   # 중단부의 사다리꼴을 만들기 위함
t.lt(10)
t.fd(90)
t.rt(100)
t.fd(17)
t.rt(80)
t.fd(90)
t.lt(80)
t.fd(8)
t.lt(80)
t.fd(90)
t.rt(80)
t.fd(17)
t.rt(100)
t.fd(90)

t.back(30)  #사다리꼴을 3등분함
t.rt(80)
t.fd(17)
t.rt(100)
t.fd(30)
t.rt(80)
t.fd(17)
t.rt(100)

t.back(30)
for x in range(3):  #중단부 왼쪽 사다리꼴 x자 채우기
    t.rt(27)        # 각도는 시도해보면서 가장 비슷하게 맞춰서 했습니다.
    t.fd(37)
    t.lt(27)
    t.back(30)
    t.lt(31)
    t.fd(32)
    t.rt(31)

t.back(2)
t.rt(80)
t.fd(42)
t.rt(80)
t.fd(90)

t.lt(180)

for x in range(3):  #중단부 오른쪽 사다리꼴 x자 채우기
    t.lt(27)
    t.fd(37)
    t.rt(27)
    t.back(30)
    t.rt(31)
    t.fd(32)
    t.lt(31)
    t.lt(80)
    t.fd(17)
    t.back(17)
    t.rt(80)

t.back(90)  #중단부와 하단부의 경계
t.lt(80)
t.fd(76)
t.lt(90)
t.fd(10)
t.lt(90)
t.fd(80)
t.lt(90)
t.fd(10)
t.lt(90)
t.fd(4)
t.back(4)

for x in range(2):  #경계 칸 나누기
    t.fd(16)
    t.lt(90)
    t.fd(10)
    t.rt(90)
    t.fd(16)
    t.rt(90)
    t.fd(10)
    t.lt(90)

t.lt(90)        #하단부의 윗 부분 만들기
t.fd(10)
t.rt(90)
t.fd(16)
t.fd(4)
t.lt(90)
t.fd(10)
t.lt(90)
t.fd(88)
t.lt(90)
t.fd(10)
t.lt(90)
t.fd(4)
t.back(4)

for x in range(5):  # 윗 부분 칸 나누기
    t.fd(8)
    t.lt(90)
    t.fd(10)
    t.rt(90)
    t.fd(8)
    t.rt(90)
    t.fd(10)
    t.lt(90)

t.fd(8)
t.lt(90)
t.fd(10)
t.rt(30)
t.fd(140)
t.lt(120)
t.fd(70)
t.lt(90)

for x in range(100):        #반원 그리기
    t.fd(1.36)
    t.rt(180/100)

t.lt(90)    #하단부 모양 채우기
t.fd(70)
t.lt(120)
t.fd(138)   #반원을 그릴 때 약간의 오류로 2가 차이납니다 ㅜㅜ
t.lt(60)
t.fd(88)

t.lt(60)
t.fd(140)
t.lt(120)
t.fd(32)
t.lt(60)
t.fd(140)
t.rt(60)
t.fd(24)
t.rt(60)
t.fd(138)
t.lt(60)
t.fd(16)
t.lt(120)
t.fd(138)
t.lt(60)
t.fd(56)
t.lt(60)
t.fd(140)

t.rt(60)
t.fd(16)
t.rt(120)
t.fd(120)
t.rt(60)
t.fd(108)
t.lt(120)
t.fd(10)
t.lt(60)
t.fd(98)
t.rt(120)
t.fd(10)
t.rt(150)   #사인60 = 0.866025
t.fd(20*0.866025)
t.lt(90)
t.fd(88)
t.lt(90)
t.fd(20*0.866025)

for x in range(5):  # 칸나누기
    t.lt(90)
    t.fd(8)
    t.lt(90)
    t.fd(10*0.866025)
    t.rt(90)
    t.fd(8)
    t.rt(90)
    t.fd(10*0.866025)

t.back(10*0.866025)
t.rt(90)
t.fd(80)
t.lt(90)

for x in range(5):  # 칸나누기 반복
    t.lt(90)
    t.fd(8)
    t.lt(90)
    t.fd(10*0.866025)
    t.rt(90)
    t.fd(8)
    t.rt(90)
    t.fd(10*0.866025)

t.rt(90)
t.back(8)

for x in range(11): # 칸 x자 채우기
    t.lt(43)
    t.fd(8/0.7314)
    t.lt(137)
    t.fd(8)
    t.lt(137)
    t.fd(8/0.7314)
    t.lt(43)

t.back(88)
t.rt(90)
t.fd(10*0.866025)
t.lt(90)

for x in range(11): # 칸 x자 채우기 반복
    t.lt(43)
    t.fd(8/0.7314)
    t.lt(137)
    t.fd(8)
    t.lt(137)
    t.fd(8/0.7314)
    t.lt(43)

t.fd(10)        # 하단부 오른쪽 칸나누기
t.rt(60)
t.fd(40)
t.rt(120)
t.fd(32)
t.lt(120)
t.fd(40)
t.lt(60)
t.fd(32)

t.lt(120)       # 하단부 왼쪽 칸 나누기
t.fd(80)
t.lt(60)
t.fd(108)
t.lt(60)
t.fd(40)
t.lt(120)
t.fd(32)
t.rt(120)
t.fd(40)
t.rt(60)
t.fd(32)

t.rt(120)
t.fd(80)
t.rt(60)

for x in range(3):      #하단부 왼쪽 칸 x자 치기
    t.rt(69.67)         # 계산과 많은 오류로 인한 값
    t.fd(35.7141)
    t.lt(129.67)
    t.fd(40)
    t.lt(120)
    t.lt(34.33)
    t.fd(62.482)
    t.lt(25.67)
    t.lt(120)

t.back(1)
t.lt(60)
t.fd(118)
t.rt(60)
t.fd(108)
t.rt(60)

for x in range(3):      #하단부 오른쪽 x자 치기
    t.rt(50.33)         # 계산과 많은 시도에 의한 값
    t.fd(35.7141)
    t.rt(129.67)
    t.fd(40)
    t.rt(120)
    t.rt(34.44)
    t.fd(62.482)
    t.rt(25.67)















    









