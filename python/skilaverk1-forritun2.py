#!/bin/python

import random

def main():
    val = int(input("vinsamlegast veldu lið 1, 6(hætta): "))


    match val:
        case 1:
            listi()
        case 2:
            skraningaform()

        case 6:
            return 0
    return None


def listi():
    tolulisti = []
    for i in range(60):
        tolulisti.append(random.randint(10, 99))

    print("þú getur:\n1. prentað út listan 10 tölur í línu\n2. prentað út hversu oft talan 15 kemur\n3. prentað út meðaltal talnana\n4. prentað listan í öfugri röð 20 í línu\n5. prenta hversu margar tölur eru á bilinu 50 - 99")
    val = int(input("hvað villtu gera: "))

    match val:
        case 1:
            for i in range(len(tolulisti)):
                print(tolulisti[i] + " ", end='')
                if i % 10 == 0:
                    print("\n", end='')
            print("\n")

        case 2:
            total15 = 0
            for tala in tolulisti:
                if tala == 15:
                    total15 += 1

            print(total15)

        case 3:
            total = 0
            for tala in tolulisti:
                total += tala

            print(total / 60)

        case 4:
            tolulisti.reverse()

            for i in range(60):
                print(str(tolulisti[i]) + " ", end='')
                if i % 20 == 0:
                    print("\n", end='')
            print("\n")
        case 5:
            total = 0
            for tala in tolulisti:
                if tala >= 50:
                    total += 1
            print(total)

def skraningaform():
    nemenda_tal = int(input("hversu margir nemendur?: "))
    nemenda_nofn = []

    for i in range(nemenda_tal):
        nemenda_nofn.append(input("sláðu inn nafn nemenda" + str(i) + ": "))

    nemenda_nofn.sort()
    




while True:
    if main() == 0:
        break
