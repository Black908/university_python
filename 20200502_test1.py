"""
a = "String in Python"
for i in enumerate(a):
    print(i)
for i in enumerate(a):
    print(i[0])
for i in enumerate(a):
       print(i[1])
len(a)

name = input("이름을 입력하세요 : ")
cm = int(input("키(cm)를 입력하세요 : "))
kg = int(input("몸무게(kg)를 입력하세요 : "))
bmi = kg / cm / cm * 10000
if (bmi > 18.5, bmi < 22.9):
    print("정상")
elif (bmi>23, bmi<24.9):
    print("과체중")
elif (bmi>25, bmi<29.9):
    print("비만")
elif (bmi>30):
    print("고도비만")
print(name+"님의 키는 "+str(cm)+" cm이고 몸무게는 "+str(kg)+" kg 입니다.\nBMI 지수는 "+str(round(bmi,2))+" 입니다.입니다.")

a = " "
str(input("문장을 입력해주세요. 'q' 입력시 종료합니다.\n"))
while a != "q":
    a=input("")
    if a[-1] == ".":
        print("온점을 잘 입력하셨습니다.")
    else:
        print("온점을 입력하세요.")

a=""
print("문장을 입력해주세요. 'q' 입력시 종료합니다.")
while a!='q':
    a=str(input(""))
    print(a[0])
    for i in range(len(a)):
        if a[i] == " ":
            print (a[i+1])

a = "--"
b = ["A", "B", "C", "D"]
print(a.join(b))

a = "-"
b = ["홍길동", "2000", "19학번"]
print(a.join(b))

a="간장공장공장장"
print(a.count("장"))
"""

