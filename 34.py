num = int(input("enter the number : "))
sum_divisors = 0

for i in range(1, num):
    if num % i == 0:
        sum_divisors += i

if sum_divisors == num:
    print("Perfect number")
else:
    print("Not a perfect number")
