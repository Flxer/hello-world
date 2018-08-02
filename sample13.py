# 각각의 숫자의 제곱을 리스트에 넣기

# 빈 리스트를 만들고 range 를 (1,11)로 두고 for 문으로 탐색해 나가면 되지 않을까?
# 이를 리스트 변수에서 말을 해주어도 된다.
lst_1 = []
for num in range(1, 11):
    lst_1.append(num ** 2)

lst_2 = [x ** 2 for x in range(1, 11)]

print(lst_1)
print(lst_2)

# 리스트 내에 함수를 넣어주면 편리하다

# zip
# zip 안의 성분을 순서에 맞게 튜플로 묶어 준다.

lst_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst_2 = ['a', 'b', 'c']

for x in zip(lst_1, lst_2):  # 물론 zip 안에 튜플이 들어와도 된다.
    print(x)

for x, y in zip(lst_1, lst_2):
    print(x)
    print(y)

# 이 땐, x와 y에는 튜플의 성분이 각각(숫자, 문자열) 들어간다.





