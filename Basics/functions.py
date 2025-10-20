def test1(name, blunt):
    print(f"Hello, how are you: {name}")
    print(f"pass me  {blunt} blunt {name}")
    print()


def invoice(username, amount, date):
    print(f"Hello{username} ")
    print(F"Your bill is ${amount:.2f}, and the due date is {date}")

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

fullname = create_name("Big", "nate")
print(fullname)

#invoice("bigNate",200, 2023)
#test1("nate", 2)