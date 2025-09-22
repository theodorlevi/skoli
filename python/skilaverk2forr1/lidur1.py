from random import randint
from math import factorial

def main():

    inp = input("sláðu inn val, 1, 8: ")

    match inp:
        case "1":
            talnabil_a()
        case "2":
            talnabil_b()
        case "3":
            gaman()
        case "4":
            teninga_leikur()
        case "5":
            margfoldun()
        case "6":
            medaltal()
        case "7":
            ymislegt()
        case _: # virkar líka sem hætta
            return 0
    main()
    return 1


def talnabil_a():
    inp1 = int(input("tala1: "))
    inp2 = int(input(""))

    summa = 0

    print(inp1, "~", inp2)
    for i in range(inp1, inp2):
        print(i, end=" ")
        summa += i
    print("summa: ", summa)

def talnabil_b():
    tolur = [i for i in range(100, 201)]

    for tala in tolur:
        if tala % 4 == 0 and tala % 5 != 0:
            print("Júdó")
        elif tala % 5 == 0 and tala % 4 != 0:
            print("Kung-Fu")
        elif tala % 5 == 0 and tala % 4 == 0:
            print("Jiu-Jitzu")
        else:
            print(tala)

def gaman():
    inp = int(input("hversu oft villtu sjæa whoohoo: "))

    for i in range(inp + 1):
        for j in range(i):
            if j == 0:
                print("whoohoo ", end="")
            else:
                print("- whoohoo ", end="")
        print("")

def teninga_leikur():
    leikmadur1_sum = 0
    leikmadur2_sum = 0

    for _ in range(5):
        randnum = randint(1, 6)
        print("leikmaður 1: ", randnum)
        leikmadur1_sum += randnum
        randnum = randint(1, 6)
        print("leikaður 2: ", randnum)
        leikmadur2_sum += randnum

    if leikmadur2_sum > leikmadur1_sum:
        print("leimaður 2 vann")
    elif leikmadur1_sum > leikmadur2_sum:
        print("leikmaður 1 vann")
    else:
        print("jafntefli")

def margfoldun():
    print(factorial(int(input("sláðu inn tölu: "))))

def medaltal():
    tolur = []
    num_tolur = 0
    sum_tolur = 0

    while True:
        inp = input("sláðu inn tölu eða - til að hætta")
        if inp == "-":
            break
        else:
            tolur.append(float(inp))
            num_tolur += 1
            sum_tolur += float(inp)
    print("magn talna: ", num_tolur)
    print("medal tal: ", sum_tolur / num_tolur )

def ymislegt():
    keyrslur = 0

    while True:
        keyrslur += 1
        val = input("veldu, 1, 3")

        match val:
            case "1":
                summa = 0
                magn = 0

                for _ in range(10):
                    summa += float(input("skrifaðu tölu: "))
                    magn += 1
                print("meðaltal: ", summa / magn)
                print("summa: ", summa)
            case "2":
                if int(input("skrifaðu tölu: ")) % 2 == 0:
                    print("slétt tala")
                else:
                    print("odda tala")
            case _:
                for _ in range(10):
                    print("Ég er frábær forritari")
                break

exit(main())