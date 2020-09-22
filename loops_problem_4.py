

# number guessing

number = []

for i in range(25,51):
    number.append(i)

print(number)




while True:
    print("Type q to quit")
    a = input("Guess a number:")
    if a == "q":
        break

    try:
        a = int(a)
    except ValueError:
        print("please type a number or q to quit.")
     
    if a in number:
        print("You guessed a correct number!")
    else:
        print("You guessed incorrectly!")
    
