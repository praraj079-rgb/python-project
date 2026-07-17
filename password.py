import random
import string

print("===== PASSWORD GENERATOR =====")

length = int(input("Enter the password length: "))

print("\nChoose the character types:")
uppercase = input("Include Uppercase Letters? (y/n): ").lower()
lowercase = input("Include Lowercase Letters? (y/n): ").lower()
numbers = input("Include Numbers? (y/n): ").lower()
symbols = input("Include Symbols? (y/n): ").lower()

characters = ""

if uppercase == "y":
    characters += string.ascii_uppercase

if lowercase == "y":
    characters += string.ascii_lowercase

if numbers == "y":
    characters += string.digits

if symbols == "y":
    characters += string.punctuation

if characters == "":
    print("\nError: Please select at least one character type.")
else:
    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("\nGenerated Password:", password)