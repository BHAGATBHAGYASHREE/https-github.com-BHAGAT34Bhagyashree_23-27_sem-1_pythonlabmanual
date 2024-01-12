
def get_user_details(name, email, age, *args, **kwargs):
    print("User Details:")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Age: {age}")
    print("Additional args:", args)
    print("Additional kwargs:", kwargs)
user_name = input("Enter your name: ")
user_email = input("Enter your email: ")
user_age = int(input("Enter your age: "))
get_user_details(user_name, user_email, user_age, address="123 Main St", phone="555-1234")
