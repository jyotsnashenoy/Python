num = int(input("Enter the number of terms : "))
arr = []
n1 = 0
n2 = 1
count = 0

if num <= 0:
    print("Enter a positive integer.")
elif num == 1:
    print("Fibonacci sequence : ", n1)
else:
    print("Fibonacci sequence : ")
    while count < num:
        arr.append(n1)
        nth = n1+n2
        n1 = n2
        n2 = nth
        count = count+1
    print(arr)
