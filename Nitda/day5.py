import math
print("Welcome to sirMath")

print("""I can Handle the following operations
      1. Addition
      2. Subtraction
      3. Multiplication
      4. Divition
      5. Floor Divition
      6. Modulus
      7. Exponent
      8. Logrithm
      """)

operation: str = input("Pick an operation form the options [1 - 8]: ")
num1: str = input("Enter numer: ")
num2: str = input("Enter numer: ")
num1: float = float(num1)
num2: float = float(num2)

if operation == 1:
    print(num1 + num2)
elif operation == 2:
    print(num1 - num2)
elif operation == 3:
    print(num1 * num2)
elif operation == 4:
    print(num1 / num2)
elif operation == 5:
    print(num1 // num2)
elif operation == 6:
    print(num1 % num2)
elif operation == 7:
    print(num1 ** num2)
elif operation == 8:
    result = math.log(num1, num2)
else:
    print("")