# Return the elements which sums to 12
# This is for sorted array

arr = [1, 2, 4, 8, 12, 14, 17]
target = 12

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == target:
            print(f"Numbers are {arr[i]} and {arr[j]}")
