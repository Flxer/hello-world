# append
a = [1, 2, 3, 4]
a.append(5)
print(a)

# sort

a = [1, 4, 5, 2, 6, 8, 2, 9, 4]
a.sort(reverse=True)
print(a)

# reverse
a.reverse()
print(a)

# index
print(a.index(4))

# insert
a = [1, 4, 5, 2, 6, 8, 2, 9, 4]
a.insert(2,"4")
print(a)

a = [1, 4, 5, 2, 6, 8, 2, 9, 4]
b = a[:2]
c = a[2:]
print(b + [4, '4'] + c)

a.remove(2)
print(a)

# pop
lst = [1, 2, 3, 4, 5, 6, 7]
lst.pop()
print(lst.pop)

# extend 와 +의 차이
# +는 원본이 그대로 보존되나, extend 는 원본이 보존되지 않는다.
# 주의, append 는 요소로써 추가하는 것이다.


lst = [3, 4, 'C', 'd']
Pop = lst.pop(2)

print(Pop)


# list 함수 안에서 index 를 받느냐, element 자체를 받느냐는 구분하지 않아도 된다.
# element 를 받는 함수와 index 함수와 혼용해서 쓴다면 index 를 받는 것 처럼 쓸 수 있기 때문이다.



