white_space_list = [" " * x for x in reversed(range(5))]
star_list = ["*" * (2 * y + 1) for y in range(5)]

for w, s in zip(white_space_list, star_list):
    print(w + s)

# enumerate
# element 들과 그에 해당하는 index가 튜플로 묶임
lst = ['a', 'b', 'c', 'd', 'e']

index = 0
for x in lst:
    print(x, index)
    index += 1

print("=" * 20)

for index, x in enumerate(lst):
    print(x, index)

# 실습

index = 0

sen = "adfjsfsdfkjdk"
lst = list(sen)
idx_lst = []
for index, x in enumerate(lst):
    if 'f' == x:
        idx_lst.append(index)

print(idx_lst)








