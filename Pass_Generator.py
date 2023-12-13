import random
import string

def generate_password(length=10):
    if length < 10:
        raise ValueError("Password length must be at least 10 characters")

    # Ensure at least 3 uppercase letters
    uppercase_letters = ''.join(random.choice(string.ascii_uppercase) for _ in range(3))

    # Ensure at least 3 lowercase letters
    lowercase_letters = ''.join(random.choice(string.ascii_lowercase) for _ in range(3))

    # Ensure at least 2 digits
    digits = ''.join(random.choice(string.digits) for _ in range(2))

    # Ensure at least 2 special characters
    special_characters = ''.join(random.choice(string.punctuation) for _ in range(2))

    # Combine all parts and shuffle them
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters
    shuffled_password = ''.join(random.sample(all_characters, length))

    return shuffled_password

# Example usage:
password = generate_password()
print("Your Password : ",password)
