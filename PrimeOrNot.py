num = int(input("Enter a num : "))
count = 0

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            count = count+1
if count == 0:
    print(num, "is a prime number.")
else:
    print(num, "is a not prime number.")


# Using Boolean
# num = int(input("Enter a num : "))
# is_prime = True

# if num > 1:
#     for i in range(2, num):
#         if (num % i) == 0:
#             is_prime = False
#             break
# else:
#     is_prime = False
# if is_prime:
#     print(num, " is a prime number.")
# else:
#     print(num, " is a not a prime number.")
