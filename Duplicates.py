arr = [1, 9, 3, 17, 4, 16, 9, 7, 21, 3]
result = []
duplicates = []

for i in range(len(arr)):
    if arr[i] not in result:
        result.append(arr[i])
    else:
        duplicates.append(arr[i])


print("Result :", result)
print("Duplicates :", duplicates)
