'''
dict={"a0":"cake", "a1":"fish", "a2":"stake"}

print(dict['a0'])

dict["adtinl_key"]=999
print(dict['adtinl_key'])

del dict['adtinl_key']

print('='*30)
print(dict)

print(dict.keys())
print(dict.values())
print(dict.items())

'''

me = {}
me["name"] = "yhm"
me["age"] = 20
me["age"] = 30

print(me.keys())
print(me.values())
print(me.items())

del me["age"]
print(me)


