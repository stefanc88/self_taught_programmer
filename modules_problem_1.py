

# using a function from statistics


import statistics


numbers = []


for i in range(1,101):
    numbers.append(i)

print(numbers)


a = statistics.quantiles(numbers, n=25)

print(a)
