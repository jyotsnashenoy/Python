# CommomElements

list1 = [1, 4, 16, 9, 7, 21, 3]
list2 = [6, 3, 7, 11, 101, 23, 9]
result = []

for i in range(0, len(list1)):
    for j in range(0, len(list2)):
        if list1[i] == list2[j]:
            result.append(list2[j])
print(f"CommomElements are", result)
