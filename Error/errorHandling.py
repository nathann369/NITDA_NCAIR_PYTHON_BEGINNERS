# exception can be handled using try except and optionally finally blocks. 
# if the exception occors in the try block the code in the except block is executed

# f = open('text.txt') #will give an error

def test1():
    try:
        f = open("data/list.txt", "w")
       # print(f.read())
    except FileNotFoundError as e:
        # print("Opps file not found")
        print(e)
    except Exception as e:
        print(e)
    else:
        print(f.read())
        f.close()
    finally:
        print("finally always gets executed regradless of if the code has exceptions or not")

test1()

