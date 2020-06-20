"""data_list = ["A", "b", 3, "4", "@"]
print(data_list)
data_tuple = ("A", "b", 3, "4", "@")
print(data_tuple)
data_set = {"A", "b", 3, "4", "@"}
print(data_set)

a_list =["사과", "귤", "딸기"]
b_list =["라면", "고기", "케이크"]
c_list = a_list+b_list
print(c_list)

a = [1, 2, 3, 4, 5,6,6,6,7]
print(a.count(6))
print(a.index(3))
print(a.remove(5))
print(a)    #Page218

stu = ["홍길동", "허난설현", "허균"]
print(stu.append("이황"))
print(stu.insert(2, str("허균")))
print(stu.count("허균"))
print(stu)

at = ["이황", "이이", "원효"]
print("현재학생은%s"%at)
a = input("전학 온 학생은 누구입니까?")
b=0
at.append(a)
print(at)
print("번호 재정렬....")
at.sort()

for i in at:
    b=b+1
    print(b, i)

print("튜플 조작기 ver 1")
print("튜플에 입력할 자료들을 차례로 입력하세요. 빈칸으로 구분합니다.")
a=input()
a=tuple(a.split(" "))

while True:
    print("작업 할 내용을 입력하세요")
    b=input("q = 끝내기, s = 슬라이싱, c= 세기, i = 존재 여부:")
    if b=='q':
        print("프로그램을 종료합니다.")
        break;
    elif b=='s':
        b1=int(input("From : "))
        b2=int(input("To : "))
        print(a[b1:b2])
    elif b=='c':
        c1 =input("찾은 자료 값은 :")
        print(a.count(c1),"번 있습니다")
    elif b=='i':
        i1=input("찾은 자료 값은 :")
        print(i1 in b)
"""
