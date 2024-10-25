# An anagram is a word or phrase formed by rearranging the letters of another word or phrase,
# typically using all the original letters exactly once.
# For example, the words "listen" and "silent" are anagrams because you can
# rearrange the letters of "listen" to form "silent."

def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Sort the characters of both strings and compare
    return sorted(str1) == sorted(str2)


string1 = input("Enter String 1 : ")
string2 = input("Enter String 2 : ")

if are_anagrams(string1, string2):
    print(f'"{string1}" and "{string2}" are anagrams.')
else:
    print(f'"{string1}" and "{string2}" are not anagrams.')
