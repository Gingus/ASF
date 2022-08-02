import random


status = True
k1 = []
cmel = []

ckey = ["c", "d", "e", "f", "g", "a", "b"]
dkey = ["d", "e", "f#", "g", "a", "b", "c"]


def continue_prog():
    """asking for 1/yes or 2/no and return Val!"""
    cont = int(input("do you want to go again \n"
                     "1 for yes \n"
                     "2 for no"))
    while cont != int():
        cont = int(input("That needs to be a 1 or 2 please \n"
                         "do you want to go again \n"
                         "1 for yes \n"
                         "2 for no"))
    return cont


def kill():
    """Continues or stops the program"""
    global status
    confirm = input("again (Y/n)  :  ")
    if confirm == "n":
        status = False
    else:
        pass


def melody(key):
    """Print"""
    key = key
    randomiser = random.randint(0, 6)
    # if key =
    print(randomiser)


# def keychange():
#     c = a + b


while status == True:
    """Creates a melody"""
    cont = continue_prog()
    inp1 = input("press 1 for a 4 note melody \n "
                 "press 2 for key change")
    if inp1 == "1":
        jeff = int(input("how many notes do you need in your melody?"))
        for x in range(jeff):
            melody()

    elif inp1 == "2":
        inpkey = int(input("1 for c \n"
                           "2 for dmaj"))
        k1.append(inpkey)
        if inpkey == 1:
            cmelinp = input("enter your melody without spaces")
            count = len(cmelinp)
            int2str = str(count)
            x = cmelinp.split(int2str)
            cmel.append(x)
            print(cmel)
            break



