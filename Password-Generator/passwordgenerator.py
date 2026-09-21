import string
import random

print("Welcome to the Password Generator!")

while True:
    try:
        input_length = int(input("What is your desired password length? (must be at least 8 characters): "))
        if input_length < 8:
            print("Invalid input. Please enter a number greater than or equal to 8.")
        else:
            break
    except ValueError:
        print("Please enter a valid number.")

include_lower = input("Include lowercase letters? (y/n): ").lower() == "y"
include_upper = input("Include uppercase letters? (y/n): ").lower() == "y"
include_digits = input("Include numbers? (y/n): ").lower() == "y"
include_symbols = input("Include symbols? (y/n): ").lower() == "y"


pool = ""
def build_pool():
    global pool
    if include_lower:
        pool += string.ascii_lowercase
    if include_upper:
        pool += string.ascii_uppercase
    if include_digits:
        pool += string.digits
    if include_symbols:
        pool += string.punctuation
    if pool == "":
        print("You must select at least one character type!")


length=int(input_length)
build_pool()
""" random.choice(): returns a list of randomly selected elements from the pool, with k specifying the number of elements to select. 
    "".join(...): takes the list of characters and turns them into one string, with "" (empty string) between each character, meaning no spaces between them. 
"""
password = "".join(random.choices(pool, k=input_length))
print(f"Your generated password is: {password}")
