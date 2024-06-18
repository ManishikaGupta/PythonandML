def check_string():
    string = input("Enter a string: ")
    prefix = input("Enter a prefix: ")
    suffix = input("Enter a suffix: ")

    if string.startswith(prefix):
        print(f"The string '{string}' starts with the prefix '{prefix}'.")
    else:
        print(f"The string '{string}' does not start with the prefix '{prefix}'.")

    if string.endswith(suffix):
        print(f"The string '{string}' ends with the suffix '{suffix}'.")
    else:
        print(f"The string '{string}' does not end with the suffix '{suffix}'.")

check_string()