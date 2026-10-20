# Mini-Project: User Registration Validator

## Objective
In this project, you will create a robust user registration tool directly inside your Jupyter Notebook. 
You will define custom functions to validate a user's username, email, and password. 
Most importantly, you will use `try/except` blocks and the `raise` keyword to handle invalid inputs gracefully without crashing your notebook kernel.

## Prerequisites
Before you begin, ensure you understand:
* How to define and call functions.
* How to use basic string methods (like `in` or `len()`).
* How to manually trigger an error using `raise ValueError("message")`.
* How to catch errors using a `try/except` block.
* How to execute code cells in a Jupyter environment.

## Step-by-Step Instructions

### Step 1: Set Up Your Notebook
1. In your workspace, create a new file named `registration.ipynb`.
2. All your code for this project will go inside the code cells of this file.

### Step 2: Create the Validation Functions
You will need to create three separate functions. Each function should check a specific rule and `raise` a `ValueError` if the rule is broken.

1. **`validate_username(username)`**:
   * Check if the length of the username is less than 5 characters.
   * If it is, `raise` a `ValueError` with the message: `"Username must be at least 5 characters long."`
   * Otherwise, return `True`.

2. **`validate_email(email)`**:
   * Check if the string `"@"` is NOT in the email, OR if `"."` is NOT in the email.
   * If either is missing, `raise` a `ValueError` with the message: `"Invalid email format. Must contain '@' and '.'"`
   * Otherwise, return `True`.

3. **`validate_password(password)`**:
   * Check if the password length is less than 8 characters.
   * If it is, `raise` a `ValueError` with the message: `"Password must be at least 8 characters long."`
   * Otherwise, return `True`.

### Step 3: Build the Main Registration Flow
1. Below your functions (in the same cell or a new one), 
ask the user for three inputs: a username, an email, and a password, storing them in variables.
2. Create a `try` block. Inside the `try` block, call all three of your validation functions, passing in the user's inputs. 
3. If all three pass without raising an error, print `"Registration successful!"` inside the `try` block.
4. Create an `except ValueError as e:` block immediately after the `try` block.
5. Inside the `except` block, print the error message (`print(f"Registration failed: {e}")`).

*Note: To test your code, click inside your code cell and press **Shift + Enter**. 
Try typing a short password or an email without an '@' symbol in the text boxes that appear, 
and watch your custom error messages elegantly handle the mistakes!*