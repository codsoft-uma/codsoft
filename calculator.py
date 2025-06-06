def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b== 0:
        return "Error: Division by zero"
    return a/b

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (add/subtract/multiply/divide): ")

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
except ValueError:
    print("Invalid input. Please enter numeric values.")
    exit()

if choice == 'add':
    print(f"The result is: {add(num1, num2)}")
elif choice == 'subtract':
    print(f"The result is: {subtract(num1, num2)}")
elif choice == 'multiply':
    print(f"The result is: {multiply(num1, num2)}")
elif choice == 'divide':
    print(f"The result is: {divide(num1, num2)}")
else:
    print(f"Invalid choice")
