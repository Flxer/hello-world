'''
num1 = input("num1:")
num2 = input("num2:")

if num1 > num2:
    print("num1 larger :", num1)
elif num1 < num2:
    print("num2 larger :", num2)
elif num1 == num2:
    print("same value")
else:
    print("error")
'''
# input 함수로 반환되는 것은 문자열 이다.
# 정수를 다루고 싶으면 추가적으로 int()를 써 주어야 한다.

# while 문
'''
a = 0
while a <= 20:
    a = a + 1 # a가 0에서 1로 바뀌고
    if a % 2 == 1:
        continue
    print(a)
'''

# 실습
'''i = 0
while i <= 10:
    i = i + 1
    print("*", end = "")


x = 0
while x ** 3 <= 10000:
    x = x + 1

    if x ** 3 > 10000:  #if 를 안하고 while 밖에 print()를 해주는게 더 괜찮다. 22까지 살피고 나서 그 이후는 살필 필요 없으니 x 출력하고
        print(x)
'''




