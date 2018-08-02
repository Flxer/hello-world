# for 문
"""
for x in [1, 2, 3, 4, 5, 6]:
    print(x)

for x in range(10):
    print(x)

for num in range(1, 11):
    print(num ** 2)

for word in ("asfheuiw"):
    print(word * 2)
"""

for i in range(2, 10):
    for j in range(1, 10):
        print("%d * %d = %d" %(i, j, i * j)) # 배웠던 것처럼 .format()으로도 할 수 있다.
        if j == 7:
            print ("lucky!")

            # 제어문이 어떻게 걸리는가에(순서) 주의하자.


marks = list(input("Score:"))

number = 0
for mark in marks:
    number = number + 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." %number)
    else:
        print("%d번 학생은 불합격 입니다." % number)
