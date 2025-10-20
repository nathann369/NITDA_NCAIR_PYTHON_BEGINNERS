# this function loops through the first loop with the second loop which is called a Nested loop
def loop1():
    numbers = {1,2,3}
    n2 = [2,4,6,8,10]
    for x in numbers:
        for n in n2:
            print("the answer is: ",n)

def loop2():
    for x in range(1,99,5):
        print(x)

def breakTest():
    for x in range(1,21):
        if x == 10:
            break
        else:
            print(x, end="-")
def cont():
    for x in range(1,21):
        if x == 10:
            continue
        else:
            print(x)

def stars():
    rows = int(input("enter number of rows: "))
    cols = int(input("enter number of cols: "))
    sign = input("enter the signs: ")

    for x in range(rows):
        for y in range (cols):
            print(sign, end="")
        print()

#loop1()
#loop2()
#cont()
#breakTest()
stars()