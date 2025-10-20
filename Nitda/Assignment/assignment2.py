'''Assignment 1: find out why we use `is` and `is not` to compare values with None. Instead of `==` and `!=`

Assignment 2: Find out how to make the marriage recommender in `comparisons.py` in the notes for `Class 5` work for bad inputs such as
'AA '
'aa'
'aas '


Assignment 3: Write a calculator program that takes three inputs from the user
num1
num2
Operator / Operation
The program should work for the following cases
#   i. Addition (+)
#   ii. Subtraction (-)
#   iii. Multiplication (*)
#   iv. Division (/)
#   v. Floor Division (//)
#   vi. Modulus (%)
#   vii. Exponent (**)
#   viii. Logarithm (log) - log of num2 to base num1
#   ix. Sine (sin) - sin of num1 (num2 should be ignored)
#   x. Cosine (cos) - cos of num1
#   xi. Tangent (tan) - tan of num1
#   xii. Cosecant (cosec) - cosec of num1
#   xiii. Secant (sec) - sec of num1
#   xiv. Cotangent (cot) - cot of num1
#   xv. ArcSin (asin) - sine inverse of num1
#   xvi. ArcCos (acos) - cosine inverse of num1
#   xvii. ArcTan (atan) - tan inverse of num1
#   xviii. Sinh of num1
#   xix. Cosh of num1
#   xx. Tanh of num1
#   xxi. Exponent (e ^ num1) - e ^ num1'''

"""
Answer 1:
We use is and is not when comparing a value to None because None is a singleton — there is only one instance of None in Python.

is checks for identity — whether two variables point to the same object in the computer memory.  While

== checks for equality — whether the values of two objects are the same.

Since there’s only one None, checking identity with is None is faster, safer, and clearer."""
import math

# Examples:
x = None

if x is None:      # ✅ Correct
    print("x is None")

if x == None:      # ⚠️ Works, but not preferred
    print("x equals None")


"""
Answer 2:
Assuming the program checks blood types and genotypes for compatibility, we need to sanitize inputs by:

Stripping spaces

Converting input to uppercase

Validating against allowed genotypes (AA, AS, SS, etc.)"""

# Example 2:
# valid_genotypes = {"AA", "AS", "SS"}
# print(valid_genotypes)
# genotype1 = input("Enter your genotype: ").strip().upper()
# genotype2 = input("Enter partner's genotype: ").strip().upper()

# if genotype1 not in valid_genotypes or genotype2 not in valid_genotypes:
#     print("Invalid input. Please enter a valid genotype (AA, AS, SS).")
# else:
#     # Continue with compatibility logic
#     if genotype1 == "AA" and genotype2 in ("AA", "AS"):
#         print("You're compatible!")
#     elif genotype1 == "AS" and genotype2 == "AS":
#         print("Caution: Risk of SS child.")
#     elif "SS" in (genotype1, genotype2):
#         print("Not recommended: SS genotype present.")
#     else:
#         print("Consult a doctor.")

# ------------------------------------------ PLEASE UNCOMEMNT TO USE --------------------------------------------------------------

# Example 3

# # Get user inputs
# num1 = float(input("Enter first number (num1): "))
# num2 = float(input("Enter second number (num2): "))
# operation = input("Enter operation: ").strip().lower()

# # Perform operation
# if operation == '+':
#     result = num1 + num2
# elif operation == '-':
#     result = num1 - num2
# elif operation == '*':
#     result = num1 * num2
# elif operation == '/':
#     result = num1 / num2 if num2 != 0 else "Error: Division by zero"
# elif operation == '//':
#     result = num1 // num2 if num2 != 0 else "Error: Division by zero"
# elif operation == '%':
#     result = num1 % num2 if num2 != 0 else "Error: Modulus by zero"
# elif operation == '**':
#     result = num1 ** num2
# elif operation == 'log':
#     result = math.log(num2, num1) if num1 > 0 and num1 != 1 and num2 > 0 else "Error: Invalid log inputs"
# elif operation == 'sin':
#     result = math.sin(math.radians(num1))
# elif operation == 'cos':
#     result = math.cos(math.radians(num1))
# elif operation == 'tan':
#     result = math.tan(math.radians(num1))
# elif operation == 'cosec':
#     sin_val = math.sin(math.radians(num1))
#     result = 1 / sin_val if sin_val != 0 else "Error: Cosecant undefined"
# elif operation == 'sec':
#     cos_val = math.cos(math.radians(num1))
#     result = 1 / cos_val if cos_val != 0 else "Error: Secant undefined"
# elif operation == 'cot':
#     tan_val = math.tan(math.radians(num1))
#     result = 1 / tan_val if tan_val != 0 else "Error: Cotangent undefined"
# elif operation == 'asin':
#     result = math.degrees(math.asin(num1)) if -1 <= num1 <= 1 else "Error: Input out of domain"
# elif operation == 'acos':
#     result = math.degrees(math.acos(num1)) if -1 <= num1 <= 1 else "Error: Input out of domain"
# elif operation == 'atan':
#     result = math.degrees(math.atan(num1))
# elif operation == 'sinh':
#     result = math.sinh(num1)
# elif operation == 'cosh':
#     result = math.cosh(num1)
# elif operation == 'tanh':
#     result = math.tanh(num1)
# elif operation == 'e':
#     result = math.exp(num1)
# else:
#     result = "Invalid operation"

# print("Result:", result)
