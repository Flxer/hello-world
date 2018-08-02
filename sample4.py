'''
a = [1, '2', 2, 3, '4', 'hi']
print(a[2])
print(a[2]+a[3])

print(a + [3,4,5])
print(a * 2)
print(a + [1, 2]*2)

b = [[[[3], 4], [2]],'p']
print(b[0][0])

c = [3]
print(c * 20)
'''
a = [10, 20, 30, 50, 80]
a[0:3] = [1, 2, 3, 5]
print(a)

del a[1]
print(a)