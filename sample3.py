'''
print("Hi, Is it great?".replace("Hi,", "Cool"))
print("Hi Ii tititititizzi".split('i'))


b = 'We are R so R are us but r is not same with us.'
a = '*'
c = a.join(b)
print(c)


a = '1980M1120'
a.replace('1980M', 'M1980')


b = '11011011110110101011'

print(b.replace('1101','aaa'))

# replace 함수는 바꿔 나가면서 읽는 듯 하다. 바꾼 데이터를 다루고 읽어나가다가 또 바꿔주고.
# replace 를 두번이나 (한 줄에서) 쓸 수도 있다. 함수에서 각 위치가 무엇을 의미하는지를 정확히 알면 여러 함수를 섞어서 사용이 가능하다.

'''
# 실습1

a = input("input : ")
init = a[:1]
mid = a[1:-1]
end = a[-1:]

I = init.upper()
m = mid.lower()
E = end.upper()

print(I + m + E)

# 굳이 변수 지정을 하지 않았어도 됐는데..















