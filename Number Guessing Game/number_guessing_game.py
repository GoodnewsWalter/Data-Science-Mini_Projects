import random
secret_number = random.randint(1, 100)
print("Welcome to the Number Guessing Game!")
print("I have selected a number, Can you guess it?")

guess = 0
attempts = 0

while guess != secret_number:
    guess = int(input("Enter your guess: "))

    attempts += 1
    
    if (guess < secret_number):
        print ("\tToo low! Try again.")
    elif (guess > secret_number):
        print ("\tToo high! Try again.")
    else:
        print (f"\nCongratulations!🎉 You guessed the number Correctly in {attempts} attempts." )
