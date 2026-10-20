"""Validate user registration input from the command line."""

import re


MIN_USERNAME_LENGTH = 5
MAX_USERNAME_LENGTH = 20
MIN_PASSWORD_LENGTH = 8
MAX_PASSWORD_LENGTH = 64
SPECIAL_CHARACTERS = "!@#$%^&*(),.?:{}|<>"
USERNAME_PATTERN = re.compile(r"^[A-Za-z0-9_]+$")
EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def check_rule(is_valid, error_message):
    """Raise a clear validation error when a rule is not met."""
    if not is_valid:
        raise ValueError(error_message)


def validate_username(username):
    """Validate username length and allowed characters."""
    check_rule(username, "Username cannot be empty.")
    check_rule(
        len(username) >= MIN_USERNAME_LENGTH,
        f"Username must be at least {MIN_USERNAME_LENGTH} characters long.",
    )
    check_rule(
        len(username) <= MAX_USERNAME_LENGTH,
        f"Username cannot be longer than {MAX_USERNAME_LENGTH} characters.",
    )
    check_rule(
        USERNAME_PATTERN.fullmatch(username),
        "Username can only contain letters, numbers, and underscores.",
    )
    return True


def validate_email(email):
    """Validate a simple email format."""
    check_rule(email, "Email cannot be empty.")
    check_rule(
        EMAIL_PATTERN.fullmatch(email),
        "Invalid email format. Example: johndoe@example.com",
    )
    return True


def validate_password(password):
    """Validate password length and complexity requirements."""
    password_rules = [
        (password, "Password cannot be empty."),
        (
            len(password) >= MIN_PASSWORD_LENGTH,
            f"Password must be at least {MIN_PASSWORD_LENGTH} characters long.",
        ),
        (
            len(password) <= MAX_PASSWORD_LENGTH,
            f"Password cannot be longer than {MAX_PASSWORD_LENGTH} characters.",
        ),
        (
            not any(character.isspace() for character in password),
            "Password cannot contain spaces.",
        ),
        (
            any(character.isupper() for character in password),
            "Password must contain at least one uppercase letter.",
        ),
        (
            any(character.islower() for character in password),
            "Password must contain at least one lowercase letter.",
        ),
        (
            any(character.isdigit() for character in password),
            "Password must contain at least one number.",
        ),
        (
            any(character in SPECIAL_CHARACTERS for character in password),
            "Password must contain at least one special character.",
        ),
    ]

    for is_valid, error_message in password_rules:
        check_rule(is_valid, error_message)

    return True


def show_instructions():
    """Print registration input requirements for the user."""
    print(
        """=== User Registration Validator ===

Please follow these input requirements:
- Username: 5 to 20 characters; letters, numbers, and underscores only.
- Email: Use a valid format, such as johndoe@example.com.
- Password: 8 to 64 characters with no spaces.
- Password must include uppercase, lowercase, number, and special character.
- Allowed special characters: !@#$%^&*(),.?:{}|<>
"""
    )


def main():
    """Collect user input and run all registration validation checks."""
    show_instructions()

    try:
        username = input("Enter username: ").strip()
        email = input("Enter email: ").strip()
        password = input("Enter password: ")

        validate_username(username)
        validate_email(email)
        validate_password(password)

        print("\nRegistration successful!")
    except ValueError as error:
        print(f"\nRegistration failed: {error}")


if __name__ == "__main__":
    main()
