class Employee:
    def get_details(self):
        self.name = input("enter the name")
        self.email = input("enter the email")
        self.age = int(input("enter age"))

    def print_details(self):
        print("Employee Details:")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")

emp = Employee()
emp.get_details()
emp.print_details()
