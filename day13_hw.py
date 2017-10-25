import turtle as t  #turtle 함수를 불러온다.
import random       #랜덤함수를 불러온다.    

t.speed(0)          #스피드를 최고속도로 올린다.


def square(n):  #길이가 n인 정사각형을 만드는 함수
    t.setheading(270)    # 거북이가 밑을 보도록 한다
    for x in range(4): 
        t.fd(n)
        t.lt(90)

def rtwall(i):  # 오른쪽 벽을 맞았을 때 반응 함수
    if t.xcor() >= i:   # x좌표가 경계선 i를 넘었을 때 
        if y <= b:      # 위에서 아래로 내려가는 방향이었을 때
            t.rt(2*(ang-270))   #방향을 꺾는다.
            
        else:           # 아래에서 위로 올라가는 방향이었을 때
            t.lt(2*(90-ang))    


def ltwall(i):  # 왼쪽 벽을 맞았을 때 반응 함수
    if t.xcor() <= i:   # x좌표가 경계선i를 넘었을 때
        if y <= b:      # 위에서 아래로
            t.lt(2*(270-ang))
        else:           # 아래에서 위로
            t.rt(2*(ang-90))


def upwall(i):  #위쪽 벽을 맞았을 때 반응 함수
    if t.ycor() >= i:   # y좌표가 경계선 i를 넘었을 때
        if x <= a:      # 오른쪽에서 왼쪽으로 가는 방향이었을 때
            t.lt(2*(180-ang))
        else:           # 왼쪽에서 오른쪽으로 가는 방향이었을 때
            t.rt(2*ang)

def downwall(i):    # 아래쪽 벽을 맞았을 때 반응 함수
    if t.ycor() <= i:   # y좌표가 경계선 i를 넘었을 때
        if x <= a:      # 오른쪽에서 왼쪽
            t.rt(2*(ang-180))
        else:           # 왼쪽에서 오른쪽
            t.lt(2*(360-ang))

def rectangle (l,h):    #가로가 l 세로가 h인 직사각형을 만드는 함수
    t.setheading(270)
    for x in range(2):
        t.fd(h)
        t.lt(90)
        t.fd(l)
        t.lt(90)


t.shape("turtle")   #커서의 모양을 거북이 모양으로 불러온다.
t.up()  # 팬을 든다
t.goto(-381.00,321.00)  #작은 창 왼쪽 맨 위 꼭지점 좌표
t.down()    # 팬을 내린다


t.pensize(2)    #펜사이즈를 3으로 정한다.
square(500) #길이가 500인 정사각형을 만든다.        

    # 사각형의 왼쪽 위 좌표는 (-381,321)
    # 사각형의 왼쪽 밑 좌표는 (-381,-179)
    # 사각형의 오른쪽 밑 좌표는 (119,-179)
    # 사각형의 오른쪽 위 좌표는 (119,321)

t.up()  # 펜을 든다.

_x = random.randint(-381, 99)   # 한 변의 길이가 20인 정사각형을 만들기 위해
                                # x좌표에서 20을 뺀 값을 넣는다.
_y = random.randint(-159, 321)  # 위와 동일한 이유로 20을 더한 값을 넣는다.

while True: #거북이가 시작할 때 장애물 안에 있음을 방지하기 위함
    if _x >=-151 and _x < -131 and _y <= 91 and _y >= 71:
        _x = random.randint(-381, 99)
        _y = random.randint(-159, 321)
    else:
        break
    
t.goto(_x, _y)

t.down()    #그림을 그리기 시작한다.



square(20)  #길이가 20인 정사각형을 장애물로 만든다.


t.up()

_x2 = random.randint(-381, 79)# 한 변의 길이가 40인 정사각형을 만들기 위해
                                # x좌표에서 40을 뺀 값을 넣는다.
_y2 = random.randint(-139, 321) # 위와 동일한 이유로 40을 더한  값을 넣는다.

while True: #거북이가 시작할 때 장애물 안에 있음을 방지하기 위함
    if _x2 >= -171 and _x2 < -131 and _y2 <= 111 and _y2 >= 71:
        _x2 = random.randint(-381, 79)
        _y2 = random.randint(-139, 321)
    else:
        break
    
t.goto(_x2, _y2)

t.down()

square(40)  # 길이가 40인 정사각형을 장애물로 만든다.

t.up()

_x3 = random.randint(-381, 49)  # 한 변의 길이가 70인 정사각형을 만들기 위해
                                # x좌표에서 70을 뺀 값을 넣는다.
