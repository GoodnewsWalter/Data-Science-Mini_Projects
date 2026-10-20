SPECIAL_CHARACTERS = "!@#$%^&*(),.?\":{}|<>"


def check_rule(is_valid, error_message):
    if not is_valid:
        raise ValueError(error_message)


def validate_username(username):
    check_rule(
        len(username) >= 5,
        "Username must be at least 5 characters long.",
    )
    return True


def validate_email(email):
    check_rule(
        "@" in email and "." in email,
        "Invalid email format. Example: johndoe@example.com",
    )
    return True


def validate_password(password):
    password_rules = [
        (
            len(password) >= 8,
            "Password must be at least 8 characters long.",
        ),
        (
            any(char.isupper() for char in password),
            "Password must contain at least one uppercase letter.",
        ),
        (
            any(char.islower() for char in password),
            "Password must contain at least one lowercase letter.",
        ),
        (
            any(char.isdigit() for char in password),
            "Password must contain at least one number.",
        ),
        (
            any(char in SPECIAL_CHARACTERS for char in password),
            "Password must contain at least one special character.",
        ),
    ]

    for is_valid, error_message in password_rules:
        check_rule(is_valid, error_message)

    return True


def show_instructions():
    print(
        """=== User Registration System ===

Please follow these requirements:
- Username: At least 5 characters long
- Email: Must contain '@' and '.'
- Password:
  * At least 8 characters long
  * At least one uppercase and lowercase letter
  * At least one number and special character
"""
    )


show_instructions()

try:
    username = input("Enter username: ").strip()
    email = input("Enter email: ").strip()
    password = input("Enter password: ").strip()

    validate_username(username)
    validate_email(email)
    validate_password(password)

    print("\nRegistration successful!")

except ValueError as error:
    print(f"\nRegistration failed: {error}")

except Exception as error:
    print(f"\nAn unexpected error occurred: {error}")
