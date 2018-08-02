# 실습

lst = []
lst.append(21)
lst.append(42)
lst.append(23)
lst.append(14)
lst.append(5)
lst.append(66)

lst.sort()

print(lst)

Max_value = max(lst)
min_value = min(lst)

print("Max: %d" % Max_value)
print("min: %d" % min_value)

lst.remove(Max_value)
lst.remove(min_value)

print(lst)


