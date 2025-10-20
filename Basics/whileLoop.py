

def loop1():
    global name
    name = input("enter a name: ").title()
    while name == "":
        print("you havent enter any name")
        name = input("enter a name: ").title()
    print(f"weldon {name}")

def loop2():
    global age
    age = int(input("enter your age: "))
    while age < 5:
        print("invalid age")
        print("you must be above 5 years old to use this app")
        age = int(input("enter your age: "))
    print(f"Hey {name} You are {age} years old")

def loop3():
    global food
    food = input("Enter a food you like (q to QUIT): ")
    while not food  == "q":
        print(f"Hey {name} You like {food}")
        food = input("Enter another food you like (q to QUIT): ")
    print(f"Thanks {name} Bye")

def loop4():
    global num
    num = int(input("Enter a # between 1 - 10: "))
    while num < 1 or num > 10:
        print(f"{num} is not valid")
        num = int(input("Enter a # between 1 - 10: "))
    print(f"{name} The number you enrtered is {num}")
    print(f"Thanks {name} Bye")
     
def main():
    loop1()
    loop2()
    loop3()
    loop4()

main()

