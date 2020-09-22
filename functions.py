

def f(x):
    return x + 1

z = f(4)

if z == 5:
    print("z is 5")
else:
    print("z is not 5")

    
# function without parameters


def f():
    return 1 + 1

result = f()
print(result)

def f(x, y, z):
    return x + y + z

result = f(1,2,3)
print(result)

# function withou return-statement returns NONE

def f():
    z = 1 + 1

result = f()
print(result)

# length of an object
a = len("Python")
print(a)

# input function

age = input("Enter your age:")
int_age = int(age)
if int_age < 21:
    print("You are young!")
else:
    print("Wow, you are old!")

#Reusing functions

def even_odd():
    n = input("type a number:")
    n = int(n)

    if n % 2 == 0:
        print("even")
    else:
        print("odd")

even_odd()

# global scope and local scope

def f():
    x = 1
    y = 2
    z = 3
    print(x)
    print(y)
    print(z)

f()







