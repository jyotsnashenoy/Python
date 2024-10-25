word = str(input("Enter a word : "))

vowels = ['a', 'e', 'i', 'o', 'u']
count = 0

for char in word:
    if char not in vowels:
        count = count+1
print("Number of consonents :", count)