_y3 = random.randint(-109, 321) # 위와 동일한 이유로 70을 더한 값을 넣는다.

while True: #거북이가 시작할 때 장애물 안에 있음을 방지하기 위함
    if _x3 >=-201 and _x3 < -131 and _y3 <= 141 and _y3 >= 71:
        _x3 = random.randint(-381, 49)
        _y3 = random.randint(-109, 321)
    else:
        break



t.goto(_x3,_y3)

t.down()




square(70)  # 길이가 70인 정사각형을 장애물로 만든다.

t.up()


_x4 = random.randint(-381, 69)   # 가로의 길이가 50인 직사각형을 만들기 위해
                                # x좌표에서 50을 뺀 값을 넣는다.
_y4 = random.randint(-159, 321)  # 위와 동일한 이유로 20을 더한 값을 넣는다.

while True: #거북이가 시작할 때 장애물 안에 있음을 방지하기 위함
    if _x4 >=-181 and _x4 < -131 and _y4 <= 91 and _y4 >= 71:
        _x4 = random.randint(-381, 69)
        _y4 = random.randint(-159, 321)
    else:
        break

t.goto(_x4,_y4)

t.down()


rectangle(50,20)    #가로가 50 높이가 20인 직사각형을 랜덤으로 만든다.

    
t.up()  # 펜을 든다.

t.goto(-131,71) #(-137,71)좌표로 이동한다.
n = random.randint(1,360)   # n에 1~360사이의 랜덤한 숫자를 부여한다.
t.setheading(n) # 거북이의 방향을 360도 안으로 랜덤하게 돌린다.
t.down()    # 그리기 시작한다.
t.pensize(1)    # 펜사이즈를 1로 한다.


x=0     #변수를 정의한다.
y=0
ang=0



