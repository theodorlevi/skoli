#!/bin/python

import random

def medaltal(nafn_a_skra: str):
    num_list = open(nafn_a_skra, "r").read().split()
    sum_num = 0
    num_ammount = 0
    for n in num_list:
        if int(n) > 28:
            continue
        else:
            num_ammount += 1
            sum_num += int(n)
    return sum_num / num_ammount



def lesa_lista(nafn_a_skra: str):
    file = open(nafn_a_skra).read().split()
    i = 0
    for n in file:
        if n is None: continue
        if i % 20 == 0:
            print()
        print(n, end=" ")
        i += 1
    print("\n")

def skrifa_lista(nafn_a_skra: str, listi: list[str]):
    file = open(nafn_a_skra, "w")
    file.write(" ".join(listi))


skrifa_lista("tolur.txt", [str(random.randint(20, 40)) for i in range(100)])
lesa_lista("tolur.txt")
print(f"{round(medaltal("tolur.txt"), 1)}")
