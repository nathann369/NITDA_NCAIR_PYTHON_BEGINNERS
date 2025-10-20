num1 = input("Enter a number: ")
n1 = float(num1)
math = input("Enter an operator (+, -, *, /): ")
num2 = float(input("Enter a numbber: "))
#n2 = float(num2)

if math == "+":
    result = n1 + num2
    print("result is: ", result)
elif math == "-":
    result = n1 - num2
    print("result is: ", result)
elif math == '*':
    result = n1 * num2
    print("result is: ", result)
elif math == '/':
    result = n1 / num2
    print("result is: ", result)