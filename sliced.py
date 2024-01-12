original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

sliced_list1 = original_list[2:5]
sliced_list2 = original_list[1:]
sliced_list3 = original_list[:6]
sliced_list4 = original_list[::2]
sliced_list5 = original_list[::-1]

print("Original List:", original_list)
print("Sliced List 1:", sliced_list1)
print("Sliced List 2:", sliced_list2)
print("Sliced List 3:", sliced_list3)
print("Sliced List 4:", sliced_list4)
print("Sliced List 5:", sliced_list5)

extension_list1 = original_list + [10, 11, 12]
extension_list2 = original_list.copy()
extension_list2.append([10, 11, 12])
extension_list3 = original_list.copy()
extension_list3.extend([10, 11, 12])

print("\nOriginal List:", original_list)
print("Extended List 1:", extension_list1)
print("Extended List 2:", extension_list2)
print("Extended List 3:", extension_list3)
