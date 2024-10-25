arr = [1, 2, 3, 4, 5]
sum = 0
avg = 0
n = len(arr)

for i in range(n):
    sum = sum+arr[i]
avg = sum//n
print("Average :", avg)
