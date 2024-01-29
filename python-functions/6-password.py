def validate_password(password):
    # Check length
    if len(password) < 8:
        return False

    # Check for uppercase, lowercase, and digit
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)

    if not (has_uppercase and has_lowercase and has_digit):
        return False

    # Check for spaces
    if ' ' in password:
        return False

    # If all checks pass, the password is valid
    return True


