import hashlib

# Create a function to hash the password
def hash_password(password):
    salt = b'somerandomstring'  # Generate a random salt value
    # Combine the password and salt, and hash them using SHA256
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return hashed_password.hex()

# Get the user's password
password = input("Enter your password: ")

# Hash the password and store it in a file
with open('password.txt', 'w') as f:
    f.write(hash_password(password))
