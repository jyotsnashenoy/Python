# SecondLargest.py

arr = [1, 4, 16, 9, 17, 21, 3]
largest = arr[0]
Second_largest = arr[0]

for i in range(len(arr)):
    if arr[i] > largest:
        largest = arr[i]

for i in range(len(arr)):
    if arr[i] > Second_largest and arr[i] != largest:
        Second_largest = arr[i]
print("Second Largest :", Second_largest)
