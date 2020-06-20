"""f = open("/Users/user/PycharmProjects/gtec/score.txt", 'r')
score = f.readlines()
print(score)
score = list(map(int, score))
score_sum = 0

for i in score:
    score_sum = score_sum+i
score_sum_avg = score_sum / len(score)

print("전체 합은 %d입니다."%score_sum)
print("전체 평균은 %d입니다."%score_sum_avg)

import turtle
a = turtle
i = 0

while i <3:
    a.forward(100)
    a.left(120)
    i = i+1

leng = int(input("사각형 길이를 입력해주세요."))
while leng%2 != 0:
    print("짝수를 입력해주세요")
    leng = int(input("사각형 길이를 입력해주세요."))

step = int(input("Step Size 를 입력해주세요."))
while step%2 != 0:
    print("짝수를 입력해주세요")
    step = int(input("Step Size 를 입력해주세요."))

import turtle
a = turtle
i = 0
j = 0
japyo = 0+step

while i <3:
    a.goto(0,0)
    a.pendown()
    for j in range(4):
        a.forward(leng)
        a.left(90)
    a.penup()
    i = i+1

a.exitonclick()
"""

import turtle
i = 0
j = 0
while i <4:
    turtle.forward(100)
    turtle.left(90)
    i = i+1
turtle.penup()
turtle.goto(10,10)
turtle.pendown()

while j<4:
    turtle.forward(80)
    turtle.left(90)
    j = j + 1

turtle.exitonclick()