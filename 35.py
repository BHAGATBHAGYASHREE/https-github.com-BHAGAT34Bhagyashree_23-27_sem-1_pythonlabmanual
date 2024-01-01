def count_upper_lower(string_test):
    upper_count = 0
    lower_count = 0

    for char in string_test:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    return upper_count, lower_count

string_test = 'Today is My Best Day'
result = count_upper_lower(string_test)
print(result)
