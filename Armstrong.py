# Armstrong number is a number that is equal to the sum of its digits, each raised to a power.
# For example, 153 is an Armstrong number because 1^3 + 5^3 + 3^3 equals 153.

# print(len(str(num))) - Number of Digits

num = int(input("Enter a num : "))
n = len(str(num))
temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    sum = sum+(digit ** n)
    temp = temp//10

if sum == num:
    print(num, "is a Armstrong number")
else:
    print(num, "is not a Armstrong number")
