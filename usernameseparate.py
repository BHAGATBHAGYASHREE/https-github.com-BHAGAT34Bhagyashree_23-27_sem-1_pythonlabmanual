email = input("enter the full email : ")
parts = email.split('@')

if len(parts) == 2:
    username, domain = parts
    user_domain_tuple = (username, domain)
    print(user_domain_tuple)
else:
    print("Invalid email address")
