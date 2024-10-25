word = str(input("Enter a word : "))
l = str(input("Enter a letter : "))

count = 0
for letter in word:
    if letter == l:
        count = count+1
print("Number of occurances :", count)
