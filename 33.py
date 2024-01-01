def get_distinct_elements(input_list):
    return list(set(input_list))

user_input = input("Enter elements separated by spaces: ")
input_list = list(map(int, user_input.split()))

result_list = get_distinct_elements(input_list)
print(result_list)
