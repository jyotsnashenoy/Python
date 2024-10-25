num = int(input("Enter a number : "))
factors = []

if num > 0:
    for i in range(1, num+1):
        if (num % i) == 0:
            factors.append(i)
    print("Factors :", factors)
    print("Number of Factors :", len(factors))
else:
    print("Please enter a positive integer greater than 0.")
