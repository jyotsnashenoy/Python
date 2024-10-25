arr = [1, 6, 4, 77, 2, 9]
even = 0
odd = 0

for i in range(len(arr)):
    if arr[i] % 2 == 0:
        even = even+arr[i]
    else:
        odd = odd+arr[i]
print(f"Sum of Even Elements : ", even)
print(f"Sum of Odd Elements : ", odd)