while True:
    a = t.xcor() # a변수에 x좌표를 대입한다.
    b = t.ycor() # b변수에 y좌표를 대입한다.
    
    # 테두리 경계의 범위를 인식시킨다. 여기서는 바깥쪽 범위라 or를 씀
    if t.xcor() >= 119 or t.xcor() <=-381 or t.ycor() <= -179 or t.ycor() >=321:
        x = t.xcor()    # x에 x좌표를 대입시킨다.
        y = t.ycor()    # y에 y좌표를 대입시킨다.
        ang = t.heading()   # ang에 각도를 대입시킨다.
        
        rtwall(119) # i가 119일 때 오른쪽 벽
            
        
        downwall(-179)  #i가 -179일 때 아래쪽 벽
            
        
        upwall(321) # i가 321일 때 위쪽 벽    
            
        
        ltwall(-381)    # i가 -381일 때 왼쪽 벽
        


    # 장애물 정사각형 1
    # 정사각형의 범위를 인식시킨다. 여기서는 안쪽 범위라 and를 씀
    if t.xcor() >= (_x) and t.xcor() <= (_x+20) and t.ycor() <= (_y) and t.ycor() >= (_y-20):   
        x = t.xcor()
        y = t.ycor()
        ang = t.heading()

        if x <= _x+1 and y <= _y-1 and y >= (_y-20+1):  # 1씩움직이고 검사를
            # 하기 때문에 최대 1씩 검사에 허용 범위를 주어 방향을 꺽게 만듬
            if y <= b:      # 위에서 아래로 내려가는 방향이었을 때
                t.rt(2*(ang-270))   #방향을 꺾는다.
            
            else:           # 아래에서 위로 올라가는 방향이었을 때
                t.lt(2*(90-ang))            

        if x >= (_x+20-1) and y <= _y-1 and y>= (_y-20+1):
            if y <= b:      # 위에서 아래로
                t.lt(2*(270-ang))
            else:           # 아래에서 위로
                t.rt(2*(ang-90))

        if y >= _y-1 and x >= _x+1 and x <= (_x +20-1 ):
            if x <= a:      # 오른쪽에서 왼쪽
                t.rt(2*(ang-180))
            else:           # 왼쪽에서 오른쪽
                t.lt(2*(360-ang))

        if y <= (_y-20+1) and x >= _x+1 and x <= (_x + 20-1):
             if x <= a:      # 오른쪽에서 왼쪽으로 가는 방향이었을 때
                t.lt(2*(180-ang))
             else:           # 왼쪽에서 오른쪽으로 가는 방향이었을 때
                t.rt(2*ang)
            

    #장애물 정사각형 2
                
    if t.xcor() >= (_x2) and t.xcor() <= (_x2+40) and t.ycor() <= (_y2) and t.ycor() >= (_y2-40):   
        x = t.xcor()
        y = t.ycor()
        ang = t.heading()

        if x <= _x2+1 and y <= _y2-1 and y >= (_y2-40+1):
            if y <= b:      # 위에서 아래로 내려가는 방향이었을 때
                t.rt(2*(ang-270))   #방향을 꺾는다.
            
            else:           # 아래에서 위로 올라가는 방향이었을 때
                t.lt(2*(90-ang))            

        if x >= (_x2+40-1) and y <= _y2-1 and y>= (_y2-40+1):
            if y <= b:      # 위에서 아래로
                t.lt(2*(270-ang))
            else:           # 아래에서 위로
                t.rt(2*(ang-90))

        if y >= _y2-1 and x >= _x2+1 and x <= (_x2 +40-1 ):
            if x <= a:      # 오른쪽에서 왼쪽
                t.rt(2*(ang-180))
            else:           # 왼쪽에서 오른쪽
                t.lt(2*(360-ang))

        if y <= (_y2-40+1) and x >= _x2+1 and x <= (_x2 + 40-1):
             if x <= a:      # 오른쪽에서 왼쪽으로 가는 방향이었을 때
                t.lt(2*(180-ang))
             else:           # 왼쪽에서 오른쪽으로 가는 방향이었을 때
                t.rt(2*ang)


    # 장애물 정사각형 3
    if t.xcor() >= (_x3) and t.xcor() <= (_x3+70) and t.ycor() <= (_y3) and t.ycor() >= (_y3-70):   
        x = t.xcor()
        y = t.ycor()
        ang = t.heading()

        if x <= _x3+1 and y <= _y3-1 and y >= (_y3-70+1):
            if y <= b:      # 위에서 아래로 내려가는 방향이었을 때
                t.rt(2*(ang-270))   #방향을 꺾는다.
            
            else:           # 아래에서 위로 올라가는 방향이었을 때
                t.lt(2*(90-ang))            

        if x >= (_x3+70-1) and y <= _y3-1 and y>= (_y3-70+1):
            if y <= b:      # 위에서 아래로
                t.lt(2*(270-ang))
            else:           # 아래에서 위로
                t.rt(2*(ang-90))

        if y >= _y3-1 and x >= _x3+1 and x <= (_x3 +70-1 ):
            if x <= a:      # 오른쪽에서 왼쪽
                t.rt(2*(ang-180))
            else:           # 왼쪽에서 오른쪽
                t.lt(2*(360-ang))

        if y <= (_y3-70+1) and x >= _x3+1 and x <= (_x3 + 70-1):
             if x <= a:      # 오른쪽에서 왼쪽으로 가는 방향이었을 때
                t.lt(2*(180-ang))
             else:           # 왼쪽에서 오른쪽으로 가는 방향이었을 때
                t.rt(2*ang)

    # 장애물 직사각형 1
    if t.xcor() >= (_x4) and t.xcor() <= (_x4+50) and t.ycor() <= (_y4) and t.ycor() >= (_y4-20):   
        x = t.xcor()
        y = t.ycor()
        ang = t.heading()

        if x <= _x4+1 and y <= _y4-1 and y >= (_y4-20+1):
            if y <= b:      # 위에서 아래로 내려가는 방향이었을 때
                t.rt(2*(ang-270))   #방향을 꺾는다.
            
            else:           # 아래에서 위로 올라가는 방향이었을 때
                t.lt(2*(90-ang))            

        if x >= (_x4+50-1) and y <= _y4-1 and y>= (_y4-20+1):
            if y <= b:      # 위에서 아래로
                t.lt(2*(270-ang))
            else:           # 아래에서 위로
                t.rt(2*(ang-90))

        if y >= _y4-1 and x >= _x4+1 and x <= (_x4 +50-1 ):
            if x <= a:      # 오른쪽에서 왼쪽
                t.rt(2*(ang-180))
            else:           # 왼쪽에서 오른쪽
                t.lt(2*(360-ang))

        if y <= (_y4-20+1) and x >= _x4+1 and x <= (_x4 + 50-1):
             if x <= a:      # 오른쪽에서 왼쪽으로 가는 방향이었을 때
                t.lt(2*(180-ang))
             else:           # 왼쪽에서 오른쪽으로 가는 방향이었을 때
                t.rt(2*ang)


    t.fd(1) #1픽셀씩 진행하면서 검사를 진행함
    


