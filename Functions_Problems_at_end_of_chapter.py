

# Problem 1

def square():
    try:
        a = input("Please enter a number:")
        a = int(a)
        b = a**2
        print(b)
    except ValueError:
        print("Invalid input.")
square()
# Problem 2

def stringh ():
    a = input("Please enter something:")
    a = str(a)
    return print(a)

stringh()

# Problem 3

def lot_para(a=10,b=20 ):
    try:
        x = input("Please enter an integer value for x:")
        x = int(x)
        y = input("Please enter an integer value for y:")
        y = int(y)
        z = input("Please enter an integer value for z:")
        z = int(z)
        result = x+y+z+a+b
        print(result)
    except ValueError:
        print("Invalid input.")

lot_para()
