num = int(input("Enter a num : "))

temp = num
reversed = 0

while temp > 0:
    rem = temp % 10
    reversed = (reversed*10)+rem
    temp = temp//10

if num == reversed:
    print("Palindrome")
else:
    print("Not a Palindrome")
