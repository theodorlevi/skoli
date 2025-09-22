#!/bin/python

def skrifa_i_skra(listi: dict[str, tuple[int, int]], nafntxt: str):
    file = open(nafntxt, "w")

    for (nafn, value) in listi:
        file.write(" ".join(str(nafn, value[0], value[1])))


def breyta_upplisingum(launalisti: dict[str, tuple[int, int]], nafn: str, laun: int):
    launalisti[nafn] = (launalisti[nafn][0], laun)


