def get_unique_elements(input_list):
    unique_elements = []
    for element in input_list:
        if element not in unique_elements:
            unique_elements.append(element)
    return unique_elements
original_list = [1, 2, 2, 3, 4, 4, 5, 6, 6]
result_list = get_unique_elements(original_list)
print("Original List:", original_list)
print("List with Distinct Elements:", result_list)