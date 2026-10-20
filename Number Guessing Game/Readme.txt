# Mini-Project: The Number Guessing Game

## Objective
In this project, you will build an interactive command-line game where the computer generates a secret number, and the player must guess what it is. You will apply the foundational Python concepts you've learned so far: variables, `input()` functions, `while` loops, and `if/elif/else` conditional statements.

## Prerequisites
Before you begin, ensure you understand:
* How to take user input and convert it to an integer using `int()`.
* How to structure a `while` loop.
* How to write `if`, `elif`, and `else` statements.

## Step-by-Step Instructions

### Step 1: Set Up Your File
1. In your workspace, create a new file named `number_guessing_game.py`.
2. All your code for this project will go inside this file.

### Step 2: Import the Random Module
To make the game unpredictable, the computer needs to pick a random number.
1. At the very top of your file, import Python's built-in random module: 
   `import random`
2. Use `random.randint(1, 100)` to generate a secret number between 1 and 100 and store it in a variable called `secret_number`.

### Step 3: Initialize Game Variables
Set up the variables you will need to track the game's state before the loop starts.
1. Create a variable called `guess` and set it to `0`.
2. Create a variable called `attempts` and set it to `0`. This will track how many tries it takes the player to win.

### Step 4: Create the Game Loop
The game should keep running until the player guesses the correct number.
1. Create a `while` loop that continues to run as long as `guess` is not equal to (`!=`) the `secret_number`.

### Step 5: Capture Player Input and Build Game Logic
Inside your `while` loop:
1. Ask the user for a guess using `input()` and convert it to an integer. Store this in your `guess` variable.
2. Increment your `attempts` variable by 1.
3. Use an `if/elif/else` block to give the player hints:
   * **If** the guess is lower than the `secret_number`, print `"Too low! Try again."`
   * **Elif** the guess is higher than the `secret_number`, print `"Too high! Try again."`
   * **Else** (meaning they guessed correctly), print a congratulatory message that includes the number of `attempts` it took them.

*Note: Save your file and run it in the terminal using `python3 number_guessing_game.py` to test it before submitting!*