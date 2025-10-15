# script.py
user_input = input("Enter a number: ")
if not user_input.strip():
    print("Error: Input cannot be empty!")
else:
    number = int(user_input)
    print("You entered:", number)