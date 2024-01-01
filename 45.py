class Input:
    def getinput(self):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        return num1, num2


class Addition(Input):
    def addnumbers(self):
        num1, num2 = self.getinput()
        result = num1 + num2
        return result


def main():
    addition = Addition()
    result = addition.addnumbers()
    print(f"The sum of the two numbers is: {result}")


if __name__ == "__main__":
    main()
