import random
import string

def generate_password(length=18, include_upper=True, include_lower=True, include_numbers=True, include_symbols=True):
    """Generates a random password of the given length.

    Args:
        length: The length of the password to generate.
        include_upper: Whether to include uppercase letters in the password.
        include_lower: Whether to include lowercase letters in the password.
        include_numbers: Whether to include numbers in the password.
        include_symbols: Whether to include symbols in the password.

    Returns:
        A random password of the given length.
    """
    characters = []
    if include_upper:
        characters.extend(string.ascii_uppercase)
    if include_lower:
        characters.extend(string.ascii_lowercase)
    if include_numbers:
        characters.extend(string.digits)
    if include_symbols:
        characters.extend(string.punctuation)

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_complex_password(length=16, include_upper=True, include_lower=True, include_numbers=True, include_symbols=True, include_special_symbols=True):
    """Generates a more complex random password of the given length.

    Args:
        length: The length of the password to generate.
        include_upper: Whether to include uppercase letters in the password.
        include_lower: Whether to include lowercase letters in the password.
        include_numbers: Whether to include numbers in the password.
        include_symbols: Whether to include symbols in the password.
        include_special_symbols: Whether to include special symbols in the password.

    Returns:
        A more complex random password of the given length.
    """
    return generate_password(length, include_upper, include_lower, include_numbers, include_symbols and include_special_symbols)

if __name__ == "__main__":
    # Get user input for password length
    length = int(input("Enter the desired password length: "))

    # Generate a random password.
    password = generate_password(length)

    # Generate a more complex random password.
    complex_password = generate_complex_password(length)

    # Print the passwords to the console.
    print("Random password:", password)
    print("More complex random password:", complex_password)
