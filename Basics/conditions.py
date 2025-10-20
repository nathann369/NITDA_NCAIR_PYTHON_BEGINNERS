def test1():
    age = int(input("Enter Your age: "))
    if age >= 50:
        print("You are to old to sign up")
    elif age < 18:
        print("you have signed up")
    elif age <= 5:
        print("put down that device Kid!!")
    else:
        print("You must be 18 and above to sign up")

def test2():
    res = input("would you like some code? (Y/N): ")
    if res == "Y":
        print("here is my github link (github/nathan)")
    else:
        print("AWWWW too bad")

def test3():
    name = input("Enter you name: ")
    if name == "":
        print("Whatsup "+ {name})

def test4():
    is_active = True #False
    if is_active:
        print("Oya Paste the slip")
    else:
        print("Sleepy Head")

test4()