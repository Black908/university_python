"""first =int(input("첫번째 수 :"))
second = int(input("두번째 수 :"))
set_first = set()
set_second = set()
for i in range(1,first+1):
    frs = first % i
    if frs == 0:
        set_first.add(i)
print("첫번째 수의 약수는",set_first)
for j in range(1,second+1):
    sec = second % j
    if sec == 0:
        set_second.add(j)
print("두번째 수의 약수는",set_second)
print(first,"와 ",second,"의 공약수는")
print(set_first&set_second)

a = {"강감찬":"귀주대첩", "을지문덕":"살수대첩", "세종대왕":"집현전"}
a["서희"] = "강동6주"
print(a)

a["세종대왕"] = "한글"
print(a)

print("을지문덕" in a)
del a["을지문덕"]
print(a)
"""

f = open('loop.txt', 'a')
a = 5
for a in range(1, a + 1):
    data = "제%d의아해가무섭다고그리오." % a
    f.write(data)
    print(data)
f.close()
