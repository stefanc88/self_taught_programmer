

lst = "Where now? Who now? When now?".split("?")
x = "?"
a = lst[0]
b = lst[1]
c = lst[2]

a_ = a+x
b_ = b+x
c_ = c+x

a_ = a_.strip()
b_ = b_.strip()
c_ = c_.strip()

lst = [a_ , b_ , c_ ]
print(lst)

