def factorial(number):
    fact = 1
    if number < 0:
        print("Factorial is not defined for negative numbers.")
    elif number == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1, number + 1):
            fact*= i

        print(f"The factorial of {number} is {fact}")

user= int(input("Enter a positive integer to calculate its factorial: "))
factorial(user)