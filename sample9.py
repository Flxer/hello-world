'''
a0 = 1 == 18
a1 = 3 != 9
a2 = 3 < 8
a3 = []
'''

A_plus= 97
A_zero = 94
A_minus = 91
Fail = 50

score = 90

if score >= A_plus:
    print("You got A plus")
elif score >= A_zero:
    print("You got A zero")
elif score >= A_minus:
    print("You got A minus")

else:
    if score > Fail:
        print("You passed")
    else:
        print("You failed")







