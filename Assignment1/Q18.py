def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    return sorted(str1) == sorted(str2)
string1 = input("Enter String1:")
string2 = input("Enter String2:")
if are_anagrams(string1, string2):
    print("TRUE")
else:
    print("FALSE")
