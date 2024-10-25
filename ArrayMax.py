arr = [1, -6, 4, 77, 2, 19, 56]
max = arr[0]

for i in range(1, len(arr)):
    if arr[i] > max:
        max = arr[i]
print(max)
