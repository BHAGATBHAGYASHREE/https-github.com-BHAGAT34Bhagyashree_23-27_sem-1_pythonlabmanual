user_input = input("Enter a letter: ")
if len(user_input) == 1 and user_input.isalpha():
    
    vowels = ['a', 'e', 'i', 'o', 'u']
    if user_input.lower() in vowels:
        print(f"{user_input} is a vowel.")
    else:
        print(f"{user_input} is not a vowel.")
else:
    print("Please enter a valid single letter.")
