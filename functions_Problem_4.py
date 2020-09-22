
# two functions

def f_1():
    try:
        x = input("Please enter an integer value:")
        x = int(x)
        a = x/2
        a = int(a)
        print(a)
        return a
    except ValueError:
        print("Invalid input.")

def f_2(y):
    return y * 4
    

a = f_1()
b = f_2(a)

print(b)
