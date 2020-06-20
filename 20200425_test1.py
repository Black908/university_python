"""i=2
while i<100:
    print(i)
    i=i+2

i=1
while i<100:
    i+=1
    if(i%2==0):
        print(i)

i=2
while i<33:
    print(i%4)
    i=i+1

a_m=1
a_m1=
a_m1=a_m+(2*a_m1)
print(a_m1)

a1=1
an1=0
an=1
while a1<101:
    an1=2*an
    print(an1)
    an=an1
    a1=a1+1

a1=1
an1=a1+2
while a1<100:
    print(an1)
    an1=an1+2
    a1=a1+1

name=""
while name!="q":
    name=input("당신의 이름을 입력하세요. 'q를 입력하면 종료합니다.:")
    print(name)

answer=54
input1=""
while input1 !="54":
    input1=input("숫자를 입력해주세요.")
    if(input1=="54"):
        print("정답입니다.")
    else :
        print("실패입니다.")
a=0; b=1
for i in range(20):
    print(a, end=" ")
    n=a+b
    a=b
    b=n

a= int(input("홀수는 1, 짝수는 2를 입력해주세요:"))
for i in range(a,101,2):
    print(i)

i=0
while i<6:
    i = i+1
    if i==3:
        continue
    print(i,"번째 반복입니다.")

print("최대공약수 구하기")
a=int(input("첫번째 숫자: "))
b=int(input("두번째 숫자: "))

if b>a:
    a,b = b,a

while (b!=0):
    a= a%b
    a,b = b,a
print("최대공약수는",a)

print("구구단을 외자")
for a in range(2,10):
    print(a,"단 시작=========")
    for b in range(1,10):
        print(a,"X",b,"=",a*b)
"""
