def count_occurrences(lst, element):
    count = 0
    for item in lst:
        if item == element:
            count += 1
    return count

lst = [1, 2, 3, 2, 4, 2, 5]
element = 2
occurrences = count_occurrences(lst, element)
print(f"The element {element} occurs {occurrences} times in the list.")