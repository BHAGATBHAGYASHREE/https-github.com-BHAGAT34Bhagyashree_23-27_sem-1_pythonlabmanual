n = int(input("enter the value : "))
cube_dict = {}

for num in range(1, n + 1, 2):
    cube_dict[num] = num ** 3

print(cube_dict)
