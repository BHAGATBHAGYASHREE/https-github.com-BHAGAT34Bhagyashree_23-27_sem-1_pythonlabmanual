'''number =str(input("ENTER THE NUMBER"))
digi=len(str(number))
if number=='''
num = int(input("Enter a number: "))

num_str = str(num)
sum_of_powers = sum(int(digit) ** len(num_str) for digit in num_str)
if sum_of_powers == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
