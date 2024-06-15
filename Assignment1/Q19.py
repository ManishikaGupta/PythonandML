import string
def remove_punctuation(input_str):
    translator = str.maketrans('', '', string.punctuation)
    return input_str.translate(translator)

input_string = input("Enter a String:")
clean_string = remove_punctuation(input_string)
print(clean_string)
