from random import randint

Firstname: str = input("Enter your firstname: ").strip().title()
Lastname: str = input("Enter your lastname: ").strip().title()

rand: int = randint(0, 10)


username = Firstname + Lastname + str(rand)
pas = Lastname + str(rand)

print(f"Your Username is {username}")

print(f"Your password is {pas}")


##LOGIN 

user: str = input("Enter you username: ")
while user != username:
    print("invalid user or password!!!")
    user: str = input("Enter you username: ")
else:
    password = input("Enter your Password: ")
    while password != pas:
        print("Incorrect Details")
        password = input("Enter your Password: ")
    else:
       print("Welcome To The Metrixx")
