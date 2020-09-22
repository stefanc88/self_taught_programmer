

# module cubed



while True:

    a = input("Type in a number:")
    
    try:
        a = int(a)
    except ValueError:
        print("Please type in an integer!")
        continue
    b = a**3

    print(b)
    
    
