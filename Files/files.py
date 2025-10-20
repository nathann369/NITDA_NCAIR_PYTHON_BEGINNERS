import os

# opening a file
def test1():
    f = open("data.txt")
    #print(f)
    for line in f:
        print(line)

    f.close()

# testing if file exists
def test2():
    try:
        # comment: 
        f = open("data2.txt")
        print(f.read())
    except:
        print("File does not exist")
        #raise e
    finally:
        f.close()
        # comment: 
    # end try

# appending a file
def test3():
    f = open("data.txt", "a")
    f.write("OSINT")
    f.write("OSINT\n")
    f.close()

    f = open("data.txt")
    print(f.read())
    f.close()

# Write / overwriting file
def test4():
    f = open("data2.txt", "w")
    f.write("i overwrote all the content ")
    f.close()

    f = open("data2.txt")
    print(f.read())
    f.close()

# creating a new file
# this opens the file and if not existing creats the file
def test5():
    f = open("list.txt", "w")
    f.close

# creats the file but returns an error if the file exists






#test1()
#test2()
# test3()
test4()
test5()