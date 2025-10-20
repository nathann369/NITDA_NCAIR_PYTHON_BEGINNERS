data = input("enter the data: ")
print("The data is ",data)
print(f"The data is {data}")
print(f"{data:>20}\n")
print(f"{data:<20}\n")
print(f"{data:^20}\n")
print(f"{1_000_000.2657:,.2f}")


num1 = 20000
num2 = 3e5

#shft + alt + down to duplicate down

#add
result = num1 + num2
print(f"{result = :,.2f}")
print(f"{type(result) = }")

#subtrasctioin
result = num1 - num2
print(f"{result = :,.2f}")
print(f"{type(result) = }")

#multiplication
result = num1 * num2
print(f"{result = :,.2f}")
print(f"{type(result) = }")

#divition
result = num1 // num2
print(f"{result = :,.2f}")
print(f"{type(result) = }")

#exponent
x1 = 200
x2 = 2
result = x1 ** x2
print(f"{result = :,.2f}")
print(f"{type(result) = }")


# x = 0
# y = 1
# x == y
# x != y
# x > y
# x >= y
# x < y
# x <= y