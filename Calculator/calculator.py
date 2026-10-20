#Maths Function
def add (x,y):
    return (x + y)

def Subtract (x,y):
    return (x - y)

def multiply (x,y):
    return (x * y)

def divide (x,y):
    if y == 0:
        return 'cannot divide by zero' 
    return (x/y)


#User Interface
print("Welcome to My Calculator")
print("Select an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input(("Enter choice (1/2/3/4): ")))

#Capturing the Inputs
if (choice in [1, 2, 3, 4]):
    num1 = float(input(("Enter the first number: ")))
    num2 = float(input(("Enter the second number: ")))

#Routing the Logic
if choice == 1:
    result = add(num1, num2)
elif (choice == 2):
    result = Subtract(num1, num2)
elif (choice == 3):
    result = multiply(num1, num2)
elif (choice == 4):
    result = divide(num1, num2)

else:
    print ("Invalid Input")

# Output
print("Result:", result)