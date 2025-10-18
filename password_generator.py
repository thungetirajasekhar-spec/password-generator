import random
import string

def generate_password(length):
    # Define character sets
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_chars = letters + digits + symbols

    # Generate random password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

# Ask user for password length
length = int(input("Enter desired password length: "))

# Generate and display password
password = generate_password(length)
print("\n🔑 Your Secure Password is:", password)
